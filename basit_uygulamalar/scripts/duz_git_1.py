#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 00:42:08 2022

@author: kutay
"""

import rospy
from geometry_msgs.msg import Twist

def hareket():
    rospy.init_node("duz_git")
    pub=rospy.Publisher("cmd_vel",Twist,queue_size=10)
    hiz_mesaji=Twist()
    hiz_mesaji.linear.x=0.5
    mesafe=5
    yer_degistirme=0
    t0=rospy.Time.now().to_sec()
    while(yer_degistirme<mesafe):
        pub.publish(hiz_mesaji)
        t1=rospy.Time.now().to_sec()
        yer_degistirme = hiz_mesaji.linear.x*(t1-t0)
    hiz_mesaji.linear.x=0.0
    pub.publish(hiz_mesaji)
    rospy.loginfo("hedefe varildi")
hareket()    
