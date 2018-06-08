# --------------------------------File on Latop---------------------------------
# Reads controller input and connects to robot
import os, sys, socket
import pygame
from time import sleep

#### Global Variables ####

mode = 1 # starting mode; 1 for driving and 0 for arm

socketRate = .1 # Make larger number to slow do info sent to Robot; larger number creates more latency; Too low of number sents too much info
socketRateArm = 1

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
    print "For support please visit https://github.com/BSMRKRS/Controller-Support.git"
    print "#"*60
    print "To controll use the left and right joystick."
    print "Hit xbox button to quit."
    print "#"*60
    print "Hit Enter to begin!"
    raw_input("$: ")
    print "#"*60


######################
## 2. Controller Reading
######################
def controllerInput():
    global xAxisLeft, yAxisLeft, xAxisRight, yAxisRight

    dpadleft = 0
    dpadright = 0
    dpaddown = 0
    dpadup = 0

    pygame.event.get()

    try:
        joystick = pygame.joystick.Joystick(0)
    except:
        print "ERROR: Controller not found!"
        print "#" * 60
        exit()

    joystick.init()

    xAxisLeft = joystick.get_axis(0)
    yAxisLeft = joystick.get_axis(1)

    xAxisRight = joystick.get_axis(2)
    yAxisRight = joystick.get_axis(3)

    triggerLeft = joystick.get_axis(4)
    triggerRight = joystick.get_axis(5)

    start = joystick.get_button(4)
    xbox = joystick.get_button(10)

    bumperR = joystick.get_button(9)
    bumperL = joystick.get_button(8)

######################
## 3. Inturpret Joystick
######################
def driveMotors():
    global motorL, motorR

    if -yDeadZoneRight < yAxisRight < yDeadZoneRight:
        motorSpeedL = 0
        motorSpeedR = 0
    else:
        motorSpeedL = maxMotorL * -yAxisRight
        motorSpeedR = maxMotorR * -yAxisRight

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
## 5. Arm
######################
def arm():
    if -yDeadZoneRight < yAxisRight < yDeadZoneLeft:
        print "Arm: Stopped"
    elif yAxisRight <= 0:
        print "Arm: Forwards"
        sockArm.sendall('0001 0000')
        sleep(socketRate)
    else:
        print "Arm: Backwards"
        sockArm.sendall('0002 0000')
        sleep(socketRate)

    if -yDeadZoneLeft < yAxisLeft < yDeadZoneLeft:
        print "Elbow: Stopped"
    elif yAxisLeft <= 0:
        print "Elbow: Forwards"
        sockArm.sendall('0003 0000')
        sleep(socketRate)
    else:
        print "Elbow: Backwards"
        sockArm.sendall('0004 0000')
        sleep(socketRate)




######################
## 5. Grasper
######################
def grasper():
    if triggerRight > -1.0:
        print "Grasper: Closing"
    else:
        print "Grasper: Stop"
    if triggerLeft > -1.0:
        print "Grasper: Opening"
    else:
        print "Grasper: Stop"


######################
## 5. Turret
######################
def turret():
    if bumperR:
        print "Turret: Right"
    elif bumperL:
        print "Turret: Left"
    else:
        print "Turret: Stopped"


######################
## 6. Connect to Network
######################
def connection(ip, port):
    try:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port on the server given by the caller
        server_address = (ip, port)
        print >>sys.stderr, 'connecting to %s port %s' % server_address
        sock.connect(server_address)
        return sock
    except:
        print "#" * 60
        print "ERROR: Failed to connect to host"
        print "#" * 60
        sleep(2)

######################
##      Main        ##
######################
ui()
try:
    sockDrive = connection(sys.argv[1], 10000)
except:
    print "No drive ip"
try:
    sockArm = connection(sys.argv[2], 10001)
except:
    print "No arm ip"
sleep(1)

while True:
    controllerInput()
    if xbox:
        #arm.control("stop")
        print "Exiting...bye"
        exit()

    if start:
        mode += 1
        mode %= 2
        sleep(1)

    if mode:
        drive = driveMotors()

        try:
            sockDrive.sendall(str(int(KitBotSpeed(-drive[0]))) + ' ' + str(int(KitBotSpeed(drive[1]))))
            sleep(socketRate)

        except:
            print "Error: Failed to connect to Robot"
            #exit()

        os.system('clear')
        print "#"*60
        print "##", " "*20, "Motor Values", " " *20, "##"
        print "#"*60
        print "motorL: ", drive[0], "motorR: ", drive[1]
    else:
        os.system('clear')
        arm()
        grasper()
        turret()
