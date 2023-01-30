#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 23:33:00 2022

@author: kutay
"""

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage
from nav_msgs.msg import Odometry
import numpy as np
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
import time
roll = pitch = yaw = 0.0
durum = 0
ust = sag = sol = donus = False
start_time = time.time()

class test():
    def __init__(self):
        rospy.init_node("harita_tur")
        rospy.Subscriber("usb_cam/image_raw/compressed",CompressedImage,self.camcallback)
        rospy.Subscriber("odom",Odometry,self.odomcallback)
       
        self.pub = rospy.Publisher("cmd_vel",Twist,queue_size = 10)
        self.hiz_mesaji = Twist()
        self.bridge = CvBridge()
        rospy.spin()
    def camcallback(self,mesaj):
        global durum, start_time
        global ust, sag, sol, donus
        img = self.bridge.compressed_imgmsg_to_cv2(mesaj,"mono8")
        img = cv2.blur(img,(30,30))
        pts1 = np.float32([[150,350],[490,350],[0,480],[640,480]])
# Size of the Transformed Image
        pts2 = np.float32([[0,0],[640,0],[0,480],[640,480]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        takip = cv2.warpPerspective(img,M,(640,480))
        pts1 = np.float32([[0,280],[640,280],[0,350],[640,350]])
# Size of the Transformed Image1
        pts2 = np.float32([[0,0],[640,0],[0,480],[640,480]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        yol_ayrimi = cv2.warpPerspective(img,M,(640,480))
        ret, takip = cv2.threshold(takip,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        kernel = np.ones((1,1), np.uint8)
 

        
        
        takip = cv2.Canny(takip,100,230)
        takip = cv2.erode(takip, kernel, iterations=1)
        takip = cv2.dilate(takip, kernel, iterations=1)
        
        ret, yol_ayrimi = cv2.threshold(yol_ayrimi,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        yol_ayrimi = cv2.Canny(yol_ayrimi,100,230)
        karsilastirma = takip[0][600]
        karsilastirma1 = takip[0][30]
        count = count1 = count2  = 0
        for i in range(1,480):
            if karsilastirma != takip[i][600]:
                count+=1
            if karsilastirma1 != takip[i][30]:
                count1+=1
        if count>=2:
            sag = True
        else:
            sag = False
        if count1>=2:
            sol = True
        else:
            sol = False
        if sol and sag:
            durum = 3
        
        
        elif sol or sag:
            karsilastirma = takip[5][0]
            count2 = 0
            for i in range(1,640):
                if karsilastirma != takip[5][i]:
                    count2+=1
            if count2 >= 2 and sag:
                durum = 4
            elif count2 >=2 and sol:
                durum = 5
            elif sol and sag == False:
                durum = 2
            elif sag and sol == False:
                durum = 1
        else:
            durum = 0
        count = 0
        karsilastirma = takip[475][0]
        for i in range(1,640):
            if karsilastirma != takip[475][i]:
                count+=1
        
       
                
        if start_time == None and durum != 0:                
            donus = True
            start_time = time.time()
            
        else:
            current_time = time.time()
            elapsed = current_time - start_time
            if durum!=0 and elapsed > 10:
                donus = True
                start_time = time.time()
            else:
                donus = False
       
#            M = cv2.moments(takip)
#            cx = int(M['m10']/M['m00'])
#            cy = int(M['m01']/M['m00'])
#            cv2.circle(takip,(cx,cy),5,(255,255,255),-1)
#            sapma = cx - 640/2
#            self.hiz_mesaji.linear.x = 0.4
#            self.hiz_mesaji.angular.z = -sapma/100
#            self.pub.publish(self.hiz_mesaji)       
        
        
        cv2.imshow("blur",img)
        cv2.imshow("img",yol_ayrimi)
        cv2.imshow("img1",takip)
        cv2.waitKey(1)
    def odomcallback(self,mesaj):
        global roll, pitch, yaw
        orientation = mesaj.pose.pose.orientation
        (roll,pitch,yaw) = euler_from_quaternion((orientation.x,orientation.y,orientation.z,orientation.w))
        angle = yaw * 180/np.pi
        if angle < 0:
            angle = angle+360
        #rospy.loginfo("x:%f  y:%f   angle:%f "%(mesaj.pose.pose.position.x,mesaj.pose.pose.position.y,angle))
        
test()
        
        