#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:20:34 2022

@author: kutay
"""

import rospy 
from nav_msgs.msg import Odometry


def test():
    rospy.init_node("Hiz_gosterge")
    rospy.Subscriber("odom",Odometry,callback)
    rospy.spin()
def callback(mesaj):
    rospy.loginfo("lineer: %f  acisal: %f"%(mesaj.twist.twist.linear.x,mesaj.twist.twist.angular.z))
    
test()