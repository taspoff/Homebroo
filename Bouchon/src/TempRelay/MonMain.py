#!/usr/bin/python3
'''
Created on 4 janv. 2016

@author: YFGI7251
'''
from http.server import HTTPServer, CGIHTTPRequestHandler


if __name__ == '__main__':
    PORT = 8890
    server_address = ("", PORT)
    server = HTTPServer
    handler = CGIHTTPRequestHandler
    handler.cgi_directories = ["/"]
    print("Serveur actif sur le port :",PORT)
    
    httpd = server(server_address , handler)
    httpd.serve_forever()
    
    