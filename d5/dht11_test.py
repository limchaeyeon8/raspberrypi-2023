# 온습도 센서 DHT11

import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time

sensor = dht.DHT11      # 초저가센서
rcv_p = 10              # 온습도 센서 값 받아오는 핀

btn = 24
count = 0

red = 17
green = 22
blue = 27

try:
    while True:
        humid, temp = dht.read_retry(sensor, rcv_p)
        if humid is not None and temp is not None:
            print(f'온도 : {temp}℃ | 습도 : {humid}%')
        else:
            print('※센싱에러※')

        time.sleep(0.5)
except Exception as ex:
    print(ex)
finally:
    print('프로그램 종료')
