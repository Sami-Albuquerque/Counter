import socketserver
from src.request_handler import RequestHandler

PORT = 8000

httpd = socketserver.TCPServer(('', PORT), RequestHandler)
print(f'Starting HTTP server on port {PORT}...')
httpd.serve_forever()
