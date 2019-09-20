import os
import cgi
import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from http.server import CGIHTTPRequestHandler
import cgitb
cgitb.enable() ## enable CGI error reporting

def web_server(port):
    server = HTTPServer
    handler = CGIHTTPRequestHandler # RequestsHandler
    server_address = ("", port)
    handler.cgi_directories = ["/cgi-bin",]
    httpd = server(server_address, handler)
    print("Starting web server with CGI support on port: %s ..." %port)
    httpd.serve_forever()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'CGI Server Example')
    parser.add_argument('--port', action='store', dest="port", type=int, required = True)
    given_args = parser.parse_args()
    web_server(given_args.port)
