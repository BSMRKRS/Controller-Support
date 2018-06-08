# --------------------------------File on Robot---------------------------------
# Hosts a TCP connection and interprets the data recieved
import sys, os, socket
from pyax12.connection import Connection

sc = Connection(port="/dev/cu.usbmodem1421", baudrate=1000000)

numMotor = 4

def set_continuous(motor_id):
    sc.set_cw_angle_limit(motor_id, 0, degrees=False)
    sc.set_ccw_angle_limit(motor_id, 0, degrees=False)

for i in range(1, numMotor):
    set_continuous(i)

######################
##    Host Info     ##
######################
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
host = '0.0.0.0'
server_address = (host, 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)

######################
##      Main        ##
######################
while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(9)
            data = data.split(' ')

            sc.set_speed(1, int(data[0]))
            sc.set_speed(4, int(data[0]))

            sc.set_speed(2, int(data[1]))
            sc.set_speed(3, int(data[1]))

    finally:
        connection.close()
