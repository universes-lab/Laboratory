# fixture_server.py
import http.server
import socketserver
import json
import threading
import os
import sys
import argparse
import time
from urllib.parse import urlparse, parse_qs # Import urlparse and parse_qs
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from pathlib import Path

# --- Configuration ---
HOST = "127.0.0.1"
PORT = 5999
TRUTH_FILE = "truth.json"
CONV_A_ID = "conv_a"
CONV_B_ID = "conv_b"
FIXTURE_HEALTH_URL = f"http://{HOST}:{PORT}/health"
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
    return Path.cwd() / TRUTH_FILE

def load_truth_data():
    truth_path = get_truth_file_path()
    if truth_path.exists():
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
    temp_path = truth_path.with_suffix('.tmp')
    try:
        with open(temp_path, 'w') as f:
            json.dump(data, f, indent=2)
        os.replace(str(temp_path), str(truth_path)) # Atomic rename
        return True
    except Exception as e:
        print(f"Error saving {TRUTH_FILE}: {e}", file=sys.stderr)
        if temp_path.exists():
            temp_path.unlink()
        return False

# --- HTTP Handler ---
class FixtureHandler(http.server.SimpleHTTPRequestHandler):
    server_version = "FixtureServer/1.0"
    sys_version = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.truth_data = load_truth_data()

    def do_GET(self):
        self.truth_data = load_truth_data()
        url_parts = urlparse(self.path)
        path = url_parts.path
        query = parse_qs(url_parts.query)

        print(f"Received request for path: {path} with query: {query}", file=sys.stderr) # Debugging line

        if path == "/conv_a":
            # Logic for conv_a: depends on switch_conv_a_to_b flag
            conversation_to_serve = self.truth_data["conversations"].get(CONV_A_ID if not self.truth_data["switch_conv_a_to_b"] else CONV_B_ID)
            if query.get("format") == ["html"]:
                self._serve_conversation_html(conversation_to_serve)
            else:
                self._serve_conversation_json(conversation_to_serve)
        elif path == "/conv_b":
            # Logic for conv_b: always serves conv_b
            conversation_to_serve = self.truth_data["conversations"].get(CONV_B_ID)
            if query.get("format") == ["html"]:
                self._serve_conversation_html(conversation_to_serve)
            else:
                self._serve_conversation_json(conversation_to_serve)
        elif path.startswith("/switch"):
            self.handle_switch()
        elif path == "/health":
            self.handle_health()
        elif path in ["/truth", "/truth.json"]:
            self.send_error(404, "Not Found")
        else:
            # Fallback for other paths, should ideally lead to 404 if not in routes
            super().do_GET()

    def _serve_conversation_html(self, conversation):
        """Helper to serve conversation data as HTML."""
        if not conversation:
            self.send_error(500, "Conversation data missing.")
            return

        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>conv_{conversation['conv_id']}</title>
    <style>
        body {{ font-family: sans-serif; padding: 12px; font-size: 13px; background: #fff; }}
        .conv-header {{ font-weight: bold; margin-bottom: 10px; color: #2c3e50; }}
        .msg {{ margin-bottom: 8px; padding: 6px 8px; border-radius: 4px; }}
        .msg.user {{ background: #e3f2fd; }}
        .msg.assistant {{ background: #f5f5f5; }}
        .msg .role {{ font-size: 11px; color: #7f8c8d; margin-bottom: 2px; }}
        .msg .content {{ white-space: pre-wrap; }}
    </style>
</head>
<body>
    <div class="conv-header">{conversation['conv_id']}</div>
    <p>Messages:</p>
    <ul>
"""
        for msg in conversation["messages"]:
            escaped_role = msg['role'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            escaped_content = msg['content'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            html_content += f"        <li><div class='role'>{escaped_role}</div><div class='content'>{escaped_content}</div></li>\n"
        html_content += """    </ul>
</body>
</html>
"""
        response_data = html_content.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(response_data)))
        self.end_headers()
        self.wfile.write(response_data)

    def _serve_conversation_json(self, conversation):
        """Helper to serve conversation data as JSON."""
        if not conversation:
            self.send_error(500, "Conversation data missing.")
            return

        response_dict = {
            "conv_id": conversation["conv_id"],
            "messages": conversation["messages"]
        }
        response_data = json.dumps(response_dict).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Content-Length", str(len(response_data)))
        self.end_headers()
        self.wfile.write(response_data)

    def handle_switch(self):
        query_params = urlparse(self.path).query
        params = parse_qs(query_params)

        if "value" in params:
            new_value_str = params["value"][0] # parse_qs returns lists
            new_value = None
            if new_value_str.lower() == "true":
                new_value = True
            elif new_value_str.lower() == "false":
                new_value = False

            if new_value is not None:
                self.truth_data["switch_conv_a_to_b"] = new_value
                if save_truth_data(self.truth_data):
                    response_dict = {
                        "ok": True,
                        "switch_conv_a_to_b": new_value
                    }
                    response_data = json.dumps(response_dict).encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.send_header("Content-Length", str(len(response_data)))
                    self.end_headers()
                    self.wfile.write(response_data)
                    return
                else:
                    self.send_error(500, "Failed to persist switch state.")
                    return
            else:
                self.send_error(400, "Invalid value for 'value' parameter. Must be 'true' or 'false'.")
                return
        self.send_error(400, "Missing or invalid 'value' parameter for switch. Expected format: /switch?value=true|false")

    def handle_health(self):
        response_data = json.dumps({"ok": True}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Content-Length", str(len(response_data)))
        self.end_headers()
        self.wfile.write(response_data)

# --- Server Startup ---
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass)
        self.shutdown_event = threading.Event()

    def process_request(self, request, client_address):
        """Override to handle potential exceptions during request processing."""
        try:
            super().process_request(request, client_address)
        except Exception as e:
            print(f"Error processing request from {client_address}: {e}", file=sys.stderr)

    def serve_forever(self, poll_interval=0.5):
        """Handle requests indefinitely. Use shutdown_event to stop."""
        self.shutdown_event.clear()
        while not self.shutdown_event.is_set():
            try:
                self.handle_request()
            except Exception as e:
                print(f"Exception in serve_forever loop: {e}", file=sys.stderr)
                if self.shutdown_event.is_set():
                    break
                time.sleep(poll_interval)

    def shutdown(self):
        """Set the shutdown event and call the parent shutdown."""
        self.shutdown_event.set()
        super().shutdown() # This should unblock the serve_forever loop

def start_server(host=HOST, port=PORT):
    """Starts the fixture server and returns the server instance and thread."""
    print(f"Attempting to start server on {host}:{port}...")
    try:
        initial_data = load_truth_data()
        if not get_truth_file_path().exists():
            if not save_truth_data(initial_data):
                print(f"FATAL: Could not create initial {TRUTH_FILE}.")
                sys.exit(1)

        server_address = (host, port)
        httpd = ThreadedTCPServer(server_address, FixtureHandler)

        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print(f"Server successfully started on {host}:{port}")
        return httpd, server_thread
    except OSError as e:
        if e.errno == 98: # Address already in use
            print(f"FATAL: port {port} is occupied. STEP 1 requires {port}. Do not auto-select another port.")
            sys.exit(1)
        else:
            print(f"Error starting server on {host}:{port}: {e}")
            sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during server startup: {e}")
        sys.exit(1)

# --- Self-Test ---
def run_self_test():
    print("Running self-test...")
    truth_path = get_truth_file_path()
    if truth_path.exists():
        try:
            truth_path.unlink()
            print(f"Removed existing {TRUTH_FILE}")
        except Exception as e:
            print(f"Error removing {TRUTH_FILE} before test: {e}", file=sys.stderr)
            return f"FAIL — Error removing {TRUTH_FILE} before test: {e}", 1

    server_address = (HOST, PORT)
    httpd = None
    server_thread = None
    test_results = []
    exit_code = 0

    try:
        print(f"Attempting to start test server on {HOST}:{PORT}...")
        httpd = ThreadedTCPServer(server_address, FixtureHandler)
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print("Test server thread started.")
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

    time.sleep(3) # Increased sleep for better reliability

    try:
        # Step 3: Check /health, /conv_a, /conv_b (JSON and HTML)
        print("Test 3: Checking /health, /conv_a, /conv_b (JSON and HTML)...")
        try:
            health_url = f"{FIXTURE_HEALTH_URL}"
            req = Request(health_url, headers={'Accept': 'application/json'})
            with urlopen(req, timeout=5) as resp:
                health_data = json.loads(resp.read().decode())
                if health_data.get("ok") != True:
                    test_results.append(f"GET /health did not return {{'ok': true}}. Got: {health_data}")
                    exit_code = 1
        except Exception as e:
            test_results.append(f"Error checking /health: {e}")
            exit_code = 1

        # Check JSON responses first (default behavior)
        conv_a_json_data = None
        try:
            conv_a_url_json = f"http://{HOST}:{PORT}/conv_a"
            req_a_json = Request(conv_a_url_json, headers={'Accept': 'application/json'})
            with urlopen(req_a_json, timeout=5) as resp_a_json:
                conv_a_json_data = json.loads(resp_a_json.read().decode())
                if conv_a_json_data.get("conv_id") != CONV_A_ID or len(conv_a_json_data.get("messages", [])) != 4:
                    test_results.append(f"GET /conv_a (JSON) did not return correct conv_id or message count. Expected '{CONV_A_ID}' and 4 messages. Got: {conv_a_json_data.get('conv_id')}, {len(conv_a_json_data.get('messages', []))} messages.")
                    exit_code = 1
        except Exception as e:
            test_results.append(f"Error checking /conv_a (JSON): {e}")
            exit_code = 1

        conv_b_json_data = None
        try:
            conv_b_url_json = f"http://{HOST}:{PORT}/conv_b"
            req_b_json = Request(conv_b_url_json, headers={'Accept': 'application/json'})
            with urlopen(req_b_json, timeout=5) as resp_b_json:
                conv_b_json_data = json.loads(resp_b_json.read().decode())
                if conv_b_json_data.get("conv_id") != CONV_B_ID or len(conv_b_json_data.get("messages", [])) != 4:
                    test_results.append(f"GET /conv_b (JSON) did not return correct conv_id or message count. Expected '{CONV_B_ID}' and 4 messages. Got: {conv_b_json_data.get('conv_id')}, {len(conv_b_json_data.get('messages', []))} messages.")
                    exit_code = 1
        except Exception as e:
            test_results.append(f"Error checking /conv_b (JSON): {e}")
            exit_code = 1

        # Check HTML responses
        try:
            conv_a_html_url = f"http://{HOST}:{PORT}/conv_a?format=html"
            req_a_html = Request(conv_a_html_url, headers={'Accept': 'text/html'})
            with urlopen(req_a_html, timeout=5) as resp_a_html:
                if 'text/html' not in resp_a_html.getheader('Content-Type'):
                    test_results.append(f"GET {conv_a_html_url} did not return text/html. Got: {resp_a_html.getheader('Content-Type')}")
                    exit_code = 1
                # Check for expected HTML content marker
                html_data_a = resp_a_html.read()
                if b'<div class="conv-header">conv_a</div>' not in html_data_a:
                     test_results.append(f"GET {conv_a_html_url} (HTML) missing expected header for conv_a.")
                     exit_code = 1
        except Exception as e:
            test_results.append(f"Error checking /conv_a (HTML): {e}")
            exit_code = 1

        try:
            conv_b_html_url = f"http://{HOST}:{PORT}/conv_b?format=html"
            req_b_html = Request(conv_b_html_url, headers={'Accept': 'text/html'})
            with urlopen(req_b_html, timeout=5) as resp_b_html:
                if 'text/html' not in resp_b_html.getheader('Content-Type'):
                    test_results.append(f"GET {conv_b_html_url} did not return text/html. Got: {resp_b_html.getheader('Content-Type')}")
                    exit_code = 1
                if b'<div class="conv-header">conv_b</div>' not in resp_b_html.read():
                    test_results.append(f"GET {conv_b_html_url} (HTML) missing expected header for conv_b.")
                    exit_code = 1
        except Exception as e:
            test_results.append(f"Error checking /conv_b (HTML): {e}")
            exit_code = 1

        # Step 4: Read truth.json and check content
        print(f"Test 4: Checking {TRUTH_FILE} content...")
        try:
            truth_content = load_truth_data()
            if truth_content.get("switch_conv_a_to_b") != False:
                test_results.append(f"Initial {TRUTH_FILE} has incorrect 'switch_conv_a_to_b'. Expected false, got {truth_content.get('switch_conv_a_to_b')}")
                exit_code = 1
            if CONV_A_ID not in truth_content.get("conversations", {}) or len(truth_content["conversations"].get(CONV_A_ID, {}).get("messages", [])) != 4:
                 test_results.append(f"Initial {TRUTH_FILE} has incorrect conv_a messages. Expected 4, got {len(truth_content['conversations'].get(CONV_A_ID, {}).get('messages', []))}")
                 exit_code = 1
            if CONV_B_ID not in truth_content.get("conversations", {}) or len(truth_content["conversations"].get(CONV_B_ID, {}).get("messages", [])) != 4:
                 test_results.append(f"Initial {TRUTH_FILE} has incorrect conv_b messages. Expected 4, got {len(truth_content['conversations'].get(CONV_B_ID, {}).get('messages', []))}")
                 exit_code = 1

        except FileNotFoundError:
            test_results.append(f"{TRUTH_FILE} not found after server start.")
            exit_code = 1
        except Exception as e:
            test_results.append(f"Error reading or validating {TRUTH_FILE}: {e}")
            exit_code = 1

        # Step 5: Execute GET /switch?value=true
        print("Test 5: Switching conv_a to conv_b...")
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
        print("Test 6 & 7: Verifying persistence and /conv_a switch...")
        try:
            truth_content_after_switch = load_truth_data()
            if truth_content_after_switch.get("switch_conv_a_to_b") != True:
                test_results.append(f"{TRUTH_FILE} not updated correctly after switch. Expected 'switch_conv_a_to_b': true, got {truth_content_after_switch.get('switch_conv_a_to_b')}")
                exit_code = 1

            req_a_after_switch = Request(f"http://{HOST}:{PORT}/conv_a?format=html", headers={'Accept': 'text/html'}) # Request HTML
            with urlopen(req_a_after_switch, timeout=5) as resp_a_after_switch:
                if 'text/html' not in resp_a_after_switch.getheader('Content-Type'):
                    test_results.append(f"GET /conv_a?format=html after switch did not return text/html. Got: {resp_a_after_switch.getheader('Content-Type')}")
                    exit_code = 1
                # Check if the HTML response for conv_a now reflects conv_b's ID or content
                if b'<div class="conv-header">conv_b</div>' not in resp_a_after_switch.read():
                     test_results.append(f"GET /conv_a?format=html after switch missing expected header for conv_b.")
                     exit_code = 1

        except FileNotFoundError:
            test_results.append(f"{TRUTH_FILE} not found after switch test.")
            exit_code = 1
        except Exception as e:
            test_results.append(f"Error after switch test: {e}")
            exit_code = 1

        # Step 8 & 10: Execute GET /switch?value=false and check /conv_a again
        print("Test 8 & 10: Switching back and verifying...")
        try:
            switch_url_false = f"http://{HOST}:{PORT}/switch?value=false"
            req_switch_false = Request(switch_url_false, headers={'Accept': 'application/json'})
            with urlopen(req_switch_false, timeout=5) as resp_switch_false:
                switch_data_false = json.loads(resp_switch_false.read().decode())
                if switch_data_false.get("ok") != True or switch_data_false.get("switch_conv_a_to_b") != False:
                    test_results.append(f"GET /switch?value=false did not return expected response. Got: {switch_data_false}")
                    exit_code = 1

            req_a_after_reset = Request(f"http://{HOST}:{PORT}/conv_a?format=html", headers={'Accept': 'text/html'}) # Request HTML
            with urlopen(req_a_after_reset, timeout=5) as resp_a_after_reset:
                 if 'text/html' not in resp_a_after_reset.getheader('Content-Type'):
                    test_results.append(f"GET /conv_a after reset did not return text/html. Got: {resp_a_after_reset.getheader('Content-Type')}")
                    exit_code = 1
                 if b'<div class="conv-header">conv_a</div>' not in resp_a_after_reset.read():
                     test_results.append(f"GET /conv_a after reset missing expected header for conv_a.")
                     exit_code = 1

        except Exception as e:
            test_results.append(f"Error during GET /switch?value=false: {e}")
            exit_code = 1

        # Step 11: Check forbidden endpoints
        print("Test 11: Checking forbidden endpoints...")
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
        print("Stopping test server...")
        if httpd:
            httpd.shutdown()
        if server_thread and server_thread.is_alive():
            server_thread.join(timeout=5)
            if server_thread.is_alive():
                print("Server thread did not shut down cleanly.")

    if not test_results:
        final_output = "SELF-TEST: PASS"
        print(final_output)
    else:
        final_output = f"SELF-TEST: FAIL — {'; '.join(test_results)}"
        print(final_output, file=sys.stderr)

    return final_output, exit_code

# --- Main Execution ---
if __name__ == "__main__":
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
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received. Shutting down server...")
            httpd.shutdown()
            if server_thread.is_alive():
                server_thread.join(timeout=5)
            print("Server shut down.")
        except Exception as e:
            print(f"An error occurred in the main loop: {e}")
            httpd.shutdown()
            if server_thread.is_alive():
                server_thread.join(timeout=5)
