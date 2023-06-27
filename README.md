# pilapse2
_Pilapse2_ is a web based controller for headless Raspberry Pi with a camera.

Included Functionality:
* Setting up the camera
* Running timelapse application
* Running motion detection application

## Building Pilapse2
## Installing Pilapse2
### Requirements
#### Hardware
Currently only works on a Raspberry Pi. We strongly recommend using a Raspberry Pi 4 but I have run it on Raspberry 
Pi 2 and 3.
#### Software
* Raspberry Pi OS
  * 32 bit (64 not tested)
  * Debian 11 (Bullseye)
  * Desktop version is not required
* OpenCV
#### Configuration (raspi-config)
Pilapse2 is based on libcamera and will not work with Raspberry Pi's legacy camera support. Use raspi-config to ensure 
that legacy camera support is disabled. 
## Running Pilapse2
### Setting Up the Camera
### Using the Timelapse Application
### Using the Motion Detection Application