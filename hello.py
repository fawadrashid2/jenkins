from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

if __name__ == "__main__":
    server = HTTPServer(("", 89), HelloHandler)
    print("Serving on port 89")
    server.serve_forever()
