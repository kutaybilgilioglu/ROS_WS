#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 00:24:50 2022

@author: kutay
"""

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import numpy as np
once = True
class Kamera():
    def __init__(self):
        rospy.init_node("kamera_dugumu")
        self.bridge = CvBridge()
        rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        rospy.spin()
        
    def kameraCallback(self,mesaj):
        global once
        img = self.bridge.imgmsg_to_cv2(mesaj,"mono8")
        rows = img.shape[0]
        
        edges = cv2.Canny(img, 50, 150, apertureSize=3)
        (thresh, im_bw) = cv2.threshold(edges, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        lines = cv2.HoughLines(im_bw, 1, np.pi/360, 90,None,0,0)
            # Specify size on vertical axis
        line = np.array([])
        line = np.hstack((line,np.array([0,0,0,0,0,0])))
        #rospy.loginfo(lines)
        img2 = np.zeros_like(img)
        for r_theta in lines:

            arr = np.array(r_theta[0], dtype=np.float64)
            r, theta = arr
    		# Stores the value of cos(theta) in a
            a = np.cos(theta)
            b = np.sin(theta)
       	 	
    		
 
    		# x0 stores the value rcos(theta)
            x0 = a*r
    		
 
    		# y0 stores the value rsin(theta)
            y0 = b*r
    		
 
    		# x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
            x1 = x0 + 1000*(-b)
    		
 
    		# y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
            y1 = y0 + 1000*(a)
    		
 
    		# x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
            x2 = x0 - 1000*(-b)
    		
 
    		# y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
            y2 = y0 - 1000*(a)
    		
 
    		# cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
    		# (0,0,255) denotes the colour of the line to be
    		# drawn. In this case, it is red.
            m = ((y2-y1)/(x2-x1))
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)
            
            angle = (np.arctan(m)*(180/np.pi))
            angle = abs(angle)
            #rospy.loginfo(type(angle))
            #rospy.loginfo("y2:%d y1:%d x2:%d x1%d angle: %f m:%f"%(y2,y1,x2,x1,angle,m))
            #m = (y2-y1)/(x2-x1)
            #y2 = 230
            #x2 = int((y2-y1+m*x1)/m)
            
            if angle >20 and angle < 180:
                line = np.vstack((line,np.array([x1,y1,x2,y2,angle,m])))
                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)      
            
        
        
        
        
        for i in range(0,len(line)-1):
            bottom_x1 = (480-line[i][1]+line[i][5]*line[i][0])
            bottom_x2 = (480-line[i+1][1]+line[i+1][5]*line[i+1][0])
            
            if line[i][5]*line[i+1][5] <0 or abs(bottom_x1-bottom_x2)>100:
                kesisim_x = int(((line[i][5]*line[i][0]-line[i][1]-line[i+1][5]*line[i+1][0]+line[i+1][1])/(line[i][5]-line[i+1][5])))
                kesisim_y = int((line[i][5]*kesisim_x - line[i][5]*line[i][0] + line[i][1]))
                if kesisim_x>30 and kesisim_x<610 and kesisim_y>15 and kesisim_y<465:
                    break
                
        
        line = line.astype(int)
        rospy.loginfo("%d   %d"%(kesisim_x,kesisim_y))
        for i in range(0,len(line)-1):
            if line[i][5]<0:
                cv2.line(img2, (kesisim_x,kesisim_y), (line[i][0], line[i][1]), (255, 255, 255), 2)
            else:
                cv2.line(img2, (kesisim_x,kesisim_y), (line[i][2], line[i][3]), (255, 255, 255), 2)
        #for i in range(0,len(line)-1):
            #cv2.line(img, (line[i][0], line[i][1]), (kesisim_x, kesisim_y), (0, 0, 255), 2)
#        #cv2.line(img, (-919, -407), (812, 592), (0, 0, 255), 2)
#        #cv2.circle(img,(0,240),3,(0,0,255),1)
#        if once == True:
#            once = False
#            for x in line:
#                #rospy.loginfo(x)
#                once=True
            
        sag_dortgen = np.array([[(0,kesisim_y),(640,kesisim_y),(640,0),(0,0)]])
        img2 = cv2.fillPoly(img2,sag_dortgen,0)
        img2 = cv2.bitwise_and(img2,img2)
           
                
                
            
        
        
        
        verticalsize = rows // 30
        M = cv2.moments(img2)
        if M['m00']!=0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(img,(cx,cy),5,(255,255,255),-1)  
        
        # Create structure element for extracting vertical lines through morphology operations
        verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))
        # Apply morphology operations
        #img = cv2.erode(img, verticalStructure)
        #img = cv2.dilate(img, verticalStructure)
        cv2.imshow('linesDetected', img)
        cv2.imshow("canny",img2)
        cv2.imshow("binary",im_bw)

        
        cv2.waitKey(1)
        
Kamera()
