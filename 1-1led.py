import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.IN)


GPIO.output(16, GPIO.input(26))