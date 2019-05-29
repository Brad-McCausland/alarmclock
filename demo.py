import RPi.GPIO as gpio
import time
import random
import math

RED = 21
YELLOW = 20
GREEN = 16

class Light:
    pinNumber = -1

    def __init__(self, pinNum):
        self.pinNumber = pinNum
        gpio.setup(self.pinNumber, gpio.OUT)

    def enable(self):
        gpio.output(self.pinNumber, gpio.HIGH)

    def disable(self):
        gpio.output(self.pinNumber, gpio.LOW)


def playAlarm(reps):
    for i in range(reps):
        green_light.enable()
        for j in range(1000):
            tone = 500 + j + (100 * math.sin(j))
            audioPin.ChangeFrequency(tone)
            time.sleep(0.001)

            if j == 900:
                green_light.disable()

#setup
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# Set up LED pins
red_light = Light(RED)
yellow_light = Light(YELLOW)
green_light = Light(GREEN)

# Set up Audio pin
gpio.setup(12, gpio.OUT)
audioPin = gpio.PWM(12, 1000) # (pin #, frequency)
audioPin.start(50) # set duty cycle

###################################
playAlarm(3)
###################################

#cleanup
audioPin.stop()
gpio.cleanup()

