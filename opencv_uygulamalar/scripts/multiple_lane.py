#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:47:53 2022

@author: kutay
"""
import time
import cv2 
import numpy as np
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int64
import math
#480,640
#sari = np.uint8([[[0,255,255]]])
#hsv = cv2.cvtColor(sari,cv2.COLOR_BGR2HSV
yol_ayri_mi = False
saga_git = False
donus = False
tekrar = True
clock = False
engel = False
yol_sagda_mi = False
tick = True
tekrar_lazer = True
start_time = 0
beklendi = False
class SeritTakip():
    def __init__(self):
        
        rospy.init_node("serit_takip")
        self.bridge = CvBridge()
        rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        self.pub = rospy.Publisher("cmd_vel",Twist,queue_size = 10)
        rospy.Subscriber("scan",LaserScan,self.lazerCallback)
        self.time_pub = rospy.Publisher("engel_timer",Int64,queue_size=1)
        self.hiz_mesaji = Twist()
        rospy.spin()
    def lazerCallback(self,mesaj):
        global engel
        global clock
        global tick
        global start_time
        global tekrar_lazer
        global beklendi
        sol_on = list(mesaj.ranges[0:9])
        sag_on = list(mesaj.ranges[350:359])
        on = sol_on + sag_on
        sol = list(mesaj.ranges[80:100])
        sag = list(mesaj.ranges[260:280])
        arka = list(mesaj.ranges[170:190])
        if min(on)<2 and clock == False and tekrar_lazer:
            print("engelle karsilasildi. 15 saniye icinde engel cekilmezse alternatif rotadan ilerlenilecek")
            clock = True
            
        elif min(on)<2 and clock:
            current_time = time.time()
            elapsed = current_time - start_time
            time_msg = np.int64(elapsed)
            #print(type(time_msg))
            self.time_pub.publish(time_msg)
            
            
            if elapsed>15:
                clock = False
                tick = True
                beklendi = True
                tekrar_lazer = False
                print("15 saniye gecti alternatif rotadan gidiliyor...")
        elif min(on)>3.5 and clock:
            clock = False
            tick = True
            beklendi = False
            print("Engel yoldan cekildi. Planlanmıs rotadan devam ediliyor...")
        else:
            if yol_sagda_mi:
                saga_git = False
            else:
                saga_git = True
            
            
    def kameraCallback(self,mesaj):
        global start_time
        global yol_ayri_mi
        global saga_git
        global donus 
        global tekrar
        global clock
        global engel
        global yol_sagda_mi
        global tick
        global beklendi
        count = 0
        count2 = 0
        
        if clock and tick:
            tick = False
            start_time = time.time()
        
        img = self.bridge.imgmsg_to_cv2(mesaj,"mono8")
        pts1 = np.float32([[250,400],[390,400],[0,480],[640,480]])
# Size of the Transformed Image
        pts2 = np.float32([[0,0],[640,0],[0,480],[640,480]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        takip = cv2.warpPerspective(img,M,(640,480))
        pts1 = np.float32([[0,280],[640,280],[0,350],[640,350]])
# Size of the Transformed Image1
        pts2 = np.float32([[0,0],[640,0],[0,480],[640,480]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        yol_ayrimi = cv2.warpPerspective(img,M,(640,480))
        
       
        gaus = cv2.GaussianBlur(img,(5,5),0,cv2.BORDER_DEFAULT)
       
        ret, otsu = cv2.threshold(gaus,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        edge = cv2.Canny(otsu,100,230)
        
        ret, takip = cv2.threshold(takip,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        takip = cv2.Canny(takip,100,230)
        
        
        ret, yol_ayrimi = cv2.threshold(yol_ayrimi,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        yol_ayrimi = cv2.Canny(yol_ayrimi,100,230)
        
        sag_dortgen = np.array([[(320,480),(640,480),(640,0),(320,0)]])
        sol_dortgen = np.array([[(0,0),(320,0),(320,480),(0,480)]])
        
        sol_ust_maske = np.zeros_like(img)
        sol_ust_maske = cv2.fillPoly(sol_ust_maske,sol_dortgen,255)
        sol_ust_maske = cv2.bitwise_and(yol_ayrimi,sol_ust_maske)
        
        sag_ust_maske = np.zeros_like(img)
        sag_ust_maske = cv2.fillPoly(sag_ust_maske,sag_dortgen,255)
        sag_ust_maske = cv2.bitwise_and(yol_ayrimi,sag_ust_maske)
        
        
        sol_maske = np.zeros_like(img)
        sol_maske = cv2.fillPoly(sol_maske,sol_dortgen,255)
        sol_maske = cv2.bitwise_and(takip,sol_maske)
        
        sag_maske = np.zeros_like(img)
        sag_maske = cv2.fillPoly(sag_maske,sag_dortgen,255)
        sag_maske = cv2.bitwise_and(takip,sag_maske)
        
       
        karsilastirma = yol_ayrimi[0][0]
        karsilastirma1 = yol_ayrimi[10][0]
        karsilastirma2 = yol_ayrimi[20][0]
        karsilastirma3 = yol_ayrimi[30][0]
        karsilastirma4 = yol_ayrimi[40][0]
        karsilastirma5 = yol_ayrimi[280][0]
        karsilastirma6 = yol_ayrimi[350][0]
        karsilastirma7 = yol_ayrimi[420][0]
        count3 = 0
        count4 = 0
        count5 = 0
        count6 = 0
        count7 = 0
        count8 = 0
        count9 = 0
        for i in range(1,len(yol_ayrimi[0])):
            
            if karsilastirma != yol_ayrimi[0][i]:
                karsilastirma = yol_ayrimi[0][i]
                count+=1
            if karsilastirma1 != yol_ayrimi[10][i]:
                karsilastirma1 = yol_ayrimi[10][i]
                count3+=1
            if karsilastirma2 != yol_ayrimi[20][i]:
                karsilastirma2 = yol_ayrimi[20][i]
                count4+=1
            if karsilastirma3 != yol_ayrimi[30][i]:
                karsilastirma3 = yol_ayrimi[30][i]
                count5+=1
            if karsilastirma4 != yol_ayrimi[40][i]:
                karsilastirma4 = yol_ayrimi[40][i]
                count6+=1
            if karsilastirma5 != yol_ayrimi[280][i]:
                karsilastirma5 = yol_ayrimi[280][i]
                count7+=1
            if karsilastirma6 != yol_ayrimi[350][i]:
                karsilastirma6 = yol_ayrimi[350][i]
                count8+=1
            if karsilastirma7 != yol_ayrimi[420][i]:
                karsilastirma7 = yol_ayrimi[420][i]
                count9+=1
        count = round((count+count3+count4+count5+count6+count7+count8+count9)/8)        
                
                
        if count >= 5 :
            yol_ayri_mi = True
            
        else:
            yol_ayri_mi = False
            tekrar = True
            
#        if yol_ayri_mi and tekrar:
#            tekrar = False
#            self.hiz_mesaji.linear.x = 0
#            self.hiz_mesaji.angular.z = 0
#            self.pub.publish(self.hiz_mesaji)
#            print("yol ayrimi algilandi: sola gitmek icin 1, saga gitmek icin 2 tusuna basiniz\n")
#            secim = int(input())
#            if secim == 1:
#                saga_git = False
#            else:
#                saga_git = True
              
        karsilastirma = takip[50][0]
        karsilastirma1 = takip[100][0]
        karsilastirma2 = takip[150][0]
        karsilastirma3 = takip[200][0]
        karsilastirma4 = takip[250][0]
        count3 = 0
        count4 = 0
        count5 = 0
        count6 = 0
        for i in range(1,len(takip[250])):
            
            if karsilastirma4 != takip[250][i]:
                
                karsilastirma4 = takip[250][i]
                count6+=1
            if karsilastirma3 != takip[200][i]:
                
                karsilastirma3 = takip[200][i]
                count5+=1
            if karsilastirma2 != takip[150][i]:
                
                karsilastirma2 = takip[150][i]
                count4+=1
            if karsilastirma1 != takip[100][i]:
                
                karsilastirma1 = takip[100][i]
                count3+=1
            if karsilastirma != takip[50][i]:
                
                karsilastirma = takip[50][i]
                count2+=1
        count2 = round((count2+count3+count4+count5+count6)/5)
        #print("{}   {}     {}   {}".format(count2,count,yol_ayri_mi,len(takip)))
        
        karsilastirma = yol_ayrimi[0][50]
        karsilastirma1 = yol_ayrimi[0][590]
        count = 0
        count1 = 0
        
        for i in range(1,len(yol_ayrimi)):
            if karsilastirma != yol_ayrimi[i][50]:
                count+=1
                karsilastirma = yol_ayrimi[i][50]
            if karsilastirma1 != yol_ayrimi[i][590]:
                count1+=1
                karsilastirma1 = yol_ayrimi[i][590]
                
        if count>0:
            yol_sagda_mi = False
        elif count1>0:
            yol_sagda_mi = True
        if beklendi:
            if yol_sagda_mi:
                saga_git = True
            else:
                saga_git = False
                
        else:
            if yol_sagda_mi:
                saga_git = False
            else:
                saga_git = True
            
       
            
        
        
        if count2 >=5 and saga_git:
             
             M = cv2.moments(sag_maske)
#             if M['m00'] <= 0.1 and M['m00'] >=-0.1:
#                 M['m00'] = 0.001
             cx = int(M['m10']/M['m00'])
             cy = int(M['m01']/M['m00'])
             cv2.circle(takip,(cx,cy),5,(255,255,255),-1)
             time.sleep(0.1)
        elif count2>=5 and saga_git == False:
             M = cv2.moments(sol_maske)
#             if M['m00'] <= 0.1 and M['m00'] >=-0.1:
#                 M['m00'] = 0.001
             cx = int(M['m10']/M['m00'])
             cy = int(M['m01']/M['m00'])
             cv2.circle(takip,(cx,cy),5,(255,255,255),-1)
#             print("sola gidis\n")
             time.sleep(0.1)
        
            
        else:
             M = cv2.moments(takip)
#             if M['m00'] <= 0.1 and M['m00'] >=-0.1:
#                 M['m00'] = 0.001
             cx = int(M['m10']/M['m00'])
             cy = int(M['m01']/M['m00'])
             cv2.circle(takip,(cx,cy),5,(255,255,255),-1)
        
        if clock:
            self.hiz_mesaji.linear.x = 0
            self.hiz_mesaji.angular.z = 0
            self.pub.publish(self.hiz_mesaji)
        else:
            sapma = cx - 640/2
            self.hiz_mesaji.linear.x = 0.1
            self.hiz_mesaji.angular.z = -sapma/150
            self.pub.publish(self.hiz_mesaji)

        
#       lines = cv2.HoughLinesP(takip, 1, np.pi / 180, 100, None, 80, 40)
#        tmp = np.zeros_like(img)



#        if lines is not None:
#             for l in lines:
#                 for x1,y1,x2,y2 in l:
#                     cv2.line(tmp,(x1,y1),(x2,y2),(255,255,255),3,cv2.LINE_AA)



#        if lines is not None:
#            for i in range(0,len(lines)):
#                rho = lines[i][0][0]
#                theta = lines[i][0][1]
#                a = math.cos(theta)
#                b = math.sin(theta)
#                x0 = a * rho
#                y0 = b * rho
#                pt1 = (int(x0 + 1000*(-b)), int(y0+1000*(a)))
#                pt2 = (int(x0 - 1000*(-b)), int(y0-1000*(a)))
#                cv2.line(tmp,pt1,pt2,(255,255,255),3,cv2.LINE_AA)
        #cv2.line(tmp,pt1,pt2,(255,255,255),3,cv2.LINE_AA)
#        cv2.imshow("orijinal",img)
#        cv2.imshow("bin",otsu)
#        cv2.imshow("edge",edge)
        cv2.imshow("takip",takip)
        cv2.imshow("yol_ayrimi",yol_ayrimi)
        cv2.imshow("sag_maske",sol_maske)
        cv2.imshow("sag ust maske",sag_ust_maske)
        cv2.imshow("sol ust maske",sol_ust_maske)
#        cv2.imshow("hough",tmp)
        
        cv2.waitKey(1)

   
    #2.70
def make_points(image, average): 
    slope, y_int = average 
    y1 = image.shape[0]
    y2 = int(y1 * (3/5))
    x1 = int((y1 - y_int) / slope)
    x2 = int((y2 - y_int) / slope)
    return np.array([x1, y1, x2, y2])


SeritTakip()