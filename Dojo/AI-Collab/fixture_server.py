# fixture_server.py
import http.server
import socketserver
import json
import threading
import os
import sys
import argparse
import time
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

# --- Configuration ---
HOST = "127.0.0.1"
PORT = 5999
TRUTH_FILE = "truth.json"
CONV_A_ID = "conv_a"
CONV_B_ID = "conv_b"
SELF_TEST_CMD = "--self-test"

# --- Initial Data ---
INITIAL_TRUTH_DATA = {
    "conversations": {
        CONV_A_ID: {
            "conv_id": CONV_A_ID,
            "messages": [
                {"role": "user", "content": "A-user-1"},
                {"role": "assistant", "content": "A-assistant-1"},
                {"role": "user", "content": "A-user-2"},
                {"role": "assistant", "content": "A-assistant-2"}
            ]
        },
        CONV_B_ID: {
            "conv_id": CONV_B_ID,
            "messages": [
                {"role": "user", "content": "B-user-1"},
                {"role": "assistant", "content": "B-assistant-1"},
                {"role": "user", "content": "B-user-2"},
                {"role": "assistant", "content": "B-assistant-2"}
            ]
        }
    },
    "switch_conv_a_to_b": False
}

# --- File Operations ---
def get_truth_file_path():
    # Assuming the script is run from the directory it resides in,
    # or the current working directory is set to the script's directory.
    # For robustness, we might want to resolve based on __file__ if available.
    # For now, assuming cwd is the project root as per context.
    return os.path.join(os.getcwd(), TRUTH_FILE)

def load_truth_data():
    truth_path = get_truth_file_path()
    if os.path.exists(truth_path):
        try:
            with open(truth_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Error decoding {TRUTH_FILE}. Starting with default.", file=sys.stderr)
            return INITIAL_TRUTH_DATA.copy()
        except Exception as e:
            print(f"Error loading {TRUTH_FILE}: {e}. Starting with default.", file=sys.stderr)
            return INITIAL_TRUTH_DATA.copy()
    else:
        return INITIAL_TRUTH_DATA.copy()

def save_truth_data(data):
    truth_path = get_truth_file_path()
    temp_path = truth_path + ".tmp"
    try:
        with open(temp_path, 'w') as f:
            json.dump(data, f, indent=2)
        os.replace(temp_path, truth_path) # Atomic rename
        return True
    except Exception as e:
        print(f"Error saving {TRUTH_FILE}: {e}", file=sys.stderr)
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return False

# --- HTTP Handler ---
class FixtureHandler(http.server.SimpleHTTPRequestHandler):
    # Server version and system version to suppress in headers
    server_version = "FixtureServer/1.0"
    sys_version = ""

    def __init__(self, *args, **kwargs):
        # Directory parameter ensures it serves from the script's directory if run directly
        # but SPEC implies it should be run from AI-Collab root. Let's rely on cwd.
        # However, for self-test, we need to ensure it's in the right dir.
        # For now, assume cwd is correct or script is run from its dir.
        super().__init__(*args, directory=os.getcwd(), **kwargs)
        # Load data when handler is instantiated for a request
        self.truth_data = load_truth_data()

    def do_GET(self):
        # Always reload truth data for /conv_a and /conv_b to ensure latest state is served,
        # especially for persistence testing. This ensures that the handler sees
        # the most recent state from disk, even if it wasn't reloaded by a previous handler instance.
        self.truth_data = load_truth_data()

        if self.path == "/conv_a":
            self.handle_conv_a()
        elif self.path == "/conv_b":
            self.handle_conv_b()
        elif self.path.startswith("/switch"):
            self.handle_switch()
        elif self.path == "/health":
            self.handle_health()
        elif self.path in ["/truth", "/truth.json"]:
            self.send_error(404, "Not Found")
        else:
            # If the path is not one of our specific endpoints and not a forbidden one,
            # try to serve it as a static file from the current directory.
            # According to SPEC, no static files are expected, so this might just result in 404s.
            super().do_GET()

    def handle_conv_a(self):
        if self.truth_data["switch_conv_a_to_b"]:
            conversation = self.truth_data["conversations"].get(CONV_B_ID)
        else:
            conversation = self.truth_data["conversations"].get(CONV_A_ID)

        if not conversation:
            self.send_error(500, "Conversation data missing.")
            return

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {
            "conv_id": conversation["conv_id"],
            "messages": conversation["messages"]
        }
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def handle_conv_b(self):
        conversation = self.truth_data["conversations"].get(CONV_B_ID)
        if not conversation:
            self.send_error(500, "Conversation data missing.")
            return

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {
            "conv_id": conversation["conv_id"],
            "messages": conversation["messages"]
        }
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def handle_switch(self):
        query_params = self.path.split("?", 1)
        if len(query_params) > 1:
            params_str = query_params[1]
            params = dict(qc.split("=") for qc in params_str.split("&") if "=" in qc) # Safely split parameters

            if "value" in params:
                new_value_str = params["value"]
                new_value = None
                if new_value_str.lower() == "true":
                    new_value = True
                elif new_value_str.lower() == "false":
                    new_value = False

                if new_value is not None:
                    # Update truth data and persist
                    self.truth_data["switch_conv_a_to_b"] = new_value
                    if save_truth_data(self.truth_data):
                        response = {
                            "ok": True,
                            "switch_conv_a_to_b": new_value
                        }
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(response).encode("utf-8"))
                        return
                    else:
                        self.send_error(500, "Failed to persist switch state.")
                        return
                else:
                    self.send_error(400, "Invalid value for 'value' parameter. Must be 'true' or 'false'.")
                    return
        self.send_error(400, "Missing or invalid 'value' parameter for switch. Expected format: /switch?value=true|false")

    def handle_health(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"ok": True}).encode("utf-8"))

