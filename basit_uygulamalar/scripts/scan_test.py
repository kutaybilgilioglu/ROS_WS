#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 14:34:59 2022

@author: kutay
"""

import rospy 
from sensor_msgs.msg import LaserScan

def scan():
    rospy.init_node("scan_test")
    rospy.Subscriber("scan",LaserScan,scanCallback)
    rospy.spin()
    
def scanCallback(mesaj):
    rospy.loginfo(mesaj.range_max)
    rospy.loginfo(mesaj.header.frame_id)
    rospy.loginfo(mesaj.angle_max)
    
scan()