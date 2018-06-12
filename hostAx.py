# --------------------------------File on Robot---------------------------------
# Hosts a TCP connection and interprets the data recieved
import sys, os, socket, re
from pyax12.connection import Connection

sc = Connection(port="/dev/ttyACM0", baudrate=1000000)

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
sock.bind(server_address)
sock.listen(1)

######################
##      Main        ##
######################
while True:
    connection, client_address = sock.accept()
    try:
        while True:
            data = connection.recv(9)
            data = str(data)
            data = re.sub("[b']", '', data)
            print("Data: ",data)
            data = data.split(' ')

            sc.set_speed(1, int(data[0]))
            sc.set_speed(2, int(data[0]))

            sc.set_speed(3, int(data[1]))
            sc.set_speed(4, int(data[1]))

    finally:
        connection.close()
