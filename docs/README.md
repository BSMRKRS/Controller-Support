# Controller-Support

Welcome to Controller Support! This repo was created for the BSM robot. This program has only been tested on Mac OSX with a robot running raspbian (debian).

## Configure motors

- Change lines 11 & 12 to correct pin values for motors

## Setup

- Make sure you have the required packages
- Clone this repo to both the laptop and robot
- An alternative to downloading the whole repo to your robot is downloading RoboPiLib.py and host.py it using wget or curl

```
$ wget https://raw.githubusercontent.com/BSMRKRS/Controller-Support/master/RoboPiLib.py
$ wget https://raw.githubusercontent.com/BSMRKRS/Controller-Support/master/host.py
```

and download Controller.py to laptop

```
$ curl -O https://raw.githubusercontent.com/BSMRKRS/Controller-Support/master/Controller.py
```

- Run host.py on robot and then run Controller on laptop (order matters and replace \<robot ip> w/ your robot's ip address)

```
$ python host.py
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
- If you are on High Sierra you will need to use this work arround to enable this driver's kext to load
  - Open "System Preferences" and click "Keyboard" then "Input Sources" and enable keyboard access to "All controls"
  - ![alt text](docs/keyboard.png)
  - In "System Preferences" go to "Security & Privacy" and hit tab until the allow button is highlighted and hit space or enter.
  - ![alt text](docs/allow.png)
  - This issue happens on High Sierra due to not allowing any kext to be allowed while a monitoring software/screen controlling software is running like "LanSchool"


## Mapping Options

- can choose to control speed w/ right and left triggers or use right joystick
- recommend using right joystick due to trigger dead zones

## Issues

- pygame does not recognize buttons other than the analog triggers and joysticks for xbox controllers
