import os
import threading
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 10000))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        return

def run_web():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"HTTP server running on 0.0.0.0:{PORT}")
    server.serve_forever()

def run_bot():
    subprocess.run(["python3", "modules/main.py"])

if __name__ == "__main__":
    t = threading.Thread(target=run_web, daemon=True)
    t.start()
    run_bot()
