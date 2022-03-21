import RPi.GPIO as GPIO

dac = [26,19,13,6,5,11,9,10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        num = int(input())
        if num == 'q':
            quit()
        elif num != int(num):
            print("incorrect input")
            continue
        elif num<0:
            print("incorrect input")
            continue
        elif num>255:
            print("incorrect input")
            continue
        c = decimal2binary(int(num))
        GPIO.output(dac,c)
        print(num*(3.3/256))
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()