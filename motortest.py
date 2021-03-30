import RPi.GPIO as GPIO
import time

# Set the GPIO board layout
GPIO.setmode(GPIO.BOARD)

#setting motor to pin 16 with output
GPIO.setup(16, GPIO.OUT)
servo = GPIO.PWM(16,50) #pin 16 with 50 hz output

#start the servo
servo.start(0)


print("clockwise")
#turns the motor clockwise
servo.ChangeDutyCycle(5)
time.sleep(2)
#this stops the motor
print("stop")
servo.ChangeDutyCycle(0)
time.sleep(2)
#rotates the motor counter-clockwise
print("counter-clockwise")
servo.ChangeDutyCycle(10)
time.sleep(2)

#Changing the duty cycle will change the speed of the rotation and the dirction
#greater than 7 will make it counter-clockwise
#less than 7 will make it clockwise
#numbers greater than 12 on the duty cycle will not work as well as negative numbers
#duration is determined by the sleep time put after the duty cycle
#servo.start(0) wil initiate the motor with no movement
#always change the duty cycle to 0 will stop all movement

servo.stop()
GPIO.cleanup()
print("Goodbye!")