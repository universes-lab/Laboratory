#!/usr/bin/env python3
"""Verify serve_interface + fixture routes. No curl."""
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse, parse_qs # Import for path parsing

# Updated CHECKS to reflect the actual content and routes
# The root check now expects '<title>AI-Colab Laboratory</title>' from index.html.
# Fixture routes now check for HTML content markers.
CHECKS = [
    ("http://127.0.0.1:8000/",              b"<title>AI-Colab Laboratory</title>"), # Updated expected marker for root, matching index.html title precisely.
    ("http://127.0.0.1:8000/chat.js",       b"DOMContentLoaded"),
    ("http://127.0.0.1:8000/seats_test.js", b"seatsTestBtn"),
    ("http://127.0.0.1:8000/A.png",         None), # Checking for presence, content not specified
    ("http://127.0.0.1:8000/B.png",         None), # Checking for presence, content not specified
    ("http://127.0.0.1:8000/C.png",         None), # Checking for presence, content not specified
    ("http://127.0.0.1:8000/D.png",         None), # Checking for presence, content not specified
    ("http://127.0.0.1:5999/conv_a?format=html", b'<div class="conv-header">conv_a</div>'), # Updated HTML marker
    ("http://127.0.0.1:5999/conv_b?format=html", b'<div class="conv-header">conv_b</div>'), # Updated HTML marker
]

def check(url, expect):
    try:
        req = urllib.request.Request(url, headers={'Accept': '*/*'}) # Generic accept header
        with urllib.request.urlopen(req, timeout=5) as r:
            data = r.read()
            status = r.status
        if status != 200:
            print(f"FAIL {url}: status {status}")
            return False
        if expect is not None and expect not in data:
            print(f"FAIL {url}: expected marker {expect!r} not found")
            return False
        print(f"OK   {url}: {len(data)} bytes")
        return True
    except urllib.error.HTTPError as e:
        print(f"FAIL {url}: HTTP {e.code}")
        return False
    except Exception as e:
        print(f"FAIL {url}: {type(e).__name__}: {e}")
        return False

def main():
    ok = True
    for url, expect in CHECKS:
        ok &= check(url, expect)
    print("VERIFY: PASS" if ok else "VERIFY: FAIL")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
