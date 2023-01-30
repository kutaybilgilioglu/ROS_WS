#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 03:36:49 2022

@author: kutay
"""

import rospy
from std_msgs.msg import Bool
once1 = False
once2 = False

class test():
    def __init__(self):
        global once1
        rospy.init_node("uno_pub")
        self.pub1 = rospy.Publisher("step_up",Bool,queue_size=1)
        self.pub2 = rospy.Publisher("step_down",Bool,queue_size=1)
        self.msg = Bool()
        if once1 == False:
            self.msg.data = True
            self.pub1.publish(self.msg)
            once1 = True
        rospy.spin()
        
        
test()