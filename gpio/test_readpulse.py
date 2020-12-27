import RPi.GPIO as GPIO
import sqlite3
import datetime
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def click23handler(channel):
    print("Click!")

GPIO.add_event_detect(23, GPIO.RISING, callback = click23handler, bouncetime = 100)   
