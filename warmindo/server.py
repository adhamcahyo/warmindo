import click
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

def get_package_version():
    import os
    from setuptools.config import read_configuration
    config = read_configuration(os.path.join(os.path.dirname(__file__), 'setup.cfg'))
    return config['metadata']['version']

def redirect_to_home(handler):
    if handler.path == "/":
        handler.send_response(301)
        handler.send_header("Location", "/home.html")
        handler.end_headers()
        return True
    return False

class WarmindoRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if redirect_to_home(self):
            return
        super().do_GET()

@click.command()
@click.option('--version', '-v', is_flag=True, help='Display the Warmindo version.')
def main(version):
    if version:
        print(f'Warmindo version {get_package_version()}')
    else:
        port = 8000
        server_address = ('', port)
        httpd = HTTPServer(server_address, WarmindoRequestHandler) 
        print(f"Server berjalan di http://localhost:{port}")
        webbrowser.open_new_tab(f"http://localhost:{port}/home.html")  # Buka halaman index di browser saat server mulai
        httpd.serve_forever()

if __name__ == '__main__':
    main()
