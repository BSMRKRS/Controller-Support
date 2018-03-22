# Controller-Support

Welcome to Controller Support! This repo was created for the BSM robot. This program has only been tested on Mac OSX with a robot running raspbian (debian).

## Setup

- Make sure you have the required packages
- Clone this repo to both the laptop and robot
- An alternitive to downloading the whole repo to your robot is downloading it from http://andrewvoss.org/downloads/host.py
```
$ wget http://anndrewvoss.org/downloads/RoboPiLib.py
$ wget http://andrewvoss.org/downloads/host.py
```
- Run host.py on robot and then run Controller on laptop (order matters and replace \<robot ip> w/ your robot's ip address)
```
$ python host.py <robot ip>
$ python Controller.py <robot ip>
```

## Required Packages on Host
- pygame
```
$ pip install pygame
```

## Write your own code

Checkout the branch named custom to write your own program with controller support.

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

## Button Mapping

Button mapping is supported, with the global variables defined in Controller.py in lines 51-53.

## Xbox Controllers (Xbox one & Xbox 360)

- requires this driver https://github.com/360Controller/360Controller/releases


## Mapping Options

- can choose to control speed w/ right and left triggers or use right joystick
- recommend using right joystick due to trigger dead zones

## Issues

- pygame does not recognize buttons other than the analog triggers and joysticks for xbox controllers

## Troubleshooting

```
Traceback (most recent call last):
  File "Controller.py", line 157, in <module>
    joysticks()
  File "Controller.py", line 61, in joysticks
    joystick = pygame.joystick.Joystick(0)
pygame.error: Invalid joystick device number
```
- Program does not recognize controller
