# DrawingBot

The Drawing Bot // R.3 Studio  is a project of IAAC, Institute for Advanced Architecture of Catalonia developed at the Master in Robotics and Advanced Construction in 2020/21 by:

Students: Helena Homsi, Juan E. Ojeda, Aslinur Taskin

Faculty: Alexandre Dubor, Aldo Sollazzo

Faculty Assistant: Antoine Jaunard, Ashkan Foroughi, Soroush Garivani

## Getting Started 
This repository will consist of several files each in their respective folders. The idea is to share all current working files in order to expand on the idea of designing and drawing with robots. We will be using a **Turtlebot 3 with a Raspberry Pi 3** containing **Ros Kinetic** as well as a computer running **Ubuntu 16.04**. All necessary files are located in this github and will be explained in the following steps. For the general set up we followed the following website, but our files that are in this github contain more than what is offered in the setup link: https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/

## Requirements
### For the Turtlebot 3: 
1. 32GB Micro SD Card
2. Raspberry Pi 3 (should already come with the Turtlebot 3 package)
* Download and upload the image file in the folder titled **_Turtlebot3 Image File_** onto a 32GB micro sd card to put into a Raspberry Pi 3 (this image file is the one we worked with)
* Additionally, a clean version of the image file could be found in the following website https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/#sbc-setup 


### For Ubuntu 16.04:
* Download and upload the disk image file in the folder titled **_Ubuntu 16.04_** onto a USB 
* If you prefer to use a clean disk image, you can download the disk image titled **_Ubuntu16.04_Clean_** and follow the instructions on this link in order to complete the rest of the set up: https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup 

We installed Ubuntu 16.04 on a bootable external hard drive, and we used a 64GB USB as the external hard drive. The following link is how we set up a USB for it to be bootable: https://www.youtube.com/watch?v=PyfqwCFwQ3w&t=428s

Note: If you are using a mac, even if you are using windows via bootcamp, you will have to prepare the USB differently to be able to use it to boot from a mac hardware. 

### For Rosbridge Connection:
* On the Ubuntu side, install https://github.com/RobotWebTools/rosbridge_suite

This allows us to subscribe/ publish to topics in ROS from/ to Grasshopper




After following the instructions to set up the connection between Ubuntu and Turtlebot3, do the following on the Ubuntu side:

```
roscore
```
SSH into the RPI and activate the Turtlebot3
```
ssh pi@[IP ADDRESS OF PI]
source ~/.bashrc
export OPENCR_PORT=/dev/ttyACM0
export OPENCR_MODEL=burger
cd ./opencr_update
./update.sh $OPENCR_PORT $OPENCR_MODEL.opencr
roslaunch turtlebot3_bringup turtlebot3_robot.launch
```
(to manually test out the movement of the robot):
```
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
(to create the bridge between ROS and GH):
```
roslaunch rosbridge_server rosbridge_websocket.launch
```
run the grasshopper file titled **_FloorPainting_** and connect to the IP address of Ubuntu by changing the IP address and clicking the button below the IP address. Then run the following on the Ubuntu side:

```
grasshopper.py
```

In order to make sure the orientation and location of the Turtlebot3 is correct on your Rhino screen, rotate and move the TB3 using teleop, and if adjustments are necessary then the rotation adjustment part of the script is highlighted and tagged. 