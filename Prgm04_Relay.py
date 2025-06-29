# @Auth Xtrans Solutions Pvt. Ltd.
# Program to test relay
# Connect RM9 to RM17

import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(36, gpio.OUT)

try:
    while(1):
        gpio.output(36,0)
        print("Relay OFF")
        time.sleep(1)
        gpio.output(36,1)
        print("Relay ON")
        time.sleep(1)
        #gpio.cleanup()
except KeyboardInterrupt:
        gpio.cleanup()
        exit
