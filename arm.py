import RoboPiLib_pwm as RPL
import time as time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

shoulder_pul = 5
shoulder_dir = 3
elbow_pul = 7
elbow_dir = 6

wrist0 = 9
wrist1 = 8

turret = 20

up = True
down = False

RPL.pinMode(shoulder_pul, RPL.PWM)
RPL.pinMode(shoulder_dir, RPL.OUTPUT)
RPL.pinMode(elbow_pul, RPL.PWM)
RPL.pinMode(elbow_dir, RPL.OUTPUT)

speed = 1000

def stop():
  RPL.pwmWrite(shoulder_pul, 0, 10000)
  RPL.pwmWrite(elbow_pul, 0, 10000)

def shoulder(dir, run_for = 1, speed = speed):
  if(dir):
    RPL.digitalWrite(shoulder_dir, 1)
  else:
    RPL.digitalWrite(shoulder_dir, 0)
  RPL.pwmWrite(shoulder_pul, speed, speed * 2)

def elbow(dir, run_for = 1, speed = speed):
  if(dir):
    RPL.digitalWrite(elbow_dir, 1)
  else:
    RPL.digitalWrite(elbow_dir, 0)
  RPL.pwmWrite(elbow_pul, speed, speed * 2)

def wristUp():
    RPL.servoWrite(wrist0, 1000)
    RPL.servoWrite(wrist1, 1000)

def wristDown():
    RPL.servoWrite(wrist0, 2000)
    RPL.servoWrite(wrist1, 2000)

def wristRotate():
    RPL.servoWrite(wrist0, 1000)
    RPL.servoWrite(wrist1, 2000)

def wristStop():
    RPL.servoWrite(wrist0, 0)
    RPL.servoWrite(wrist1, 0)

def turretLeft():
    RPL.servoWrite(turret, 1800)

def turretRight():
    RPL.servoWrite(turret, 1400)

def turretStop():
    RPL.servoWrite(turret, 0)
