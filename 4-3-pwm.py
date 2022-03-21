import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)

p = GPIO.PWM(22,1000)



try:
    while True:
        duty_cycle = input()
        duty_cycle = int(duty_cycle)
        p.start(duty_cycle)

finally:
    GPIO.cleanup