#!/usr/bin/env python3
"""
Simple development server for testing the blog locally.
Usage: python serve.py
Then open http://localhost:8000 in your browser
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

PORT = 8000
URL = f"http://localhost:{PORT}"

def main():
    # Change to the root directory of the project
    root_dir = Path(__file__).parent
    os.chdir(root_dir)
    # Start the server
    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"\n🚀 Starting development server at {URL}")
        print("📝 Open this URL in your browser to view the blog")
        print("⌨️  Press Ctrl+C to stop the server\n")
        # Open the browser automatically
        webbrowser.open(URL)
        # Start serving
        httpd.serve_forever()

if __name__ == "__main__":
    main()