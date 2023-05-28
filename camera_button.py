import RPi.GPIO as GPIO
import time
import os

def button_callback(channel):
	print("Button was pushed!")
	os.system("/home/konsta/raspicamera/capture.sh")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)
GPIO.output(6, GPIO.HIGH)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(5,GPIO.RISING,callback=button_callback)

message = input("Press enter to quit \n\n")

GPIO.cleanup()
