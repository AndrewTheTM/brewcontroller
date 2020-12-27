import RPi.GPIO as GPIO
import sqlite3
import datetime
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

clicks = 0

def click23handler(channel):
    clicks += 1
    print(f"Click {clicks}", end = '\r')

GPIO.add_event_detect(23, GPIO.RISING, callback = click23handler, bouncetime = 100)

try:
    GPIO.wait_for_edge(24, GPIO.RISING)
except KeyboardInterrupt:
    GPIO.cleanup()
