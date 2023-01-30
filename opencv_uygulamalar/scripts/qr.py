#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 14:41:03 2022

@author: kutay
"""

import rospy 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from pyzbar.pyzbar import decode
import numpy as np
once = True
class test():
    def __init__(self):
        rospy.init_node("qr")
        rospy.Subscriber("camera/rgb/image_raw",Image,self.callback)
        self.bridge = CvBridge()
        self.detector = cv2.QRCodeDetector() 
        rospy.spin()
    def callback(self,mesaj):
        global once
        img = self.bridge.imgmsg_to_cv2(mesaj,"mono8")
        img = cv2.GaussianBlur(img,(9,9),0,cv2.BORDER_DEFAULT)
        thresh = 80
        img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]
        pts1 = np.float32([[280,670],[1000,670],[30,900],[1250,900]])

        pts2 = np.float32([[0,0],[1280,0],[0,960],[1280,960]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        img2 = cv2.warpPerspective(img,M,(1280,960))
        img2 = cv2.resize(img2,(200,200),interpolation = cv2.INTER_AREA)
        data, bbox, _ = self.detector.detectAndDecode(img)
        if data:
            print(data)
        
    #print (qr_result)
        
#        qr_data = qr_result[0].data
#       
#
#        (x, y, w, h) = qr_result[0].rect
#        
#        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 4)
#        
#        text = "{}".format(qr_data)
#        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        if once == True:
            cv2.imwrite("gr.png",img2)
            once = False
    
    
        cv2.imshow("img",img)
        cv2.imshow("img2",img2)
        
        
        cv2.waitKey(1)
        
test()
        
