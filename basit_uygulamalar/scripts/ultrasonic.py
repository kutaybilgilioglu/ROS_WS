#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 02:05:23 2022

@author: eliz
"""
import rospy
import numpy as np
from std_msgs.msg import Float64MultiArray, Float64, String, Int16, Bool,Int32MultiArray

class ultrasonic():
    def __init__(self):
        rospy.init_node("sensor_node")
        self.pub= rospy.Publisher("yuk_deger",Bool,queue_size=10)
        self.yukarda=Bool()
        rospy.Subscriber("distance",Float64,self.kontrol)
        rospy.spin()
        
    def kontrol(self,mesaj):
        kontrol=np.float(mesaj)
        if kontrol<25.0:
            self.yukarda=True
        else:
            self.yukarda=False
        self.pub.publish(self.yukarda)
        
ultrasonic()
