#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 17:37:03 2022

@author: kutay
"""

import rospy
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2
import numpy as np
from geometry_msgs.msg import Twist
yol_sagda_mi = False
yol_ayri_mi = False
donus = False
class bos_tur():
    def __init__(self):
         rospy.init_node("serit_takip")
         self.bridge = CvBridge()
         rospy.Subscriber("usb_cam/image_raw/compressed",CompressedImage,self.kameraCallback)
         self.pub = rospy.Publisher("cmd_vel",Twist,queue_size = 10)
         
        
         self.hiz_mesaji = Twist()
         rospy.spin()
    def kameraCallback(self,mesaj):
        global yol_sagda_mi
        global yol_ayri_mi
        global donus
        img =  self.bridge.compressed_imgmsg_to_cv2(mesaj,"mono8")
#        pts1 = np.float32([[150,350],[490,350],[0,480],[640,480]])
## Size of the Transformed Image
#        pts2 = np.float32([[0,0],[640,0],[0,480],[640,480]])
#        M = cv2.getPerspectiveTransform(pts1,pts2)
#        takip = cv2.warpPerspective(img,M,(640,480))
#        pts1 = np.float32([[0,280],[640,280],[0,350],[640,350]])
## Size of the Transformed Image1
#        pts2 = np.float32([[0,0],[640,0],[0,480],[640,480]])
#        M = cv2.getPerspectiveTransform(pts1,pts2)
#        yol_ayrimi = cv2.warpPerspective(img,M,(640,480))
        ret, takip = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        takip = cv2.Canny(takip,100,230)
        
      
        
        
        
            
          
            
        
        
        
        cv2.imshow("takip",takip)
        cv2.imshow("yol_ayrimi",img)
        cv2.waitKey(1)
bos_tur()