#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:58:47 2022

@author: kutay
"""

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import numpy as np
class Kamera():
    def __init__(self):
        rospy.init_node("kamera_dugumu")
        self.bridge = CvBridge()
        rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        rospy.spin()
        
    def kameraCallback(self,mesaj):
        img = self.bridge.imgmsg_to_cv2(mesaj,"bgr8")
        olceklenmis = cv2.resize(img,(100,100))
        M = np.float32([[1,0,50],[0,1,200]])
        otelenmis = cv2.warpAffine(img,M,(640,480))
        N = cv2.getRotationMatrix2D((320,240),90,1)
        dondurulmus = cv2.warpAffine(img,N,(640,480))
        
        cv2.imshow("olceklenmis",olceklenmis)
        cv2.imshow("otelenmis",otelenmis)
        cv2.imshow("dondurulmus",dondurulmus)
        cv2.imshow("Robot Kamerasi",img)
        
       
        cv2.waitKey(1)
        
Kamera()