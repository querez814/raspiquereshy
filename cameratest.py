#!/usr/bin/env python3

from picamera2 import Picamera2
from gpiozero import LED, Button
from pathlib import Path
import time

user_home = Path.home()

LED_PIN = 17
BTN_PIN = 18

status = False

camera = Picamera2()
camera.configure(camera.create_still_configuration())


def take_photos():
    global status
    status = True


def setup():
    global led, button

    led = LED(LED_PIN)
    button = Button(BTN_PIN, pull_up=True, bounce_time=0.2)

    button.when_pressed = take_photos

    camera.start()


def main():
    global status

    try:
        while True:
            if status:
                for _ in range(5):
                    led.off()
                    time.sleep(0.1)
                    led.on()
                    time.sleep(0.1)

                filename = user_home / "my_photo.jpg"
                camera.capture_file(str(filename))
                print(f"Take a photo! Saved to {filename}")

                status = False
            else:
                led.on()

            time.sleep(0.1)
    except KeyboardInterrupt:
        destroy()


def destroy():
    camera.stop()
    led.on()
    led.close()
    button.close()


if __name__ == "__main__":
    setup()
    main()