# --- Server Startup ---
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True # Allows the server to be restarted quickly

    def __init__(self, server_address, RequestHandlerClass):
        # We need to ensure the handler knows the correct directory for file operations.
        # The directory should be where the script is run from, which is typically the project root.
        super().__init__(server_address, RequestHandlerClass)
        self.shutdown_event = threading.Event()

    def process_request(self, request, client_address):
        """Override to handle potential exceptions during request processing."""
        try:
            super().process_request(request, client_address)
        except Exception as e:
            print(f"Error processing request from {client_address}: {e}", file=sys.stderr)
            # Continue serving other requests

    def serve_forever(self, poll_interval=0.5):
        """Handle requests indefinitely. Use shutdown_event to stop."""
        self.shutdown_event.clear()
        # Use a loop that checks the shutdown event periodically
        while not self.shutdown_event.is_set():
            try:
                # Serve one request, but this might block.
                # A more sophisticated server might use select or other mechanisms
                # for non-blocking server shutdown.
                # For this use case, handle_request() is okay if we call shutdown()
                # which should unblock it.
                self.handle_request()
            except Exception as e:
                # Catch potential errors during handle_request if they are not caught by the handler itself
                print(f"Exception in serve_forever loop: {e}", file=sys.stderr)
                if self.shutdown_event.is_set():
                    break # Exit if shutdown is requested
                time.sleep(poll_interval) # Wait before checking again if not shutting down

    def shutdown(self):
        """Set the shutdown event and call the parent shutdown."""
        self.shutdown_event.set()
        super().shutdown() # This should unblock the serve_forever loop

def start_server(host=HOST, port=PORT):
    """Starts the fixture server and returns the server instance and thread."""
    print(f"Attempting to start server on {host}:{port}...", file=sys.stderr)
    try:
        # Ensure truth.json exists before starting, or create it with default data
        initial_data = load_truth_data()
        if not os.path.exists(get_truth_file_path()):
            if not save_truth_data(initial_data):
                print(f"FATAL: Could not create initial {TRUTH_FILE}.", file=sys.stderr)
                sys.exit(1) # Critical failure

        server_address = (host, port)
        httpd = ThreadedTCPServer(server_address, FixtureHandler)

        # Start server in a new thread so main thread can continue (e.g., for self-test or wait)
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True  # Allow main program to exit even if server thread is running
        server_thread.start()
        print(f"Server successfully started on {host}:{port}", file=sys.stderr)
        return httpd, server_thread
    except OSError as e:
        if e.errno == 98: # Address already in use
            print(f"FATAL: port {port} is occupied. STEP 1 requires {port}. Do not auto-select another port.", file=sys.stderr)
            sys.exit(1) # Exit with error code as per SPEC
        else:
            print(f"Error starting server on {host}:{port}: {e}", file=sys.stderr)
            sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during server startup: {e}", file=sys.stderr)
        sys.exit(1)

