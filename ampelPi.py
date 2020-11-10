import RPi.GPIO as GPIO
import time
from os import system

# GPIO Slot Taste
taste = 24

# GPIO Slot Grün
gruen = 17

# GPIO Slot Gelb
gelb = 27

# GPIO Slot Rot
rot = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(taste, GPIO.IN)
GPIO.setup(gruen, GPIO.OUT)
GPIO.setup(gelb, GPIO.OUT)
GPIO.setup(rot, GPIO.OUT)

# Programschleife
while True:
    GPIO.output(gruen, GPIO.HIGH)
    GPIO.output(gelb, GPIO.LOW)
    GPIO.output(rot, GPIO.LOW)
    if GPIO.input(taste) == 1:
        system('clear')
        print("Button pressed, please wait for the signal")
        time.sleep(5)
        GPIO.output(gruen, GPIO.LOW)
        GPIO.output(gelb, GPIO.HIGH)
        GPIO.output(rot, GPIO.LOW)
        time.sleep(1)
        GPIO.output(gruen, GPIO.LOW)
        GPIO.output(gelb, GPIO.LOW)
        GPIO.output(rot, GPIO.HIGH)
        print("You may go now!")
        time.sleep(12)
        print("Please stop, cars will get a green signal soon!")
        time.sleep(3)
        GPIO.output(gruen, GPIO.LOW)
        GPIO.output(gelb, GPIO.HIGH)
        GPIO.output(rot, GPIO.HIGH)
        time.sleep(1)