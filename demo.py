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

def display_green():
    red_light.disable()
    yellow_light.disable()
    green_light.enable()

def display_yellow():
    red_light.disable()
    yellow_light.enable()
    green_light.disable()
    
def display_red():
    red_light.enable()
    yellow_light.disable()
    green_light.disable()

def display_none():
    red_light.disable()
    yellow_light.disable()
    green_light.disable()

def display_all():
    red_light.enable()
    yellow_light.enable()
    green_light.enable()

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
#audioPin.start(50) # set duty cycle

#######################################
while(1):
    command = raw_input("command: ")
    if command == "g":
        display_green()
    elif command == 'y':
        display_yellow()
    elif command == 'r':
        display_red()
    elif command == 'a':
        display_all()
    elif command == 'n':
        display_none()

#cleanup
audioPin.stop()
gpio.cleanup()

