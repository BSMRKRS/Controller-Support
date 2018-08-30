# host/ax-12.py
# Host file for robots using AX-12 servos

# MIT License
#
# Copyright (c) 2018 BSMRKRS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from bsmLib.networking import tcpServer
from pyax12.connection import Connection

#### Global Variables ####
HOST = '0.0.0.0'
PORT = 10000

DEVICE = '/dev/ttyACM0' # Ax-12 servos

# Servo IDs
L = (1, 2) # Left servos
R = (2, 3) # Right Servos


######################
## 0. Setup
######################
# Create tcp connection and listen
t = tcpServer(HOST, PORT)
t.listen()

sc = Connection(port=DEVICE, baudrate=1000000)

# Set servos to continuous
for i in (L + R):
    set_continuous(i)


######################
## 1. Continuous
######################
def set_continuous(motor_id):
    sc.set_cw_angle_limit(motor_id, 0, degrees=False)
    sc.set_ccw_angle_limit(motor_id, 0, degrees=False)


######################
## 2. Speed Convert
######################
def speedConvert(speed):
    if(speed > 0.0):
        speed = 1024 + speed * 1023
        return speed
    elif(speed < 0.0):
        speed = -speed * 1023
        return speed
    else:
        speed = 0
        return speed


######################
## 3. Drive
######################
def drive():
    d = t.recv()
    if d == "stop":
        for i in (L + R):
            sc.set_speed(i, 0)
        t.stop()
        exit()
    d = d.split(' ')
    l = int(speedConvert(float(d[0])))
    r = int(speedConvert(float(d[1])))
    for i in L:
        sc.set_speed(i, l)
    for i in R:
        sc.set_speed(i, r)


######################
##      Main        ##
######################
if __name__ == "__main__":
    while(1):
        drive()
