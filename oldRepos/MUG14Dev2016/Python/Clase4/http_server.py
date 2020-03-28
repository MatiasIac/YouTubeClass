
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler
from http_factory import http_factory

class http_server(BaseHTTPRequestHandler):
    """Clase que maneja el server"""

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def _get_parsed_path(self, path):
        result_path = path[1:]
        splitted = result_path.split("/")
        return splitted

    def _default_not_found(self):
        return '{ "err": "Not found"}'

    def do_GET(self):
        final_path = self._get_parsed_path(self.path) #["users","1"]

        result_data = http_factory().function_pointers.get(
            'get_' + final_path[0], self._default_not_found
        )(final_path)

        self._set_headers()
        self.wfile.write(result_data)

    def do_POST(self):
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        final_path = self._get_parsed_path(self.path)

        http_factory().function_pointers.get(
            'post_' + final_path[0], self._default_not_found
        )(data_string)

        self._set_headers()

    #def do_DELETE(self):

def start_server():
    """Iniciador del server"""
    http_server_instance = SocketServer.TCPServer(('', 9002), http_server)
    http_server_instance.serve_forever()

if __name__ == "__main__":
    start_server()
