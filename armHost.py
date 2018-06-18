# --------------------------------File on Robot---------------------------------
# Hosts a TCP connection and interprets the data recieved
import sys, os, socket
import arm
import RoboPiLib as RPL
from time import sleep
RPL.RoboPiInit("/dev/ttyAMA0",115200)

# Grasper Pins
grasper0 = 10
grasper1 = 11

def convertServo(x):
    return (x + 1500)

######################
##    Host Info     ##
######################
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
host = '0.0.0.0'
server_address = (host, 10001)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(9)
            data = data.split(' ')

            if int(data[0]) == 1:
                arm.shoulder(1, .05, 500)
            if int(data[0]) == 2:
                arm.shoulder(0, .05, 500)
            if int(data[0]) == 3:
                arm.elbow(1, .05, 100)
            if int(data[0]) == 4:
                arm.elbow(0, .05, 100)
            if int(data[0]) == 5:
                RPL.servoWrite(grasper0, convertServo(-int(data[1])))
                RPL.servoWrite(grasper1, convertServo(int(data[1])))
            if int(data[0]) == 6:
                arm.wristRotate()
            if int(data[0]) == 7:
                arm.wristUp()
            if int(data[0]) == 8:
                arm.wristDown()
            if int(data[0]) == 9:
                arm.turretRight()
            if int(data[0]) == 10:
                arm.turretRight()
            else:
                arm.wristStop()
                arm.turretStop()
                arm.stop()

            connection.sendall('r')

    finally:
        connection.close()
