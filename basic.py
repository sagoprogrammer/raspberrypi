import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while True:
        print("[] Truning ON LED...!")
        GPIO.output(17, GPIO.HIGH)
        sleep(1)
        print("[] Truning OFF LED...!")
        GIPO.output(17, GPIO.LOW)
        sleep(1)
