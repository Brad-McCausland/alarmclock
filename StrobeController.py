import RPi.GPIO as gpio

class StrobeController:
    pinNumber = 6

    def __init__(self):
        #setup
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

        gpio.setup(self.pinNumber, gpio.OUT)

    def __del__(self):
        self.disable_strobe()
        gpio.cleanup()

    def enable_strobe(self):
        gpio.output(self.pinNumber, gpio.HIGH)

    def disable_strobe(self):
        gpio.output(self.pinNumber, gpio.LOW)