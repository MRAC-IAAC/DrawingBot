#!/usr/bin/env python

from __future__ import print_function
import rospy
import actionlib
import turtlebot3_example.msg
import sys
from geometry_msgs.msg import Twist
from math import radians


def callback(data, param):
    print (data)
    vel = param[0]
    vel.publish(data)



if __name__ == '__main__':
    try:
        param = []
        rospy.init_node('drawasquare', anonymous=False)
        cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=100)
        param.append(cmd_vel)
        gh_cmd = rospy.Subscriber('/gh', Twist, callback, param)
        rospy.spin()

    except:
        rospy.loginfo("node terminated.")
