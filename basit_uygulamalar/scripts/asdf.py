#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 21:55:23 2022

@author: eliz
"""

import rospy
from sensor_msgs.msg import LaserScan


def test():
    rospy.init_node("test")
    rospy.Subscriber("scan",LaserScan,callback)
    rospy.spin()
def callback(mesaj):
    rospy.loginfo("aci 0: %f"%mesaj.ranges[0])
    
test()