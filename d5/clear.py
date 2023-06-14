# CLEAR

import RPi.GPIO as GPIO

red = 17
green = 22
blue = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.cleanup()