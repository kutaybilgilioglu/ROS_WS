#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 21:47:31 2022

@author: cigdem
"""
import math
from math import sin, cos, pi
import numpy as np

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float32

import time

    
odom_broadcaster = tf.TransformBroadcaster()

x = 8.0
y = 0.0
th = np.pi/2
angle = Float32()
angle = 90
vx = 0.0
vy = 0.0
vth = 0.0
son = False
sonx = 0
sony = 0
aci = 0
class test():
    def __init__(self):
        
            rospy.init_node('odometry_publish2r')
            self.current_time = rospy.Time.now()
            self.last_time = rospy.Time.now()
            self.odom_pub = rospy.Publisher("odom1", Odometry, queue_size=50)
            self.pub = rospy.Publisher("angle",Float32,queue_size=10)
            rospy.Subscriber("hiz_deger",Float64MultiArray,self.callback)
            rospy.Subscriber("qr_odom",Float64MultiArray,self.qr_odom_Callback)
            
            #rospy.Subscriber("ilk_iki",Float64MultiArray,self.qr_ilk)
            rospy.spin()

    def qr_odom_Callback(self,mesaj):
         global x, y,son,sonx,sony,angle
         if son == False:
         	x = (mesaj.data[0]/1000)
         	y = (mesaj.data[1]/1000)
         	sonx = x
         	sony = y
         	son = True
         else:
         	x = (mesaj.data[0]/1000)
         	y = (mesaj.data[1]/1000)
         	if sonx-x == 0 and y-sony >0:
         		angle = 90
         		
         	elif sonx-x == 0 and y-sony <0:
         		angle = 270
         	elif x-sonx > 0 and y-sony == 0:
         		angle = 0
         	elif x-sonx < 0 and y-sony == 0:
         		angle = 180
        
    def callback(self,mesaj):
        global vx, vy, vth,x,y,th,angle,odom_broadcaster,aci
        vx = mesaj.data[0]
        vy = mesaj.data[1]
        vth = mesaj.data[2]
        angle = angle*(180/np.pi)
        mod = angle % 360
        
        
        if (angle>=0 and angle<45) or (angle>=315 and angle<=359):
            aci=1
            
        elif angle>=45 and angle<135:
            aci=90
            
        elif angle>=135 and angle<225:
            aci=180
            
        elif angle>=225 and angle<315:
            aci=270
            
        rospy.loginfo("aci: %f  derece:%f"%(aci,angle))
    
        self.current_time = rospy.Time.now()
    
        angle = angle/100
   


    # compute odometry in a typical way given the velocities of the robot
        dt = (self.current_time - self.last_time).to_sec()
        delta_x = (vx * np.cos(100*th*(math.pi/180))) * dt
        
        delta_y = (vx * np.sin(100*th*(math.pi/180))) * dt
        delta_th = vth * dt

        x += delta_x
        y += delta_y
        th += delta_th
        angle = th
        angle = angle * 100
        mod = angle % 360
        if angle < 0 or angle >=360:
            angle = mod
        
       
        
        
        self.pub.publish(angle)
        
        angle = (angle*(np.pi/180))
        
    # since all odometry is 6DOF we'll need a quaternion created from yaw
        odom_quat = tf.transformations.quaternion_from_euler(0, 0, angle)

  

    # next, we'll publish the odometry message over ROS
        odom = Odometry()
        odom.header.stamp = self.current_time
        odom.header.frame_id = "odom1"

        

    # set the position
        odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))

    # set the velocity
        odom.child_frame_id = "base_link"
        odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))

    # publish the message
        self.odom_pub.publish(odom)

        self.last_time = self.current_time
       
        
test()
