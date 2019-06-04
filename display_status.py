# A simple script that indicates the status of TACO_server on the Pi LEDs. Green for online, flashing yellow for not.
# To be called by crontab every 5 minutes

import subprocess, os, LEDController

controller = LEDController.LEDController()

p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
out, err = p.communicate()

server_online = False
driver_online = False

for line in out.splitlines():
    if b"TACO_server" in line:
        server_online = True
    elif b"TACO_driver" in line:
        driver_online = True

if server_online:
    # Only change lights if driver is not currently running
    if not driver_online:
        controller.display_green()
else:
    controller.flash_yellow(60 * 5)