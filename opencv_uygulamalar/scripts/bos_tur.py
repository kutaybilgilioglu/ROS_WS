#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 17:12:44 2022

@author: kutay
"""

import rospy
import math
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2
import numpy as np
from geometry_msgs.msg import Twist
#from std_msgs.msg import Float64MultiArray
from tf.transformations import euler_from_quaternion
from nav_msgs.msg import Odometry

yol_sagda_mi = False
yol_ayri_mi = False
donus = False
rderece = 0
target = 0
konum_x = 0
konum_y = 0
h_konum_x = 0
h_konum_y = 0
turn = False
target_set = False
fark_gidildi = False
class bos_tur():
    def __init__(self):
         rospy.init_node("serit_takip")
         self.bridge = CvBridge()
         rospy.Subscriber("usb_cam/image_raw/compressed",CompressedImage,self.kameraCallback)
         self.pub = rospy.Publisher("cmd_vel",Twist,queue_size = 10)
         rospy.Subscriber("odom",Odometry,self.odomCallback)
         #rospy.Subscriber("qtr",Float64MultiArray,self.qtr_callback)
        
         self.hiz_mesaji = Twist()
         rospy.spin()
    
    #def qtr_callback(self,mesaj):
        


     
    def odomCallback(self,mesaj):
        global rderece,konum_x,konum_y
        orientation_q = mesaj.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
        rderece= yaw*(180/np.pi)
        if rderece < 0:
            rderece = rderece+360
        konum_x = mesaj.pose.pose.position.x
        konum_y = mesaj.pose.pose.position.y
        
         
         
    def kameraCallback(self,mesaj):
        global yol_sagda_mi
        global yol_ayri_mi
        global donus,rderece,target_set,turn,target,konum_x,konum_y,h_konum_x,h_konum_y,fark_gidildi
        img =  self.bridge.compressed_imgmsg_to_cv2(mesaj,"mono8")
        img = cv2.blur(img,(20,20))
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
        ret, takip1 = cv2.threshold(takip,80,255,cv2.THRESH_BINARY)
        kernel = np.ones((1,1), np.uint8)
 

        
        
        takip = cv2.Canny(takip1,100,230)
        takip = cv2.erode(takip, kernel, iterations=1)
        takip = cv2.dilate(takip, kernel, iterations=1)
        
        
        ret, yol_ayrimi = cv2.threshold(yol_ayrimi,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #yol_ayrimi = cv2.Canny(yol_ayrimi,100,230)
        
        
        
#        kernel = np.ones((2, 2), np.uint8)
# 
#
#        yol_ayrimi = cv2.erode(yol_ayrimi, kernel, iterations=1)
#        yol_ayrimi = cv2.dilate(yol_ayrimi, kernel, iterations=1)
        
        
        
        
        karsilastirma = takip[0][30]
        karsilastirma1 = takip[0][600]
        count = 0
        count1 = 0
        for i in range(1,480):
            if takip[i][30] != karsilastirma:
                count+=1
                karsilastirma = takip[i][30]
            if takip[i][600] != karsilastirma1:
                count1+=1
                karsilastirma1 = takip[i][600]
        if (count >= 4 or count1 >=4) and turn==False:
            yol_ayri_mi = True
            if count > count1:
                yol_sagda_mi = False
            else:
                yol_sagda_mi = True
        else:
            yol_ayri_mi = False
        karsilastirma = takip[470][0]
        karsilastirma1 = takip[50][0]
        count = 0
        count1 = 0
        for i in range(1,640):
            if takip[470][i] != karsilastirma:
                count+=1
            if takip[50][i] != karsilastirma1:
                count+=1
        if count == 0 and count1 == 0:
            donus = True
        else:
            donus = False
        #rospy.loginfo("yol: %d sagda:%d"%(donus,yol_sagda_mi))
        if turn:
            if yol_sagda_mi and fark_gidildi:
                    if target_set==False:
                        target = rderece + 85
                        if target >= 360:
                            target = target-360
                        target_set=True
                    else:
                        if abs(target-rderece)<2:
                            turn=False
                            target_set=False
                            fark_gidildi = False
                            #donus = False
                    self.hiz_mesaji.linear.x = 0.0
                    self.hiz_mesaji.angular.z = -1.0
                    self.pub.publish(self.hiz_mesaji)
            
                      
                    
                   
            elif yol_sagda_mi==False and fark_gidildi:
                    if target_set==False:    
                        target = rderece - 85
                        if target < 0:
                            target = target+360
                        target_set=True
                    else:
                        if abs(target-rderece)<2:
                            print("turn")
                            turn=False
                            fark_gidildi = False
                            #donus = False
                            target_set=False
                    self.hiz_mesaji.linear.x = 0.0
                    self.hiz_mesaji.angular.z = 1.0
                    self.pub.publish(self.hiz_mesaji)
            else:
                  self.hiz_mesaji.linear.x = 0.4
                  self.hiz_mesaji.angular.z=0.0
                  a = math.sqrt((konum_x-h_konum_x)**2+(konum_y-h_konum_y)**2)
                  print(a)
                  if a >0.63:
                      fark_gidildi = True
                      print("gidildi")
            #rospy.loginfo("target_d: %f  rderece: %f"%(target,rderece))
            #rospy.loginfo(fark_gidildi)
            
        else:
            if donus == False:
                M = cv2.moments(takip)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.circle(takip,(cx,cy),5,(255,255,255),-1)
                sapma = cx - 640/2
                self.hiz_mesaji.linear.x = 0.4
                self.hiz_mesaji.angular.z = -sapma/250
                self.pub.publish(self.hiz_mesaji)
            else:
                turn = True
                fark_gidildi = False
                h_konum_x = konum_x
                h_konum_y = konum_y
        rospy.loginfo("target: %d donus: %d  target_d: %d  rderece: %d  turn: %d"%(target_set,donus,target,rderece,turn))
        
          
            
        
        
        cv2.imshow("norm",img)
        cv2.imshow("takip",takip)
        cv2.imshow("yol_ayrimi",takip1)
        cv2.waitKey(1)
bos_tur()