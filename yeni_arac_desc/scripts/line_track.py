#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 06:26:41 2022

@author: kutay
"""

import rospy
import math
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray,Bool
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
class Run():
    def __init__(self):
        rospy.init_node("mover")
        self.bridge = CvBridge()
        rospy.Subscriber("camera/rgb/image_raw",Image,self.camCallback)
        self.pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
        self.hiz_mesaji = Twist()
        rospy.spin()
    def camCallback(self,mesaj):
        yol_durumu=0
        img = self.bridge.imgmsg_to_cv2(mesaj,"mono8")
        (thresh, img) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        img = cv2.Canny(img,60,200)
        M = cv2.moments(img)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.circle(img,(cx,cy),5,(255,255,255),-1)
        
        sol_count = 0
        sag_count=0
        sol_karsilastirma = img[0][50]
        sag_karsilastirma = img[0][590]
        for i in range(1,480):
            if sol_karsilastirma != img[i][50]:
                sol_count+=1
                sol_karsilastirma = img[i][50]
            if sag_karsilastirma != img[i][590]:
                sag_count+=1
                sag_karsilastirma != img[i][590]
       
        if sol_count >= 2 and sag_count>=2:
            rospy.loginfo("cift_ayrim")
        elif sag_count >=2 and sol_count<2:
            rospy.loginfo("sag_ayrim")
        elif sol_count>=2 and sag_count<2:
            rospy.loginfo("sol_ayrim")
        else:
            rospy.loginfo("ayrim_yok")
        sapma = cx - 640/2
        self.hiz_mesaji.linear.x = 0.4
        self.hiz_mesaji.angular.z = -sapma/200
        self.pub.publish(self.hiz_mesaji)
        cv2.imshow("canny",img)
        cv2.waitKey(1)
Run()