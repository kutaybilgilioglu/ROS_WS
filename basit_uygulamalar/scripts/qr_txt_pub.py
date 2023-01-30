#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 07:37:47 2022

@author: kutay
"""

import rospy
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Bool
import numpy as np
from nav_msgs.msg import Odometry
import rospkg

rota = "Q7-Q41-Q42-Q22-Q23-Q24-Q36-Q37-Q38-Q39-Q40-Q5-Q6-Q7-Q8-Q9-Q10-Q11-Q48-Q49-Q50-Q51-Q52-Q18-Q19-Q43-Q44-Q45-Q46-Q47-Q9-Q8-Q7-Q6-Q5-Q4-Q3-Q31-Q32-Q33-Q34-Q35-Q26-Q25-Q24-Q23-Q22-Q42-Q41-Q7-Q6-Q5"
#rospy.init_node("rota_pub")
pub = rospy.Publisher("rota_m",Float64MultiArray,queue_size=1)
rospack = rospkg.RosPack()
check = Float64MultiArray()
rota=rota.split("-")
check_x = 0
check_y = 0
index = 0
yuk = False
step_up = Bool() 
step_down = Bool()
down_pub = rospy.Publisher("step_down",Bool,queue_size=1)
up_pub = rospy.Publisher("step_up",Bool,queue_size=1)
with open(rospack.get_path('basit_uygulamalar')+"/scripts/qr_test_parkur.txt") as f:
        lines = f.readlines()

def test():
    rospy.init_node("checkpoint")
    rospy.Subscriber("odom1",Odometry,odomCallback)
    rospy.Subscriber("yuk_deger",Bool,yukCallback)
    
    
    rospy.spin()
    
def yukCallback(self,mesaj):
    global yuk
    yuk = mesaj.data
    
def odomCallback(mesaj):
    global check_x,check_y,index,lines,pub,check,yuk,step_up,step_down,up_pub,down_pub
    for line in lines:
        line = line.split(";")
        #rospy.loginfo("%s   %s"%(line[0],rota[index]))
        if line[0]==rota[index]:
            check_x=line[1]
            check_y=line[2]
            check_y = check_y.strip('\r')
            check_y = check_y.strip('\n')
            check_x = float(check_x)
            check_y = float(check_y)
            check.data = [check_x,check_y]
            
            pub.publish(check)
    if abs((1000*mesaj.pose.pose.position.x)-check_x) < 300 and abs((1000*mesaj.pose.pose.position.y)-check_y) < 300 :
#        if rota[index]=='Q50' or rota[index]=='Q45' or rota[index]=='Q38' or rota[index]=='Q33':
#            if yuk == True:
#                step_down.data = True
#                step_up.data = False
#                down_pub.publish(step_down)
#                up_pub.publish(step_up)
#            else:
#                step_down.data = False
#                step_up.data = True
#                down_pub.publish(step_down)
#                up_pub.publish(step_up)
#            
#                
#                
                
                
                
            
            
            
        index+=1
    if index == len(rota):
        rospy.loginfo("rota tamamlandı")
            
            
test()            
    
    
    
    
