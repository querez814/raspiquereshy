import numpy as np
import cv2
from picamera2 import Picamera2
from gpiozero import LED
import time

LED_PIN = 17
led = LED(LED_PIN)

face_cascade = cv2.CascadeClassifier('/home/student8/assignment8/haarcascade_frontalface_default.xml')

picam2 = Picamera2()

config = picam2.create_video_configuration(
   main={"size": (640, 480)},
)
picam2.configure(config)

picam2.start()

print("Camera started. Waiting for faces. Press Ctrl+C to quit.")

try:
   while True:
      frame = picam2.capture_array()

      frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

      faces = face_cascade.detectMultiScale(gray, 1.3, 5)

      if len(faces) > 0:
         if not led.is_lit:
            led.on()
            print("Face detected. LED ON.")
      else:
         if led.is_lit:
            led.off()
            print("No face. LED OFF.")

except KeyboardInterrupt:
   print("Program interrupted by user. Cleaning up.")

finally:
   picam2.stop()
   print("Camera stopped.")
