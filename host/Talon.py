# host/RoboPi.py
# Host file for robots using a RoboPi hat

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
from bsmLib.misc import map
from bsmLib import RPL

#### Global Variables ####
HOST = '0.0.0.0'
PORT = 10000

MIN = 1000 # Min servo speed
MAX = 2000 # Max servo speed

# Servo Pins
L = 0
R = 1

# PWM
PERIOD = 3000

######################
## 0. Setup
######################
# Create tcp connection and listen
t = tcpServer(HOST, PORT)
t.listen()

RPL.init() # Init RoboPi hat connection

# Set to PWM pin mode
RPL.pinMode(L, RPL.PWM)
RPL.pinMode(R, RPL.PWM)

######################
## 1. drive
######################
def drive():
    d = t.recv()
    if d == "stop":
        RPL.servoWrite(L, 0)
        RPL.servoWrite(R, 0)
        t.stop()
        exit()
    d = d.split(' ')
    l = int(map(float(d[0]), -1, 1, MIN, MAX))
    r = int(map(float(d[1]), -1, 1, MIN, MAX))
    RPL.pwmWrite(L, l, PERIOD)
    RPL.servoWrite(R, r, PERIOD)


######################
##      Main        ##
######################
if __name__ == "__main__":
    while(1):
        drive()
