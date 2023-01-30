#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 16:08:30 2022

@author: kutay
"""

import rospy
from tf.transformations import euler_from_quaternion
from nav_msgs.msg import Odometry
import numpy as np

def test():
    rospy.init_node("odom_etst")
    rospy.Subscriber("odom",Odometry,callback)
    rospy.spin()
def callback(mesaj):
    orientation_q = mesaj.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    rderece= yaw*(180/np.pi)
    rospy.loginfo("rderece: %d"%rderece)
test()