# --------------------------------File on Host---------------------------------
# Reads controller input and writes to file that is read from clientRead.py on robot
import pygame
import os

#### Global Variables ####

# left and right joystick dead zones (current dead zone for ps4 controller)
xDeadZoneLeft = 0.06
yDeadZoneLeft = 0.06
xDeadZoneRight = 0.06
yDeadZoneRight = 0.06

# motor speeds (assumes there is the same possible speeds going in reverse)
maxMotorL = 500
maxMotorR = 500

######################
## 0. Initialization
######################
pygame.init()
pygame.display.init()
pygame.joystick.init()

######################
## 1. UI
######################
def ui():
    global controllerScheme
    print "#"*60
    print "Welcome to the BSM robot controller support python program!"
    print "#"*60
    controller = open('controllerASCII', "r")
    print controller.read()
    print "#"*60
    print "I recommend choosing the joystick layout."
    print "For support please visit https://github.com/BSMRKRS/Controller-Support.git"
    print "#"*60
    print "Please select a controller scheme:"
    print "0. Speed control w/ right joystick"
    print "1. Speed control w/ triggers"
    controllerScheme = input("$: ")
    print "#"*60

    # Defualts to joystick control if input was not put in correctly
    if controllerScheme != 0:
        if controllerScheme != 1:
            controllerScheme = 0


######################
## 2. Controller Reading
######################
def controllerInput():
    global xAxisLeft, yAxisLeft, xAxisRight, yAxisRight, triggerLeft, triggerRight
    global buttonSquare, buttonX, buttonCircle, buttonTriangle
    global dpadleft, dpadright, dpaddown, dpadup, bumperL, bumperR

    dpadleft = 0
    dpadright = 0
    dpaddown = 0
    dpadup = 0

    pygame.event.get()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    xAxisLeft = joystick.get_axis(0)
    yAxisLeft = joystick.get_axis(1)

    xAxisRight = joystick.get_axis(2)
    yAxisRight = joystick.get_axis(3)

    triggerLeft = joystick.get_axis(4)
    triggerRight = joystick.get_axis(5)

    buttonSquare = joystick.get_button(0)
    buttonX = joystick.get_button(1)
    buttonCircle = joystick.get_button(2)
    buttonTriangle = joystick.get_button(3)

    bumperL = joystick.get_button(4)
    bumperR = joystick.get_button(5)

    dpad = joystick.get_hat(0)
    dpadxaxis = dpad[0]
    dpadyaxis = dpad[1]

    if dpadxaxis > 0:
        dpadright = dpadxaxis
    if dpadxaxis < 0:
        dpadleft = -dpadxaxis
    if dpadyaxis > 0:
        dpadup = dpadyaxis
    if dpadyaxis < 0:
        dpaddown = -dpadyaxis


######################
## 3. Inturpret Joystick
######################
def driveMotors():
    global motorL, motorR

    if -yDeadZoneRight < yAxisRight < yDeadZoneLeft:
        motorSpeedL = 0
        motorSpeedR = 0

    elif controllerScheme == 0:
        motorSpeedL = maxMotorL * -yAxisRight
        motorSpeedR = maxMotorR * -yAxisRight

    if controllerScheme == 1:
        if triggerRight >= 0:
            motorSpeedL = .5 * maxMotorL * (triggerRight+1)
            motorSpeedR = .5 * maxMotorR * (triggerRight+1)
        elif triggerLeft > 0:
            motorSpeedL = .5 * maxMotorL * -(triggerLeft+1)
            motorSpeedR = .5 * maxMotorR * -(triggerLeft+1)

    if -xDeadZoneLeft < xAxisLeft < xDeadZoneLeft:
        motorL = motorSpeedL
        motorR = motorSpeedR

    elif xAxisLeft <= 0:
        motorL = motorSpeedL - (motorSpeedL * (-xAxisLeft))
        motorR = motorSpeedR
    elif xAxisLeft > 0:
        motorL = motorSpeedL
        motorR = motorSpeedR + (motorSpeedR * (-xAxisLeft))

    return motorL, motorR


######################
## 4. Convert to KitBot
######################
def KitBotSpeed(speed):
    center = 1500
    return speed + center


######################
## 5. Write to ftpTemp
######################
def updateFTP(data):
    f.seek(0)
    f.write(str(KitBotSpeed(-data[0])))
    f.write(" ")
    f.write(str(KitBotSpeed(data[1])))
    f.write(" ")
    f.truncate()


######################
##      Main        ##
######################
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
server_address = ("192.168.21.113", 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

ui()
f = open('ftpTemp','r+')
while True:
    controllerInput()
    drive = driveMotors()

    try:
        message = 'This is the message.  It will be repeated.'
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall("l." + int(float(data[0])))
        sock.sendall("r." + int(float(data[1])))

        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print >>sys.stderr, 'received "%s"' % data

    finally:
        sock.close()

    os.system('clear')
    print "#"*60
    print "##", " "*20, "Motor Values", " " *20, "##"
    print "#"*60
    print "motorL: ", drive[0], "motorR: ", drive[1]
