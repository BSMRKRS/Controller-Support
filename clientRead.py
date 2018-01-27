# --------------------------------File on client--------------------------------
# Reads the ftp file from Host
import RoboPiLib as RPL
import ftplib
RPL.RoboPiInit("/dev/ttyAMA0",115200)

######################
##    Host Info     ##
######################
ftp = ftplib.FTP('ip', 'username', 'password') # host computer info
ftp.cwd('directory of this repo') # directory of repo on host

######################
##      Main        ##
######################
while True:
    gFile = open("ftpTemp", "wb")
    ftp.retrbinary('RETR ftpTemp', gFile.write)
    gFile = open("ftpTemp", "r")
    buff = gFile.read()
    convertTxtArray = buff.split()
    motorL = convertTxtArray[0]
    motorR = convertTxtArray[1]
    RPL.servoWrite(0, int(float(motorL))) # for some odd reason would not convert directly to int with int()
    RPL.servoWrite(1, int(float(motorR))) # for some odd reason would not convert directly to int with int()
    print motorL, motorR
