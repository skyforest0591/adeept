import RPi.GPIO as GPIO
import move
import LED
import servo
# import socket_connect
# GPIO PIN Configuration
RIGHT_MOTOR_FORWARD_GPIO_PIN = 18
RIGHT_MOTOR_BACKWARD_GPIO_PIN = 17
LEFT_MOTOR_FORWARD_GPIO_PIN = 23
LEFT_MOTOR_BACKWARD_GPIO_PIN = 22

# Global variables
FORWARD_POWER_RIGHT = None;
BACKWARD_POWER_RIGHT = None;
FORWARD_POWER_LEFT = None;
BACKWARD_POWER_LEFT = None;
led = LED.LED()
# C = socket_connect.Connection()
def init():
    """ Initiate and configure the variables needed for the 'setRobotMotorPower' command."""
    
    # This function will assign the following global variables:
    global FORWARD_POWER_RIGHT
    global BACKWARD_POWER_RIGHT
    global FORWARD_POWER_LEFT
    global BACKWARD_POWER_LEFT
    '''
    GPIO.setwarnings(False)
    # Motor Right
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    FORWARD_POWER_RIGHT = GPIO.PWM(18, 100)
    BACKWARD_POWER_RIGHT = GPIO.PWM(17, 100)
    FORWARD_POWER_RIGHT.start(0)
    BACKWARD_POWER_RIGHT.start(0)

    # Motor Left
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    FORWARD_POWER_LEFT = GPIO.PWM(23, 100)
    BACKWARD_POWER_LEFT = GPIO.PWM(22, 100)
    FORWARD_POWER_LEFT.start(0)
    BACKWARD_POWER_LEFT.start(0)
    '''
    move.setup()


def set(motor, power):
    """ Execute the 'setRobotMotorPower' command. """
    # C.command_send(motor,power)
    # Set the power of left motor.
    if motor == "A":
        if power > 0:
            move.move(power,'forward')
            #FORWARD_POWER_LEFT.ChangeDutyCycle(power)
            #BACKWARD_POWER_LEFT.ChangeDutyCycle(0)
        elif power == 0:
            move.motorStop()
            #FORWARD_POWER_LEFT.ChangeDutyCycle(0)
            #BACKWARD_POWER_LEFT.ChangeDutyCycle(0)
        else:
            move.move(-power,'backward')
            #FORWARD_POWER_LEFT.ChangeDutyCycle(0)
            #BACKWARD_POWER_LEFT.ChangeDutyCycle(-power)
        
    elif motor == "B":
        if power > 0:
            move.move(power,'backward')
            #FORWARD_POWER_RIGHT.ChangeDutyCycle(power)
            #BACKWARD_POWER_RIGHT.ChangeDutyCycle(0)
        elif power == 0:
            move.motorStop()
            #FORWARD_POWER_RIGHT.ChangeDutyCycle(0)
            #BACKWARD_POWER_RIGHT.ChangeDutyCycle(0)
        else:
            move.move(-power,'forward')
            #FORWARD_POWER_RIGHT.ChangeDutyCycle(0)
            #BACKWARD_POWER_RIGHT.ChangeDutyCycle(-power)

    if motor == 'Left':
        servo.turnLeft(float(power/255))
        # led.setcolor('R',power)
    elif motor == 'Right':
        servo.turnRight(float(power/255))
        # led.setcolor('G',power)
    elif motor == 'Middle':
        servo.turnMiddle()
        # led.setcolor('B',power)

    return 0;