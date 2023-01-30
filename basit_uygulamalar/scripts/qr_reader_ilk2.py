#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 18:56:44 2022

@author: cigdem
"""

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray,Bool,Float64
 

pub = rospy.Publisher("qr_odom", Float64MultiArray, queue_size=10)
pub1 = rospy.Publisher("qr_yuk", Bool, queue_size =1)
pub2 = rospy.Publisher("ilk_iki", Bool , queue_size=10)

def file_close():
    global file,count,degerler,x,y
    file.close()


file = open("qr_values","w+")
degerler = " "
x_str = " "
y_str = " "
q_id = " "
x = 0.0
y = 0.0
str_split = list()
pub_xy = Float64MultiArray()
qr_yuk = False
qr_son = list()
sensor_yuk = False
count = 0
ilk_iki = False

def test():
    rospy.init_node('qr_reader')
    rospy.on_shutdown(file_close)
    rospy.Subscriber('qr_values',String,qrCallback)
    rospy.Subscriber('distance',Float64,Callback)
    rospy.spin()
    
    
def Callback(mesaj):
    global sensor_yuk   
    
    if(mesaj.data<10):
        sensor_yuk = True

def qrCallback(mesaj):
        
        global file, degerler, x_str, y_str, str_split, q_id
        global x,y, count
        global pub_xy, qr_son, ilk_iki
        global qr_yuk
        
        
        degerler = mesaj.data
        
        count += 1
        if(count == 2):
            ilk_iki = True
            
        pub2.publish(ilk_iki)

        str_split = degerler.split(";")
        
        rospy.loginfo(degerler)
        rospy.loginfo(str_split)
        
        q_id = str_split[0] 
        x_str = str_split[1]
        y_str = str_split[2] 
        y_str = y_str.strip('\r')
        y_str = y_str.strip('\n')
        
        x = float(x_str)
        y = float(y_str)

       
        
        
        pub_xy.data = [x,y]
        pub.publish(pub_xy)


        if (q_id == "Q33" or q_id == "Q38" or q_id == "Q45" or q_id == "Q50"):
            qr_yuk = True
            if(sensor_yuk):
                rospy.loginfo("qr okundu, yuk noktasindayiz!")
            pub1.publish(qr_yuk)
            
            
#        rospy.loginfo(q_id)
#        rospy.loginfo(x_str)
#        rospy.loginfo(y_str)   
        rospy.loginfo(x)
        rospy.loginfo(y)           
               
        
        file.write(q_id)
        file.write(" ")
        file.write(x_str)
        file.write(" ")
        file.write(y_str)
        

        
test()

    
    
  