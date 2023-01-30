#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 22:09:30 2022

@author: kutay
"""

import cv2
import numpy as np
#mavi = np.uint8([[[255,0,0]]])
#hsv = cv2.cvtColor(mavi,cv2.COLOR_BGR2HSV)
#print(hsv)
cap = cv2.VideoCapture(0)
while True:
    _,img = cap.read()
    img = cv2.resize(img,(640,480))
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    alt_mavi = np.array([110,100,100])
    ust_mavi = np.array([130,255,255])
    maske = cv2.inRange(hsv,alt_mavi,ust_mavi)
    sonuc = cv2.bitwise_and(img,img,mask=maske)
    cv2.imshow("orjinal",img)
    cv2.imshow("maske",maske)
    cv2.imshow("sonuc",sonuc)
    
    k = cv2.waitKey(1)
    if k == 27:
        break
    
cv2.destroyAllWindows()