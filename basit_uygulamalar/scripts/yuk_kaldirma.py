#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 10:22:08 2022

@author: kutay
"""

import rospy
from std_msgs.msg import Bool

yukarda = None
class test():
    def __init__(self):
        rospy.init_node("yuk")
        rospy.Subscriber("yuk_deger",Bool,self.yukCallback)
        self.pub = rospy.Publisher("step_up",Bool,queue_size=1)
        self.yon = Bool()
        self.yon1 = Bool()
        self.pub1 = rospy.Publisher("step_down",Bool,queue_size=1)
        rospy.spin()
    def yukCallback(self,mesaj):
        if mesaj.data == True:
            self.yon.data = True
            self.yon1.data = False
            self.pub.publish(self.yon1)
            self.pub1.publish(self.yon)
        else:
            self.yon.data = False
            self.yon1.data = True
            self.pub.publish(self.yon1)
            self.pub1.publish(self.yon)
            
test()