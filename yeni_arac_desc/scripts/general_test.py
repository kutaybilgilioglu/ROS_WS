#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 06:26:41 2022

@author: kutay
"""
import rospy
import math
from std_msgs.msg import String
from std_msgs.msg import Int8
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler


class navigate():
   def __init__(self):
      rospy.init_node("nav")
      rospy.Subscriber("/odom",Odometry,self.odomCb)
      
      
      
      rospy.spin()
   def odomCb(self,msg):
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    yaw = yaw*(180/math.pi)
    if yaw < 0:
        yaw = yaw + 360
    print(yaw)
navigate()