import http.server
import socketserver
import webbrowser
import threading
import time
import sys

PORT = 8000
DIRECTORY = "."

class SafeHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Serve the current directory
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def launch_browser():
    # Wait a moment for the server socket to bind before opening browser
    time.sleep(1)
    url = f"http://localhost:{PORT}/index.html"
    print(f"Opening browser at {url}...")
    webbrowser.open(url)

def start_server():
    # TCPServer allows reusing addresses immediately after restart
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), SafeHandler) as httpd:
            print(f"\n==========================================")
            print(f"  MX Herbal Local Server Running")
            print(f"  Address: http://localhost:{PORT}")
            print(f"  Press Ctrl+C to terminate the server")
            print(f"==========================================\n")
            httpd.serve_forever()
    except Exception as e:
        print(f"Error starting server: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Start background browser opener
    threading.Thread(target=launch_browser, daemon=True).start()
    # Start web server synchronously
    start_server()