# --- Self-Test ---
def run_self_test():
    print("Running self-test...", file=sys.stderr)
    truth_path = get_truth_file_path()
    # Clean up truth.json if it exists for a clean test start
    if os.path.exists(truth_path):
        try:
            os.remove(truth_path)
            print(f"Removed existing {TRUTH_FILE}", file=sys.stderr)
        except Exception as e:
            print(f"Error removing {TRUTH_FILE} before test: {e}", file=sys.stderr)
            return f"FAIL — Error removing {TRUTH_FILE} before test: {e}", 1

    # Start server in a separate thread for testing
    server_address = (HOST, PORT)
    httpd = None
    server_thread = None
    test_results = []
    exit_code = 0

    try:
        print(f"Attempting to start test server on {HOST}:{PORT}...", file=sys.stderr)
        httpd = ThreadedTCPServer(server_address, FixtureHandler)
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print(f"Test server thread started.", file=sys.stderr)
    except OSError as e:
        if e.errno == 98:
            error_msg = f"FAIL — Port {PORT} occupied. STEP 1 requires {PORT}. Do not auto-select another port."
            print(error_msg, file=sys.stderr)
            return error_msg, 1
        else:
            error_msg = f"FAIL — Error starting test server: {e}"
            print(error_msg, file=sys.stderr)
            return error_msg, 1
    except Exception as e:
        error_msg = f"FAIL — Unexpected error starting test server: {e}"
        print(error_msg, file=sys.stderr)
        return error_msg, 1

    # Wait a bit for server to fully initialize and bind to port
    time.sleep(2) # Increased sleep for better reliability

    # --- Test Steps ---
    try:
        # Step 3: Check /health, /conv_a, /conv_b
        print("Test 3: Checking /health, /conv_a, /conv_b...", file=sys.stderr)
        try:
            health_url = f"http://{HOST}:{PORT}/health"
            req = Request(health_url, headers={'Accept': 'application/json'})
            with urlopen(req, timeout=5) as resp:
                health_data = json.loads(resp.read().decode())
                if health_data.get("ok") != True:
                    test_results.append(f"GET /health did not return {{'ok': true}}. Got: {health_data}")
                    exit_code = 1
        except Exception as e:
            test_results.append(f"Error checking /health: {e}")
            exit_code = 1

        conv_a_data = None
        conv_a_resp_headers = None
        try:
            conv_a_url = f"http://{HOST}:{PORT}/conv_a"
            req_a = Request(conv_a_url, headers={'Accept': 'application/json'})
            with urlopen(req_a, timeout=5) as resp_a:
                conv_a_data = json.loads(resp_a.read().decode())
                conv_a_resp_headers = resp_a.info()
                if conv_a_data.get("conv_id") != CONV_A_ID or len(conv_a_data.get("messages", [])) != 4:
                    test_results.append(f"GET /conv_a did not return correct conv_id or message count. Expected '{CONV_A_ID}' and 4 messages. Got: {conv_a_data.get('conv_id')}, {len(conv_a_data.get('messages', []))} messages.")
                    exit_code = 1
        except Exception as e:
            test_results.append(f"Error checking /conv_a: {e}")
            exit_code = 1

        conv_b_data = None
        try:
            conv_b_url = f"http://{HOST}:{PORT}/conv_b"
            req_b = Request(conv_b_url, headers={'Accept': 'application/json'})
            with urlopen(req_b, timeout=5) as resp_b:
                conv_b_data = json.loads(resp_b.read().decode())
                if conv_b_data.get("conv_id") != CONV_B_ID or len(conv_b_data.get("messages", [])) != 4:
                    test_results.append(f"GET /conv_b did not return correct conv_id or message count. Expected '{CONV_B_ID}' and 4 messages. Got: {conv_b_data.get('conv_id')}, {len(conv_b_data.get('messages', []))} messages.")
                    exit_code = 1
        except Exception as e:
            test_results.append(f"Error checking /conv_b: {e}")
            exit_code = 1

        # Step 4: Read truth.json and check content
        print("Test 4: Checking truth.json content...", file=sys.stderr)
        try:
            with open(truth_path, 'r') as f:
                truth_content = json.load(f)
            if truth_content.get("switch_conv_a_to_b") != False:
                test_results.append(f"Initial truth.json has incorrect 'switch_conv_a_to_b'. Expected false, got {truth_content.get('switch_conv_a_to_b')}")
                exit_code = 1
            if CONV_A_ID not in truth_content.get("conversations", {}) or len(truth_content["conversations"][CONV_A_ID].get("messages", [])) != 4:
                 test_results.append(f"Initial truth.json has incorrect conv_a messages. Expected 4, got {len(truth_content['conversations'].get(CONV_A_ID, {}).get('messages', []))}")
                 exit_code = 1
            if CONV_B_ID not in truth_content.get("conversations", {}) or len(truth_content["conversations"][CONV_B_ID].get("messages", [])) != 4:
                 test_results.append(f"Initial truth.json has incorrect conv_b messages. Expected 4, got {len(truth_content['conversations'].get(CONV_B_ID, {}).get('messages', []))}")
                 exit_code = 1

            # Compare conv_a response with truth.json
            if conv_a_data and truth_content["conversations"][CONV_A_ID]["messages"] != conv_a_data["messages"]:
                test_results.append("GET /conv_a messages do not match truth.json conv_a messages.")
                exit_code = 1
            if conv_b_data and truth_content["conversations"][CONV_B_ID]["messages"] != conv_b_data["messages"]:
                test_results.append("GET /conv_b messages do not match truth.json conv_b messages.")
                exit_code = 1

        except FileNotFoundError:
            test_results.append(f"{TRUTH_FILE} not found after server start.")
            exit_code = 1
        except Exception as e:
            test_results.append(f"Error reading or validating {TRUTH_FILE}: {e}")
            exit_code = 1

        # Step 5: Execute GET /switch?value=true
        print("Test 5: Switching conv_a to conv_b...", file=sys.stderr)
        try:
            switch_url_true = f"http://{HOST}:{PORT}/switch?value=true"
            req_switch_true = Request(switch_url_true, headers={'Accept': 'application/json'})
            with urlopen(req_switch_true, timeout=5) as resp_switch_true:
                switch_data_true = json.loads(resp_switch_true.read().decode())
                if switch_data_true.get("ok") != True or switch_data_true.get("switch_conv_a_to_b") != True:
                    test_results.append(f"GET /switch?value=true did not return expected response. Got: {switch_data_true}")
                    exit_code = 1
        except Exception as e:
            test_results.append(f"Error during GET /switch?value=true: {e}")
            exit_code = 1

        # Step 6 & 7: Read truth.json again and check /conv_a response
        print("Test 6 & 7: Verifying persistence and /conv_a switch...", file=sys.stderr)
        try:
            with open(truth_path, 'r') as f:
                truth_content_after_switch = json.loads(f.read()) # Read again to ensure it's fresh from disk
            if truth_content_after_switch.get("switch_conv_a_to_b") != True:
                test_results.append(f"truth.json not updated correctly after switch. Expected 'switch_conv_a_to_b': true, got {truth_content_after_switch.get('switch_conv_a_to_b')}")
                exit_code = 1

            req_a_after_switch = Request(f"http://{HOST}:{PORT}/conv_a", headers={'Accept': 'application/json'})
            with urlopen(req_a_after_switch, timeout=5) as resp_a_after_switch:
                conv_a_data_after_switch = json.loads(resp_a_after_switch.read().decode())
                if conv_a_data_after_switch.get("conv_id") != CONV_B_ID or len(conv_a_data_after_switch.get("messages", [])) != 4:
                    test_results.append(f"GET /conv_a after switch did not serve conv_b. Got conv_id: {conv_a_data_after_switch.get('conv_id')}, {len(conv_a_data_after_switch.get('messages', []))} messages.")
                    exit_code = 1
                if conv_a_data_after_switch.get("messages") != truth_content_after_switch["conversations"][CONV_B_ID]["messages"]:
                    test_results.append("GET /conv_a messages after switch do not match truth.json conv_b messages.")
                    exit_code = 1

        except FileNotFoundError:
            test_results.append(f"{TRUTH_FILE} not found after switch test.")
            exit_code = 1
        except Exception as e:
            test_results.append(f"Error after switch test: {e}")
            exit_code = 1

        # Step 8 & 10: Execute GET /switch?value=false and check /conv_a again
        print("Test 8 & 10: Switching back and verifying...", file=sys.stderr)
        try:
            switch_url_false = f"http://{HOST}:{PORT}/switch?value=false"
            req_switch_false = Request(switch_url_false, headers={'Accept': 'application/json'})
            with urlopen(req_switch_false, timeout=5) as resp_switch_false:
                switch_data_false = json.loads(resp_switch_false.read().decode())
                if switch_data_false.get("ok") != True or switch_data_false.get("switch_conv_a_to_b") != False:
                    test_results.append(f"GET /switch?value=false did not return expected response. Got: {switch_data_false}")
                    exit_code = 1

            req_a_after_reset = Request(f"http://{HOST}:{PORT}/conv_a", headers={'Accept': 'application/json'})
            with urlopen(req_a_after_reset, timeout=5) as resp_a_after_reset:
                conv_a_data_after_reset = json.loads(resp_a_after_reset.read().decode())
                if conv_a_data_after_reset.get("conv_id") != CONV_A_ID or len(conv_a_data_after_reset.get("messages", [])) != 4:
                    test_results.append(f"GET /conv_a after reset did not serve conv_a. Got conv_id: {conv_a_data_after_reset.get('conv_id')}, {len(conv_a_data_after_reset.get('messages', []))} messages.")
                    exit_code = 1

        except Exception as e:
            test_results.append(f"Error during GET /switch?value=false: {e}")
            exit_code = 1

        # Step 11: Check forbidden endpoints
        print("Test 11: Checking forbidden endpoints...", file=sys.stderr)
        for forbidden_path in ["/truth", "/truth.json"]:
            try:
                req = Request(f"http://{HOST}:{PORT}{forbidden_path}", headers={'Accept': 'application/json'})
                urlopen(req, timeout=5)
                test_results.append(f"Access to forbidden path {forbidden_path} was not blocked (should be 404).")
                exit_code = 1
            except HTTPError as e:
                if e.code != 404:
                    test_results.append(f"Forbidden path {forbidden_path} returned unexpected status {e.code}.")
                    exit_code = 1
            except Exception as e:
                test_results.append(f"Error checking forbidden path {forbidden_path}: {e}")
                exit_code = 1

    except URLError as e:
        test_results.append(f"Network error during tests: {e}")
        exit_code = 1
    except Exception as e:
        test_results.append(f"Unexpected error during tests: {e}")
        exit_code = 1
    finally:
        # Stop the server
        print("Stopping test server...", file=sys.stderr)
        if httpd:
            httpd.shutdown()
        if server_thread and server_thread.is_alive():
            server_thread.join(timeout=5) # Wait for server thread to finish
            if server_thread.is_alive():
                print("Server thread did not shut down cleanly.", file=sys.stderr)

    if not test_results:
        final_output = "SELF-TEST: PASS"
        print(final_output, file=sys.stderr)
    else:
        final_output = f"SELF-TEST: FAIL — {'; '.join(test_results)}"
        print(final_output, file=sys.stderr)

    return final_output, exit_code

