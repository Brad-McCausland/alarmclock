from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import setproctitle
import subprocess
import signal
import os
from LEDController import LEDController

def kill_driver():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    for line in out.splitlines():
        if b"TACO_driver" in line:
            pid = int(line.split()[0])
            os.kill(pid, signal.SIGKILL)
            controller = LEDController.LEDController()
            controller.display_green()

class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        print("HEAD")
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "image/jpg")
        s.end_headers()

        f = open("/home/pi/Documents/alarmclock/gowron.jpg", 'rb')

        s.wfile.write(f.read())

        kill_driver()

setproctitle.setproctitle("TACO_webhost")

PORT = 8080
Handler = MyHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

httpd.serve_forever()
