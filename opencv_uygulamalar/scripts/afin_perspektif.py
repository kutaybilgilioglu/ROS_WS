#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:10:50 2022

@author: kutay
"""
import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CompressedImage
import numpy as np
class Kamera():
    def __init__(self):
        rospy.init_node("kamera_dugumu")
        self.bridge = CvBridge()
        rospy.Subscriber("raspicam_node/image/compressed",CompressedImage,self.kameraCallback)
        rospy.spin()
        
    def kameraCallback(self,mesaj):
        img = self.bridge.compressed_imgmsg_to_cv2(mesaj,"bgr8")
        #k1 = np.float32([[30,500],[200,500],[30,600]])
        #k2 = np.float32([[15,500],[100,500],[15,600]])
        #M = cv2.getAffineTransform(k1,k2)
        #affin = cv2.warpAffine(img,M,(640,480))'''
        img = cv2.resize(img,(1280,960),interpolation=cv2.INTER_AREA)
        cv2.imshow("Robot Kamerasi",img)
        #cv2.imshow("afin",affin)
        #k1 = np.float32([[5,250],[605,250],[5,400],[605,400]])
        #k2 = np.float32([[0,0],[640,0],[0,480],[640,480]])
        #M = cv2.getPerspectiveTransform(k1,k2)
        #perspektif = cv2.warpPerspective(img,M,(640,480))
        #cv2.imshow("perspektif",perspektif)
       
        cv2.waitKey(1)
        
Kamera()
