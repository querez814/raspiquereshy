#!/usr/bin/env python3
from picamera2 import Picamera2, Preview
from gpiozero import MotionSensor
import time
import os

user = os.getlogin()
user_home = os.path.expanduser(f'~{user}')

camera = Picamera2()
camera.start()

pir = MotionSensor(17)

try:
    i = 1
    while True:
        if pir.motion_detected:
            camera.capture_file(f'{user_home}/capture%s.jpg' % i)
            print('The number is %s' % i)
            time.sleep(3)
            i += 1
        else:
            print('waiting')
            time.sleep(0.5)

except KeyboardInterrupt:
    camera.stop_preview()
    pass
