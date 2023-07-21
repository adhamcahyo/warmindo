from http.server import HTTPServer, SimpleHTTPRequestHandler

def main():
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server berjalan di http://localhost:{port}")
    httpd.serve_forever()