from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import setproctitle
import subprocess
import signal
import os
import LEDController

def kill_driver():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    for line in out.splitlines():
        if b"TACO_driver" in line:
            pid = int(line.split()[0])
            os.kill(pid, signal.SIGKILL)
            controller = LEDController.LEDController()
            controller.display_none()

class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        print("HEAD")
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

        httpFile = open("/home/pi/Documents/alarmclock/index.html", 'r')
        httpResponse = ""
        for line in httpFile:
            httpResponse = httpResponse + line + '\n'
        
        data = bytes(httpResponse, "utf-8")
        s.wfile.write(data)

        kill_driver()

setproctitle.setproctitle("TACO_webhost")

PORT = 8080
Handler = MyHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

#kill_driver()

print("serving at port", PORT)
httpd.serve_forever()

