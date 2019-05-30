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

class LEDController:

    def __init__(self):
        #setup
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

        # Set up LED pins
        self.red_light = Light(RED)
        self.yellow_light = Light(YELLOW)
        self.green_light = Light(GREEN)

        # Set up Audio pin
        gpio.setup(12, gpio.OUT)
        self.audioPin = gpio.PWM(12, 1000) # (pin #, frequency)
        self.audioPin.start(50)

    def __del__(self):
        #cleanup
        self.audioPin.stop()
        gpio.cleanup()

    # Display yellow, red, and flashing red lights as alarm time approaches
    def alarmSequence(self, yellow_duration, red_duration, flash_duration):
        # Display warning light 1 hour before alarm
        self.display_yellow()

        # Display yellow warn
        time.sleep(yellow_duration)

        # Display red warn
        self.display_red()

        # Include flash duration in red light duration
        time.sleep(red_duration - flash_duration)

        # Flash red warn light
        self.flash_red(flash_duration)


    def playAlarm(self, reps):
        for i in range(reps):
            self.green_light.enable()
            for j in range(1000):
                tone = 500 + j + (100 * math.sin(j))
                self.audioPin.ChangeFrequency(tone)
                time.sleep(0.001)

                if j == 900:
                    self.green_light.disable()

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
            time.sleep(1)
            self.red_light.disable()
            time.sleep(1)