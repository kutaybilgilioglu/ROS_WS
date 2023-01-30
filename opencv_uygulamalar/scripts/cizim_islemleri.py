#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 01:34:15 2022

@author: kutay
"""

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class Kamera():
    def __init__(self):
        rospy.init_node("kamera_dugumu")
        self.bridge = CvBridge()
        rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        rospy.spin()
        
    def kameraCallback(self,mesaj):
        img = self.bridge.imgmsg_to_cv2(mesaj,"bgr8")
        cv2.line(img,(0,0),(250,250),(255,0,0),5)
        cv2.rectangle(img,(250,175),(500,125),(123,23,200),3)
        cv2.circle(img,(100,100),10,(0,0,255),-1)
        cv2.putText(img,"ros",(0,150),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
        cv2.imshow("Robot Kamerasi",img)
        
       
        cv2.waitKey(1)
        
Kamera()