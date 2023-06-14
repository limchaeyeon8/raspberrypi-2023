# Push Button 예제

import RPi.GPIO as GPIO
import time

btn = 24
count = 0

red = 17
green = 22
blue = 27

def clickHandler(channel):
    global count
    count = count + 1
    if (count % 2 == 0):
        GPIO.output(red, GPIO.LOW)
    else:
        GPIO.output(red, GPIO.HIGH)
    
    print(count)

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.add_event_detect(btn, GPIO.RISING, callback=clickHandler)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red, True)
GPIO.output(green, True)
GPIO.output(blue, True)

while (True):
    time.sleep(1)


# try:
#     while True:

#         GPIO.output(red, False)
#         GPIO.output(green, False)
#         GPIO.output(blue, False)
#         time.sleep(0.5)
#         GPIO.output(red, True)
#         GPIO.output(green, True)
#         GPIO.output(blue, True)
#         time.sleep(0.1)

#         GPIO.output(red, False)
#         time.sleep(0.5)
#         GPIO.output(red, True)
#         time.sleep(0.1)

#         GPIO.output(red, False)
#         GPIO.output(green, False)
#         time.sleep(0.5)
#         GPIO.output(red, True)
#         GPIO.output(green, True)
#         time.sleep(0.1)

#         GPIO.output(green, False)
#         time.sleep(0.5)
#         GPIO.output(green, True)
#         time.sleep(0.1)

#         GPIO.output(green, False)
#         GPIO.output(blue, False)
#         time.sleep(0.5)
#         GPIO.output(green, True)
#         GPIO.output(blue, True)
#         time.sleep(0.1)

#         GPIO.output(blue, False)
#         time.sleep(0.5)
#         GPIO.output(blue, True)
#         time.sleep(0.1)

#         GPIO.output(blue, False)
#         GPIO.output(red, False)
#         time.sleep(0.5)
#         GPIO.output(red, True)
#         GPIO.output(blue, True)
#         time.sleep(0.1)


# except KeyboardInterrupt:
#     GPIO.cleanup()