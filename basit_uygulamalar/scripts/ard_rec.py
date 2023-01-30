#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 02:01:43 2022

@author: kutay
"""

import rospy 
from std_msgs.msg import String
class com():
    def __init__(self):
        rospy.init_node("arduino_rec")
        
        rospy.Subscriber("chatter",String,self.msgCallback,queue_size=1)
        rospy.spin()
    def msgCallback(self,msg):
        rospy.loginfo(msg.data)
        
        
com()
        
