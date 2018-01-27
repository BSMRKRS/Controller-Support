# Controller-Support

Welcome to Controller Support! This repo was created for the BSM robot. This program has only been tested on Mac OSX with a robot running raspbian (debian).

## Supported Controllers/Tested Controllers

Full Support:
- PS4 Controller (wired or wireless)

Partial Support:
- Xbox One Controller (wired) - pygame doesn't recognize all buttons
- Xbox 360 Controller (wired) - pygame doesn't recognize all buttons

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
- Change the ip, username, and password in the file clientRead.py on line 10 and this repos directory on line 11
- Start ftp on the host computer:
```
$ sudo -s launchctl load -w /System/Library/LaunchDaemons/ftp.plist
```
- Run clientRead.py on client and Controller.py on host


## Required Packages on Host

- pip
```
$ sudo easy_install pip
```
- pygame
```
$ pip install pygame
```

## Required Packages on Client

- ftp
```
$ sudo apt-get install ftp
```

## Mapping Options

- can choose to control speed w/ right and left triggers or use right joystick
- recommend using right joystick due to trigger dead zones

## Issues

- pygame does not recognize buttons other than the analog triggers and joysticks for xbox controllers

## Troubleshooting

```
Traceback (most recent call last):
  File "Controller.py", line 127, in <module>
    joysticks()
  File "Controller.py", line 54, in joysticks
    joystick = pygame.joystick.Joystick(0)
pygame.error: Invalid joystick device number
```
- Program does not recognize controller
