#!/usr/bin/python2.7
import time
import RPi.GPIO as GPIO

relay_ch = 26


while True: 
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(relay_ch, GPIO.OUT)
  GPIO.output(relay_ch, GPIO.LOW)
  time.sleep(1)
  GPIO.output(relay_ch, GPIO.HIGH)
  GPIO.cleanup()
  time.sleep(1)
