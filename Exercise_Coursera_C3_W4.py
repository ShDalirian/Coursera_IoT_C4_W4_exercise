import Rpi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
while True:
    if GPIO.input(16):
        GPIO.output(18, True)
		time.sleep(0.5)
		GPIO.output(18, False)
        time.sleep(0.5)
    else:
		GPIO.output(18, True)
