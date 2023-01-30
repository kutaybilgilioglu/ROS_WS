#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 22:12:10 2022

@author: kutay
"""

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist
class buzzer():
    def __init__(self):
        rospy.init_node("buzzer1")
        self.pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
        self.hiz = Twist()
        self.pub1 = rospy.Publisher("buzzer",Bool,queue_size=1)
        self.buzzer = Bool()
        rospy.Subscriber("scan",LaserScan,self.lazerCall)
        rospy.spin()
    def lazerCall(self,mesaj):
        if mesaj.ranges[0]<1.5:
            self.hiz.linear.x = 0.0
            self.pub.publish(self.hiz)
            self.buzzer.data = True
            self.pub1.publish(self.buzzer)
        else:
            self.hiz.linear.x = 0.3
            self.pub.publish(self.hiz)
            self.buzzer.data = False
            self.pub1.publish(self.buzzer)
            
buzzer()
            