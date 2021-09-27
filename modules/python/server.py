from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import json
import os


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        post_data = self.rfile.read(int(self.headers['Content-Length']))
        commands = json.loads(post_data)
        for command in commands:
            process = subprocess.Popen(command, shell=True)
            process.wait()
        self.send_response(int(os.environ["SUCCESS"]))
        self.send_header('Content-type', 'text/html')
        self.end_headers()


os.chdir(os.environ["DIRECTORY"])
with HTTPServer(('', int(os.environ["PORT"])), Handler) as server:
    server.serve_forever()
