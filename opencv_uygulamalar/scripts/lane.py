#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 23:21:57 2022

@author: kutay
"""

import cv2 
import numpy as np
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge

#sari = np.uint8([[[0,255,255]]])
#hsv = cv2.cvtColor(sari,cv2.COLOR_BGR2HSV
class SeritTakip():
    def __init__(self):
        rospy.init_node("serit_takip")
        self.bridge = CvBridge()
        rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        self.pub = rospy.Publisher("cmd_vel",Twist,queue_size = 10)
        self.hiz_mesaji = Twist()
        rospy.spin()
    def kameraCallback(self,mesaj):
        img = self.bridge.imgmsg_to_cv2(mesaj,"mono8")
        gaus = cv2.GaussianBlur(img,(5,5),0,cv2.BORDER_DEFAULT)
        edge = cv2.Canny(gaus,100,200)
        h,w = img.shape
        
        triangle = np.array([[(100,480),(600,480),(300,100)]])
        mask = np.zeros_like(edge)
        mask = cv2.fillPoly(mask,triangle,255)
        mask = cv2.bitwise_and(edge,mask)
        #cv2.polylines(mask,triangle,True,(255,0,0),2)
        linesP = cv2.HoughLinesP(mask,1,np.pi/180,50,None,20,10)
        #for i in range(0, len(linesP)):
        #   l = linesP[i][0]
        #   cv2.line(mask,(l[0],l[1]),(l[2],l[3]),(255,0,0),3)
        #mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
        left = []
        right = []
        for line in linesP:
            x1,y1,x2,y2 = line.reshape(4)
            parameters = np.polyfit((x1,x2),(y1,y2),1)
            slope = parameters[0]
            y_int = parameters[1]
            if slope < 0:
                left.append((slope,y_int))
            else:
                right.append((slope,y_int))
        right_avg = np.average(right,axis=0)
        left_avg = np.average(left,axis=0)
        left_line = make_points(mask,left_avg)
        right_line = make_points(mask,right_avg)
        final_line = np.array([left_line,right_line])
        tmp = np.zeros_like(img)
        for line in final_line:
            x1,y1,x2,y2 = line
            cv2.line(tmp,(x1,y1),(x2,y2),(255,0,0),5)
        M = cv2.moments(tmp)
        if M['m00'] > 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(img,(cx,cy),5,(255,0,0),-1)
            sapma = cx - w/2
            self.hiz_mesaji.linear.x = 0.2
            self.hiz_mesaji.angular.z = -sapma/100
            self.pub.publish(self.hiz_mesaji)
        else:
            self.hiz_mesaji.linear.x = 0.0
            self.hiz_mesaji.angular.z = 0.0
            self.pub.publish(self.hiz_mesaji)
            
        cv2.imshow("orijinal",img)
        cv2.imshow("blur",gaus)
        cv2.imshow("edge",edge)
        cv2.imshow("mask",mask)
        cv2.imshow("tmp",tmp)
        cv2.waitKey(1)
        
def make_points(image, average): 
    slope, y_int = average 
    y1 = image.shape[0]
    y2 = int(y1 * (3/5))
    x1 = int((y1 - y_int) / slope)
    x2 = int((y2 - y_int) / slope)
    return np.array([x1, y1, x2, y2])
        
SeritTakip()