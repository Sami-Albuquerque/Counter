import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PORT = 8000

class CustomRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        file_path = self.path.strip('/')

        if file_path == "":
            file_path = "index.html"

        if os.path.exists(file_path):
            content_type = self.get_content_type(file_path)

            with open(file_path, 'rb') as file:
                file_content = file.read()

            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()

            self.wfile.write(file_content)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>404 Not Found</h1></body></html>')

    def get_content_type(self, file_path):
        if file_path.endswith('.html'):
            return 'text/html'
        elif file_path.endswith('.css'):
            return 'text/css'
        elif file_path.endswith('.js'):
            return 'application/javascript'
        elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
            return 'image/jpeg'
        elif file_path.endswith('.png'):
            return 'image/png'
        elif file_path.endswith('.gif'):
            return 'image/gif'
        else:
            return 'application/octet-stream'

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        print(f"Received POST data: {post_data.decode('utf-8')}")

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        response_message = f"Received POST data: {post_data.decode('utf-8')}"
        self.wfile.write(response_message.encode('utf-8'))

httpd = socketserver.TCPServer(('', PORT), CustomRequestHandler)
print(f'Starting HTTP server on port {PORT}...')
httpd.serve_forever()