# --- Main Execution ---
if __name__ == "__main__":
    # Ensure that the script runs from the project root for file path consistency.
    # The context indicates E:\Gemini\Dojo\AI-Collab is the ROOT.
    # If the script is run from a subdirectory, this might need adjustment.
    # For now, assume it's run from the project root.
    # os.chdir(os.path.dirname(os.path.abspath(__file__))) # This would change CWD to script dir.
    # Better to rely on user running it from correct CWD or handle it in start_server/run_self_test

    parser = argparse.ArgumentParser(description="Local fixture server for AI-Collab.")
    parser.add_argument(SELF_TEST_CMD, action="store_true", help="Run self-test and exit.")

    args = parser.parse_args()

    if args.self_test:
        test_output, exit_code = run_self_test()
        print(test_output)
        sys.exit(exit_code)
    else:
        # Normal server run
        httpd, server_thread = start_server()
        try:
            # Keep the main thread alive to keep the server running.
            # The server is designed to run in a separate thread and `serve_forever`
            # should block until `httpd.shutdown()` is called.
            # This loop is a common pattern to keep the main thread alive.
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received. Shutting down server...", file=sys.stderr)
            httpd.shutdown()
            if server_thread.is_alive():
                server_thread.join(timeout=5) # Wait for server thread to finish
            print("Server shut down.", file=sys.stderr)
        except Exception as e:
            print(f"An error occurred in the main loop: {e}", file=sys.stderr)
            httpd.shutdown()
            if server_thread.is_alive():
                server_thread.join(timeout=5)
