# controller.py
# Basic script for driving robot

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


from bsmLib.controller import controller
from bsmLib.networking import tcpClient
from sys import argv

#### Global Variables ####
DEADZONE = .2 # Controller deadzone

HOST = argv[1]
PORT = 10000


######################
## 0. Setup
######################
# Setup Controller
c = controller(0, DEADZONE)

# Create tcp connection & connect
t = tcpClient(HOST, PORT)
t.connect()


######################
## 1. Drive
######################
def drive():
    c.update()

    # Trigger turn in place
    if(c.RT > -1.0):
        s = (c.RT + 1) / 2
        return s, s
    elif(c.LT > -1.0):
        s = (c.LT + 1) / 2
        return -s, -s

    # Analog speed from Left Joystick
    l = c.LY
    r = c.LY

    # Direction from Right Joystick
    if(c.RX <= 0.0):
        l += (l * (c.RX))
    elif(c.RX > 0.0):
        r -= (r * (c.RX))

    return -l, r


######################
## 2. Run
######################
def run():
    if c.XBOX:
        t.send("stop")
        t.stop()
        exit()
    d = drive()
    d = "%f %f" % (d[0], -d[1])
    t.send(d)

######################
##      Main        ##
######################
if __name__ == "__main__":
    while(1):
        run()
