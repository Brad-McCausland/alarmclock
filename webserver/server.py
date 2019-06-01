import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
#TODO: INTERRUPT ALARM SEQUENCE HERE
print("serving at port", PORT)
httpd.serve_forever()
