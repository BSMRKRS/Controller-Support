# --------------------------------File on client--------------------------------
# Reads

import RoboPiLib as RPL
import ftplib
RPL.RoboPiInit("/dev/ttyAMA0",115200)
while True:
    ftp = ftplib.FTP('ip', 'username', 'password') # host computer info
    ftp.cwd('directory of this repository') # directory of repo on host
    gFile = open("ftpTemp.txt", "wb")
    ftp.retrbinary('RETR ftpTemp', gFile.write)
    gFile.close()
    ftp.quit()
    gFile = open("ftpTemp.txt", "r")
    buff = gFile.read()
    convertTxtArray = buff.split()
    motorL = convertTxtArray[0]
    motorR = convertTxtArray[1]
    RPL.servoWrite(0, int(float(motorL))) # for some odd reason would not convert directly to int with int()
    RPL.servoWrite(1, int(float(motorR))) # for some odd reason would not convert directly to int with int()
