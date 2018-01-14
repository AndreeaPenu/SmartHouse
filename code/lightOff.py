#!/usr/bin/python


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT) 
GPIO.output(4, True)

def trigger() :
    GPIO.output(4, False)
#   GPIO.cleanup()
    break
     

try: 
    trigger()
         
		
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()