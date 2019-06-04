import RPi.GPIO as gpio
import time
import random
import math
from Light import Light

RED = 21
YELLOW = 20
GREEN = 16

class LEDController:

    def __init__(self):
        #setup
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

        # Set up LED pins
        self.red_light = Light(RED)
        self.yellow_light = Light(YELLOW)
        self.green_light = Light(GREEN)

    def __del__(self):
        #cleanup
        gpio.cleanup()

    def display_green(self):
        self.red_light.disable()
        self.yellow_light.disable()
        self.green_light.enable()

    def display_yellow(self):
        self.red_light.disable()
        self.yellow_light.enable()
        self.green_light.disable()
        
    def display_red(self):
        self.red_light.enable()
        self.yellow_light.disable()
        self.green_light.disable()

    def display_none(self):
        self.red_light.disable()
        self.yellow_light.disable()
        self.green_light.disable()

    def display_all(self):
        self.red_light.enable()
        self.yellow_light.enable()
        self.green_light.enable()

    # flash the read light for 'duration' seconds. Note this is a blocking operation.
    def flash_red(self, duration):
        self.green_light.disable()
        self.yellow_light.disable()
        for i in range (duration/2):
            self.red_light.enable()
            time.sleep(0.5)
            self.red_light.disable()
            time.sleep(0.5)

    def flash_yellow(self, duration):
        self.green_light.disable()
        self.red_light.disable()
        for i in range (duration):
            self.yellow_light.enable()
            time.sleep(0.5)
            self.yellow_light.disable()
            time.sleep(0.5)