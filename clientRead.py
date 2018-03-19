# --------------------------------File on client--------------------------------
# Reads the ftp file from Host
import sys, socket
import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

######################
##    Host Info     ##
######################
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = ('192.168.21.113', 10000)
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
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            data = data.split('.')

            if data[0] == 'l':
                RPL.servoWrite(0, int(data[1]))

            if data[0] == 'r':
                RPL.servoWrite(0, int(-data[1]))

            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
