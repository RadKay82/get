import RPi.GPIO as GPIO
import time

dac = [26,19,13,6,5,11,9,10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        for i in range(0,256):
            c = decimal2binary(int(i))
            GPIO.output(dac,c)
            time.sleep(0.05)
        GPIO.output(dac,0)
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()