# open_seats.py
import json
import sys
import os
import subprocess
import pathlib
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

# --- Configuration ---
FIXTURE_HEALTH_URL = "http://127.0.0.1:5999/health"
EDGE_EXECUTABLE_PATHS = [
    "msedge", # Try 'msedge' command first (in PATH)
    "microsoft-edge", # Alias for msedge
    r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    r"C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
]
PROFILE_BASE_DIR = pathlib.Path("E:\\Gemini\\Dojo\\AI-Collab\\profiles")
OPEN_SEATS_JSON = "open_seats.json"

# --- Helper Functions ---
def check_fixture_server():
    """Checks if the fixture server is running and responsive."""
    print("Step 1: Checking fixture server health...")
    try:
        req = Request(FIXTURE_HEALTH_URL, headers={'Accept': 'application/json'})
        with urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            if data.get("ok") == True:
                print("Fixture server is running.")
                return True
            else:
                print(f"FATAL: fixture not running on 127.0.0.1:5999. Unexpected health response: {data}", file=sys.stderr)
                return False
    except URLError as e:
        print(f"FATAL: fixture not running on 127.0.0.1:5999. Error connecting: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"FATAL: fixture not running on 127.0.0.1:5999. Unexpected error: {e}", file=sys.stderr)
        return False

def find_edge_executable():
    """Finds the Microsoft Edge executable path."""
    print("Step 2: Checking for Microsoft Edge executable...")
    for path_candidate in EDGE_EXECUTABLE_PATHS:
        try:
            if path_candidate.startswith("msedge") or path_candidate.startswith("microsoft-edge"):
                # Try to find the command in PATH using 'where' if it's a command name
                try:
                    # Check if the command exists and can be run with --version
                    # Use shell=True to resolve PATH entries correctly
                    result = subprocess.run([path_candidate, "--version"], capture_output=True, text=True, check=False, shell=True)
                    if result.returncode == 0:
                        # If found, now resolve its absolute path using 'where'
                        try:
                            where_result = subprocess.run(["where", path_candidate], capture_output=True, text=True, check=True, shell=True)
                            # 'where' output can have multiple lines, take the first one
                            absolute_path = where_result.stdout.strip().splitlines()[0]
                            print(f"Microsoft Edge found at: {absolute_path}")
                            return absolute_path
                        except Exception as e:
                            print(f"Warning: Found '{path_candidate}' in PATH but failed to resolve absolute path: {e}. Falling back to command name '{path_candidate}'.", file=sys.stderr)
                            return path_candidate # Fallback to command name
                    # Handle cases like 'msedge' not being in PATH where returncode might be non-zero or 127
                    elif result.returncode != 127: # 127 is often "command not found", other errors are more concerning
                        print(f"Warning: Command '{path_candidate}' returned non-zero exit code {result.returncode} when checking version. Trying next path.", file=sys.stderr)

                except FileNotFoundError: # If 'where' or the command itself is not found
                    pass # Try next path
                except Exception as e: # Catch other potential errors during command execution
                    print(f"Warning: Error during check for '{path_candidate}' via PATH: {e}. Trying next path.", file=sys.stderr)

            else: # It's an absolute path
                if os.path.exists(path_candidate):
                    # Verify it's executable by trying to run --version
                    result = subprocess.run([path_candidate, "--version"], capture_output=True, text=True, check=False)
                    if result.returncode == 0:
                        absolute_path = os.path.abspath(path_candidate)
                        print(f"Microsoft Edge found at: {absolute_path}")
                        return absolute_path
                    else:
                        print(f"Warning: File exists at '{path_candidate}' but --version check failed (exit code {result.returncode}). Trying next path.", file=sys.stderr)

        except Exception as e: # Catch any unexpected errors during path checking
            print(f"Warning: Unexpected error checking path '{path_candidate}': {e}. Trying next path.", file=sys.stderr)

    print("FATAL: Microsoft Edge not found. Please ensure it is installed and in your PATH, or check the hardcoded paths.", file=sys.stderr)
    return None

def create_profile_directories():
    """Creates the profile directories if they do not exist."""
    print("Step 3: Creating profile directories...")
    seat_dirs = [
        PROFILE_BASE_DIR / "seat-01",
        PROFILE_BASE_DIR / "seat-02"
    ]
    created_any = False
    for dir_path in seat_dirs:
        if not dir_path.exists():
            try:
                dir_path.mkdir(parents=True, exist_ok=True)
                print(f"Created directory: {dir_path}")
                created_any = True
            except Exception as e:
                print(f"Error creating directory {dir_path}: {e}", file=sys.stderr)
                # Decide if this is fatal. For now, continue.
    if created_any:
        print("Profile directories ensured.")
    else:
        print("Profile directories already exist.")

def launch_browser(edge_path, profile_dir, url):
    """Launches a Microsoft Edge browser process."""
    # Ensure edge_path is treated as a command or absolute path correctly
    command = [
        edge_path,
        f"--user-data-dir={profile_dir}",
        url
    ]
    try:
        # Use Popen to run in background, don't wait
        # If edge_path is a simple command like 'msedge', Popen should resolve it if it's in PATH
        process = subprocess.Popen(command)
        print(f"Launched Edge for {url} with profile {profile_dir}. PID: {process.pid}")
        return process.pid
    except FileNotFoundError:
        # This is more likely if edge_path is an absolute path that doesn't exist
        print(f"FATAL: Edge executable not found at {edge_path}. Cannot launch browser.", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error launching browser for {url} with command '{edge_path}': {e}", file=sys.stderr)
        return None

def main():
    # Step 1: Check fixture server
    if not check_fixture_server():
        sys.exit(1)

    # Step 2: Find Edge executable
    edge_path = find_edge_executable()
    if not edge_path:
        sys.exit(1)

    # Step 3: Create profile directories
    create_profile_directories()

    # Step 4: Launch browsers
    print("Step 4: Launching Microsoft Edge processes...")
    seat_configs = {
        "seat-01": {
            "url": "http://127.0.0.1:5999/conv_a",
            "profile_dir": PROFILE_BASE_DIR / "seat-01"
        },
        "seat-02": {
            "url": "http://127.0.0.1:5999/conv_b",
            "profile_dir": PROFILE_BASE_DIR / "seat-02"
        }
    }

    open_seats_data = {}
    pids = []

    for seat_id, config in seat_configs.items():
        # Pass the resolved edge_path to launch_browser
        pid = launch_browser(edge_path, config["profile_dir"], config["url"])
        if pid is None:
            print(f"FATAL: Failed to launch browser for {seat_id}. Exiting.", file=sys.stderr)
            # Attempt to clean up any started processes if one fails
            for started_pid in pids:
                try:
                    os.kill(started_pid, 9) # SIGKILL
                except OSError:
                    pass # Process might have already exited
            sys.exit(1)
        pids.append(pid)
        open_seats_data[seat_id] = {
            "pid": pid,
            "url": config["url"],
            "profile_dir": str(config["profile_dir"])
        }

    # Step 5: Write open_seats.json
    print(f"Step 5: Writing {OPEN_SEATS_JSON}...")
    try:
        output_path = pathlib.Path(OPEN_SEATS_JSON)
        with open(output_path, 'w') as f:
            json.dump(open_seats_data, f, indent=2)
        print(f"Successfully wrote {OPEN_SEATS_JSON}")
    except Exception as e:
        print(f"FATAL: Failed to write {OPEN_SEATS_JSON}: {e}", file=sys.stderr)
        # Attempt to clean up started processes
        for started_pid in pids:
            try:
                os.kill(started_pid, 9)
            except OSError:
                pass
        sys.exit(1)

    # Step 6: Print success message
    print("Step 6: Printing success message...")
    print("OPEN: PASS")
    sys.exit(0)

if __name__ == "__main__":
    main()
