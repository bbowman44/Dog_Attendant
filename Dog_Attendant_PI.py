#importing libraries
from bluepy.btle import Scanner
from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time



pir = MotionSensor(17)          #declaring the motion sensor pin on the raspberry pi
GPIO.setup(18,GPIO.OUT)         #declaring the pin for the servo motor on the raspberry pi
servo1 = GPIO.PWM(18,50)        #settinp up the servo motor as a pwm
MP = -51                        #Measure power: this is the RSSI at 1 meter distance
scanner = Scanner()             #instantiating Scanner class

def Main():
    #loop for checking for motion and rotating motor
    print("Starting Device...")
    while True:
    
        print("Waiting for Motion")
        pir.wait_for_motion()       #wait for motion
        print('Motion detected, scanning for bluetooth tag')
        devices = scanner.scan(6.0) #declaring a variable to scan for bluetooth

        #loop for checking the distance of the bluetooth receiver
        
        for device in devices:
            
            distance = Distance(device.rssi)
            print('DEV = {} RSSI = {}'.format(device.addr,device.rssi))
            
            if device.addr == 'f5:af:3d:5b:0e:0d' and (distance <= 1):
                print('Device Detected')
                servo1.start(2.5)           #start the motor
                servo1.ChangeDutyCycle(2)   #clockwise movement
                print('opening door')
                time.sleep(0.6)
                servo1.ChangeDutyCycle(0)   #stops movement
                print('holding door')
                time.sleep(11.5)
                servo1.ChangeDutyCycle(10)  #counter clockwise movement
                print('door closing')
                time.sleep(0.52)
                servo1.ChangeDutyCycle(0)   #stop motor
        print('Door Closed')


def Distance(RSSI):

    distance = 10**((MP-(RSSI))/(10*2))
    return distance
