import RPi.GPIO as gpio
import time
import math

class SoundController:

    def __init__(self):
        # Set up Audio pins
        gpio.setup(12, gpio.OUT)
        self.audioPin = gpio.PWM(12, 1000) # (pin number, frequency)

    def __del__(self):
        # Clean up
        self.audioPin.stop()
        gpio.cleanup()

    # Play single tone and then wait for specified durations, defaults to .5 each. Meant to be called in a loop by code importing this class
    def playTone(self, tone_duration = 0.5, pause_duration = 0.5):
        tone = 800
        self.audioPin.ChangeFrequency(tone)
        time.sleep(tone_duration)
        self.audioPin.stop()
        time.sleep(pause_duration)

        #for i in range(1000):
            #tone = 500 + i + (100 * math.sin(i))
            #self.audioPin.ChangeFrequency(tone)
            #time.sleep(0.001)

    # Play default tone for a specified number of reps
    def playAlarm(self, reps):
        for i in range(reps):
            self.playTone()