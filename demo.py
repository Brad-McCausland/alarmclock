import RPi.GPIO as gpio
import time
import random

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(12, gpio.OUT)

#activate led
gpio.output(12, gpio.HIGH)
print "LEDs enabled"

#time.sleep(1)

#play sound
p = gpio.PWM(12, 50)
p.start(70)
for x in range(10000):
    tone = random.randint(200,2200)
    p.ChangeFrequency(tone)
    time.sleep(0.0001)
p.stop()

#deactivate led
gpio.output(12, gpio.LOW)
print "LEDs disabled"

gpio.cleanup()
