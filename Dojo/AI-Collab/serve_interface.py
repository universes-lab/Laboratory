#!/usr/bin/env python3
"""Local HTTP server for AI-Collab templates + static files.

Routes:
  GET /              -> templates/index.html
  GET /chat.js       -> static/chat.js
  GET /seats_test.js -> static/seats_test.js
  GET /A.png         -> templates/A.png
  GET /B.png         -> templates/B.png
  GET /C.png         -> templates/C.png
  GET /D.png         -> templates/D.png
  Everything else    -> 404
"""
import http.server
import socketserver
import os
import sys

HOST = "127.0.0.1"
PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))

ROUTES = {
    "/":              ("templates/index.html", "text/html; charset=utf-8"),
    "/chat.js":       ("static/chat.js",       "application/javascript; charset=utf-8"),
    "/seats_test.js": ("static/seats_test.js", "application/javascript; charset=utf-8"),
    "/A.png":         ("templates/A.png",      "image/png"),
    "/B.png":         ("templates/B.png",      "image/png"),
    "/C.png":         ("templates/C.png",      "image/png"),
    "/D.png":         ("templates/D.png",      "image/png"),
}


class Handler(http.server.BaseHTTPRequestHandler):
    server_version = "AI-Collab-Interface/1.0"
    sys_version = ""

    def __init__(self, *args, **kwargs):
        # SimpleHTTPRequestHandler serves from current directory by default.
        # Removing explicit directory argument to rely on default behavior.
        super().__init__(*args, **kwargs)

    def do_GET(self):
        path = selfI.path.split("?", 1)[0] # Ignore query parameters for routing

        if path not in ROUTES:
            self.send_error(404, "Not Found")
            return

        rel_path, ctype = ROUTES[path]
        full_path = os.path.join(ROOT, rel_path)

        if not os.path.isfile(full_path):
            self.send_error(404, f"File not found: {rel_path}")
            return

        try:
            with open(full_path, "rb") as f:
                data = f.read()
        except Exception as e:
            self.send_error(500, f"Read error: {e}")
            return

        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        sys.stderr.write("[serve_interface] " + (fmt % args) + "\n")


class TCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def run():
    try:
        server_address = (HOST, PORT)
        httpd = TCPServer(server_address, Handler)
    except OSError as e:
        if e.errno == 98: # Address already in use
            print(f"FATAL: cannot bind {HOST}:{PORT} — Port {PORT} is already in use.", file=sys.stderr)
        else:
            print(f"FATAL: cannot bind {HOST}:{PORT} — {e}", file=sys.stderr)
        print("Port 8000 is required. Do not auto-select another port.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"FATAL: Unexpected error starting server: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"serve_interface listening on http://{HOST}:{PORT}/", file=sys.stderr)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nshutting down", file=sys.stderr)
        httpd.shutdown()
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run()
