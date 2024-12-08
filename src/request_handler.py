
import os
import json
from http.server import BaseHTTPRequestHandler
from src.check_counter import CheckCounter

class RequestHandler(BaseHTTPRequestHandler):

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
        post_data = self.rfile.read(content_length).decode('utf-8')
        number = json.loads(post_data)['number']

        if self.__is_number(number):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            response_message = f"Esse número foi enviado: {CheckCounter().call(number)} vezes."
            self.wfile.write(json.dumps({"message": response_message}).encode('utf-8'))
        else:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            self.wfile.write(json.dumps({"error": "Não é um número válido"}).encode('utf-8'))

    def __is_number(self, value):
        try:
            float(value)  # Testa converter para float
            return True
        except ValueError:
            return False
