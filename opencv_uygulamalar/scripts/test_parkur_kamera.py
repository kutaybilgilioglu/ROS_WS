#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 06:26:41 2022

@author: kutay
"""

import rospy
import math
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2
import numpy as np
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray,Bool
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion


sol_qtr = 0
sag_qtr = 0
durum = 0
hedef_x = 0
hedef_y = 0
konum_x = 0
konum_y = 0
angle = 0
fake_angle = 0
x_eslesti = False
donus = False
saga_don = False
sola_don = False
target = 0
target_set = False
ilk_iki = False
qtr_orta = 0
class bos_tur():
    def __init__(self):
         rospy.init_node("serit_takip1")
         self.bridge = CvBridge()
         rospy.Subscriber("usb_cam/image_raw/compressed",CompressedImage,self.kameraCallback)
         self.pub = rospy.Publisher("cmd_vel",Twist,queue_size = 10)
         rospy.Subscriber("odom",Odometry,self.odom_callback)
         rospy.Subscriber("qtr",Float64MultiArray,self.qtr_callback)
         rospy.Subscriber("rota_m",Float64MultiArray,self.rota_callback)
         rospy.Subscriber("odom1",Odometry,self.odom1_callback)
         rospy.Subscriber("ilk_iki",Bool,self.ilk_iki)
         self.hiz_mesaji = Twist()
         rospy.spin()
    def ilk_iki(self,mesaj):
        global ilk_iki
        ilk_iki = mesaj.data
    def odom_callback(self,mesaj):
        global angle
        orientation_q = mesaj.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
        angle= yaw*(180/np.pi)
        if angle < 0:
            angle = angle + 360
    def odom1_callback(self,mesaj):
        global konum_x,konum_y,fake_angle
        konum_x = mesaj.pose.pose.position.x*1000
        konum_y = mesaj.pose.pose.position.y*1000
        
        orientation_q = mesaj.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
        fake_angle= yaw*(180/np.pi)
        if fake_angle < 0:
            fake_angle = fake_angle + 360
    def rota_callback(self,mesaj):#bir sonraki qr konum
        global hedef_x,hedef_y,hedef_aci
        hedef_x = mesaj.data[0]
        hedef_y = mesaj.data[1]
        
        
    def qtr_callback(self,mesaj):
        global sol_qtr,sag_qtr,qtr_orta
        sol_qtr = mesaj.data[0]
        sag_qtr = mesaj.data[1]
        qtr_orta = mesaj.data[2]
        


     
    
         
         
    def kameraCallback(self,mesaj):
        global yol_sagda_mi,yol_solda_mi
        global yol_ayri_mi
        global donus,angle,target_set,turn,target,konum_x,konum_y,fark_gidildi
        global sag_qtr,sol_qtr,qtr_orta
        global durum,hedef_x,hedef_y,fake_angle,saga_don,sola_don
        img =  self.bridge.compressed_imgmsg_to_cv2(mesaj,"mono8")
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
        ret, takip1 = cv2.threshold(takip,95,255,cv2.THRESH_BINARY)
        kernel = np.ones((1,1), np.uint8)
 

        
        
        takip = cv2.Canny(takip1,100,230)
        takip = cv2.erode(takip, kernel, iterations=1)
        takip = cv2.dilate(takip, kernel, iterations=1)
        
        
        ret, yol_ayrimi = cv2.threshold(yol_ayrimi,95,255,cv2.THRESH_BINARY)
        yol_ayrimi = cv2.Canny(yol_ayrimi,100,230)
        
        
        
#        kernel = np.ones((2, 2), np.uint8)
# 
#
 #       yol_ayrimi = cv2.erode(yol_ayrimi, kernel, iterations=1)
#        yol_ayrimi = cv2.dilate(yol_ayrimi, kernel, iterations=1)
        karsilastirma = takip[80][0]
        count = 0
        for i in range(1,480):
            if karsilastirma != takip[80][i]:
                karsilastirma = takip[80][i]
                count+=1
         
        if sag_qtr>970 and sol_qtr<970 and qtr_orta>3000 and qtr_orta<12000:
            if count >=4:
                durum = 3
                
            else:
                durum = 1
                
        elif sag_qtr<970 and sol_qtr>970 and qtr_orta>3000 and qtr_orta<12000:
            if count >=4:
                durum = 4
                
            else:
                durum = 2
                
        elif sag_qtr>970 and sol_qtr>970 and qtr_orta>3000 and qtr_orta<12000: 
            durum = 5
        else:
            durum = 0
            
        if durum == 5 and donus ==False:
            if fake_angle==90:
                if hedef_x - konum_x < 0:
                    donus = True
                    saga_don = True
                    sola_don = False
                else:
                    donus = True
                    sola_don = True
                    saga_don = False
            elif fake_angle == 270:
                if hedef_x - konum_x < 0:
                    donus = True
                    sola_don = True
                    saga_don = False
                else:
                    donus = True
                    saga_don = True
                    sola_don = False
        elif durum == 4 and donus == False:
            if abs(hedef_x-konum_x)<150:
                donus = True
                sola_don = True
                saga_don = False
            else:
                donus = False
        elif durum == 3 and donus == False:
            if abs(hedef_x-konum_x)<150:
                donus = True
                saga_don = True
                sola_don = False
            else:
                donus = False
        elif durum == 2 and donus == False:
            donus = True
            sola_don = True
            saga_don = False
        elif durum == 1 and donus == False:
            donus = True
            saga_don = True
            sola_don = False
        elif donus == False and durum ==0: 
            
            saga_don = False
            sola_don = False
        
        
        rospy.loginfo("sag:%d sol:%d donus:%d durum:%d target:%d  angle:%d hedef:%d konum:%d"%(saga_don,sola_don,donus,durum,target,angle,hedef_x,konum_x))
        if donus:
            if saga_don == True and sola_don == False:
                    if target_set==False:
                        target = angle + 80
                        if target >= 360:
                            target = target-360
                        target_set=True
                    else:
                        if abs(target-angle)<2:
                            donus=False
                            target_set=False
                            
                    self.hiz_mesaji.linear.x = 0.0
                    self.hiz_mesaji.angular.z = -0.6
                    self.pub.publish(self.hiz_mesaji)
                    print("saga donus")
                      
                    
                   
            elif sola_don == True and saga_don == False:
                    if target_set==False:    
                        target = angle - 80
                        if target < 0:
                            target = target+360
                        target_set=True
                    else:
                        if abs(target-angle)<2:
                            donus=False
                            
                            target_set=False
                    self.hiz_mesaji.linear.x = 0.0
                    self.hiz_mesaji.angular.z = 0.6
                    self.pub.publish(self.hiz_mesaji)
            
            
        else:
            if ilk_iki == False:
                M = cv2.moments(takip)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.circle(takip,(cx,cy),5,(255,255,255),-1)
                sapma = cx - 640/2
#                self.hiz_mesaji.linear.x = 0.0
#                self.hiz_mesaji.angular.z = 0.0
#                self.pub.publish(self.hiz_mesaji)
            else:
                M = cv2.moments(takip)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.circle(takip,(cx,cy),5,(255,255,255),-1)
                sapma = cx - 640/2
                self.hiz_mesaji.linear.x = 0.4
                self.hiz_mesaji.angular.z = -sapma/200
                self.pub.publish(self.hiz_mesaji)
                
                
            
          
        
                
        
 
 
       
        
        
        
        
        
        cv2.imshow("norm",img)
        cv2.imshow("takip",takip)
        cv2.imshow("yol_ayrimi",takip1)
        cv2.waitKey(1)
bos_tur()