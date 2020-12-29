#!/usr/bin/python
# simple HTTP(Web) Server using http.Server
# and socket.server modules

import http.server
import socketserver
from time import sleep

PORT = 8080 # Our server default port
Handler = http.server.SimpleHTTPRequestHandler

# HTTP Server code
try:
    with socketserver.TCPServer(("",PORT),Handler) as httpd:
         print("[+] HTTP server now running at port",PORT)
         httpd.serve_forever() # Initializes the server to accept connections
except KeyboardInterrupt:
  print("[-] Server Shutting Down by user exit...");sleep(5)
    