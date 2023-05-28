import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)
GPIO.output(6, GPIO.HIGH)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	if GPIO.input(5) == GPIO.HIGH:
		print("Button was pushed!")
		time.sleep(0.3)
