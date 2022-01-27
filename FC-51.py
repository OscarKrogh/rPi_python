import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM) #alternative GPIO.BOARD



signal = 20
signal2 = 21
LedR = 16

GPIO.setup(LedR, GPIO.OUT)
GPIO.setup(signal, GPIO.IN)
GPIO.setup(signal2, GPIO.IN)

try:
    while True: # True = 1
        val = GPIO.input(signal) # read FC-51 out pin
        print(val)
        time.sleep(0.5)
        
        if val == 0:
            #GPIO.input(signal, False)
            GPIO.output(LedR, False)
        else:
            #GPIO.input(signal, True)
            GPIO.output(LedR, True)
except KeyboardInterrupt: # Stop program with Ctrl+C
# clean up GPIO pint to ennsure that all inputs/outputs are reset
    print("Setting all GPIO pins to default")
    GPIO.cleanup() #set all GPIO pint to default state
    print("exiting program")