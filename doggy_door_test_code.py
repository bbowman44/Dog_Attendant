# Importing some libraries
from bluepy.btle import Scanner
from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time

scanner = Scanner()             # instansiating Scanner class
devices = scanner.scan(5.0)     # declaring a variable to scan for bluetooth devices
pir = MotionSensor(17)          # declaring the motion sensor pin on  the raspberry pi
servo1 = GPIO.PWM(4,50)         # setting up the servo motor as a pwm

# Note: the motor rotates 360 degrees:
# when motion is detected it rotates +180
# and when motion stops motor rotates another +180 degrees instead of -180 degrees
# need to figure out how to fix that

# loop for checking for motion and rotating motor
while True:
    pir.wait_for_motion()   # waits for motion to be detected
    print("Motion detected")
    servo1.start(0)         # start the motor
    time.sleep(2)           # wait two seconds

    # loop for checking the distance of the bluetooth receiver
    for device in devices:
        print("DEV = {} RSSI = {}".format(device.addr,device.rssi))     # print all the nearby low frequency bluetooth devices

        # checkes for a specific MAC address
        # if the MAC is address is present at a given distance rotate the motor
        if device.addr == 'f5:af:3d:5b:0e:0d' and device.rssi >= -48:
            print("It's close")
            servo1.start(2.5)               # start the motor with rotation
            servo1.ChangeDutyCycle(2.5)     # supposed to rotate motor 180 degrees (maybe redundant code)
            time.sleep(1)                   # rotates for 1 second
            servo1.ChangeDutyCycle(0)       # stops the motor
            time.sleep(5)                   # waits 5 seconds before executing rotation
            servo1.ChangeDutyCycle(10.5)    # sets rotations the other way'
            time.sleep(1)                   # rotates for 1 second
            servo1.ChangeDutyCycle(0)       # stops rotation

    print("Motion stopped")     # print that the motion has stopped

servo1.stop()       # stop the motor
