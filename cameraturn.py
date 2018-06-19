import setup
import RoboPiLib as RPL
import time as time

#motor pin
mv = 8

#speed
left = 100
right = 1000

print "Left or Right?"

while raw_input("> ") == "Left":
    bro = time.time() + 0.5
    while time.time() < bro:
        RPL.servoWrite(mv, left)
        if time.time() >= bro:
            RPL.servoWrite(mv, 0)
while raw_input("> ") == "Right":
    bruh = time.time() + 0.5
    while time.time() < bruh:
        RPL.servoWrite(mv, right)
        if time.time() >= bruh:
            RPL.servoWrite(mv, 0)
else:
    print "Made a mistake there, bud."
