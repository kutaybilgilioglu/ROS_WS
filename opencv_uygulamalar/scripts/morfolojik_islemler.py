#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 12:31:08 2022

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
        img = self.bridge.imgmsg_to_cv2(mesaj,"mono8")
        ret,esiklenmis = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
        kernel = np.ones((11,11),np.uint8)
        e_img = cv2.erode(esiklenmis,kernel)
        d_img = cv2.dilate(esiklenmis,kernel)
        f_img = d_img - e_img
        o_img = cv2.morphologyEx(esiklenmis,cv2.MORPH_OPEN,kernel)
        c_img = cv2.morphologyEx(esiklenmis,cv2.MORPH_CLOSE,kernel)
        cv2.imshow("opening",o_img)
        cv2.imshow("closing",c_img)
        cv2.imshow("esiklenmis",esiklenmis)
        cv2.imshow("erosion",e_img)
        cv2.imshow("dilate",d_img)
        cv2.imshow("morfoloji",f_img)
        cv2.imshow("Robot Kamerasi",img)
        
       
        cv2.waitKey(1)
        
Kamera()