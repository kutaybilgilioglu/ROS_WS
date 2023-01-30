#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 17:30:25 2022

@author: kutay
"""

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry
class init_pose():
    def __init__(self):
        rospy.init_node("init_pub")
        rospy.Subscriber("odom",Odometry,self.callback)
        self.pub = rospy.Publisher("initialpose",PoseWithCovarianceStamped)
        self.msg = PoseWithCovarianceStamped()
        rospy.spin()
    def callback(self,mesaj):
        
        self.msg.pose.pose.position.x = mesaj.pose.pose.position.x
        self.msg.pose.pose.position.y = mesaj.pose.pose.position.y
        self.msg.pose.pose.position.z = mesaj.pose.pose.position.z
        self.msg.pose.pose.orientation.x = mesaj.pose.pose.orientation.x
        self.msg.pose.pose.orientation.y = mesaj.pose.pose.orientation.y
        self.msg.pose.pose.orientation.z = mesaj.pose.pose.orientation.z
        self.msg.pose.pose.orientation.w = mesaj.pose.pose.orientation.w
        self.msg.pose.covariance = mesaj.pose.covariance
        self.pub.publish(self.msg)
init_pose()