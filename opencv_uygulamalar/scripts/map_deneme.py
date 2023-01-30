#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 04:27:37 2022

@author: kutay
"""
import rospy
from nav_msgs.msg import OccupancyGrid
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import math
from std_msgs.msg import Int32MultiArray

def _color_converter(value):
    if value == -1:
        return 0xcd / 0xff
    return (100 - value) / 100.0

class mapping():
    def __init__(self):
        rospy.init_node("mapping")
        self.bridge = CvBridge()
        
        #rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        self.pub = rospy.Publisher("map_arayuz1",Int32MultiArray,queue_size=10)
        rospy.Subscriber("map",OccupancyGrid,self.mapCallback,queue_size=1)
        rospy.spin()
        
    def mapCallback(self,mesaj):
        
        np_data = np.array([_color_converter(e) for e in mesaj.data])

        reshaped = np.flipud(np.reshape(np_data, (mesaj.info.height, mesaj.info.width)))
        for i in range(0,len(reshaped)):
            for j in range(0,len(reshaped)):
                reshaped[i][j] = round(reshaped[i][j]*255)
        width = int(reshaped.shape[1]*150/100)
        height = int(reshaped.shape[0]*150/100)
        dim = (width,height)
        reshaped=cv2.resize(reshaped,dim,interpolation = cv2.INTER_AREA)
        reshaped = cv2.rotate(reshaped,cv2.ROTATE_90_COUNTERCLOCKWISE)
        
        result = reshaped.astype(int)
        
        result = tuple([tuple(e) for e in result])
        msg = Int32MultiArray()
        msg.data = result
        for i in mesaj.data:
            if mesaj.data[i] != -1:
                print(mesaj.data[i])
            
            
        #self.pub.publish(msg)
        
        
        
        
                
        cv2.imshow("self updating mapping",reshaped)
        
        cv2.waitKey(1)
            
        
    
        
mapping()

