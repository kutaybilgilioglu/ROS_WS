#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 19:21:31 2022

@author: kutay
"""
import rospy
from sensor_msgs.msg import LaserScan

def test():
    rospy.init_node("test")
    rospy.Subscriber("scan",LaserScan,callback)
    rospy.spin()
def callback(mesaj):
    rospy.loginfo(len(mesaj.ranges))
    rospy.loginfo("min: %f  max: %f  incr:%f  tincr:%f t:%f rmax:%f rmin:%f"%(mesaj.angle_min,mesaj.angle_max,mesaj.angle_increment,mesaj.time_increment,mesaj.scan_time,mesaj.range_min,mesaj.range_max))
    
    
test()
