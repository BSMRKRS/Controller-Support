# Robot-Controller-Support

Welcome to Robot Controller Support! This repo was created for the BSM robot. This program has only been tested on Mac OSX with a robot running raspbian (debian).

## Supported Controllers/Tested Controllers

Full Support:
- PS4 Controller (wired or wireless)

Partial Support:
- Xbox One Controller (wired) - changing controller scheme on the fly doesn't work
- Xbox 360 Controller (wired) - changing controller scheme on the fly doesn't work

Not Supported:
- Asus GamePad

Not Tested:
- Logitech controllers
- PS3 controller
- PS2 controller
- Original Xbox controller
- Wii U Pro Controller
- Wii Pro Controller

## Xbox Controllers (Xbox one & Xbox 360)

- requires this driver https://github.com/360Controller/360Controller/releases

## Setup

- Make sure you have the required packages
- Clone this repo to both the client and the host computer
- Change the ip, username, and password in the file clientRead.py on line 7 and this repos directory on line 8
- Start ftp on the host computer:
```
$ sudo -s launchctl load -w /System/Library/LaunchDaemons/ftp.plist
```
- Run clientRead.py on client
- Run Controller.py on host


## Required Packages

- pip
```
$ curl -O http://python-distribute.org/distribute_setup.py
$ python distribute_setup.py
$ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
$ python get-pip.py
```
- pygame
```
$ pip install pygame
```

## Mapping Options

- can choose to control speed w/ right and left triggers or use right joystick
- recommend using right joystick due to trigger dead zones
- can changing mapping during use by pressing right bumper

## Issues

- Xbox One & Xbox 360 Controller can't swap controller scheme on the fly
- Changing controller scheme on the fly in not consistent

## Troubleshooting

You will receive this error if the program does not recognize your controller

Traceback (most recent call last): </br>
&nbsp;&nbsp;&nbsp;  File "Controller.py", line 120, in <module> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    roboSpeed() </br>
&nbsp;&nbsp;&nbsp;  File "Controller.py", line 70, in roboSpeed </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    if -yDeadZoneRight < yAxisRight < yDeadZoneLeft: </br>
NameError: global name 'yAxisRight' is not defined </br>
