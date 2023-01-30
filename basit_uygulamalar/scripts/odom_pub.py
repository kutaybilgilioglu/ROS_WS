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

x = 0.0
y = 0.0
th = 0.0
angle = Float32()
angle = 0
vx = 0.0
vy = 0.0
vth = 0.0

class test():
    def __init__(self):
        
            rospy.init_node('odometry_publisher')
            self.current_time = rospy.Time.now()
            self.last_time = rospy.Time.now()
            self.odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)
            self.pub = rospy.Publisher("angle",Float32,queue_size=10)
            rospy.Subscriber("hiz_deger",Float64MultiArray,self.callback)
            rospy.spin()


    def callback(self,mesaj):
        global vx, vy, vth,x,y,th,angle,odom_broadcaster
        vx = mesaj.data[0]
        vy = mesaj.data[1]
        vth = mesaj.data[2]
        #rospy.loginfo(mesaj.data[0])
    
        self.current_time = rospy.Time.now()
    
    
   


    # compute odometry in a typical way given the velocities of the robot
        dt = (self.current_time - self.last_time).to_sec()
        delta_x = (vx * np.cos(100*th*(math.pi/180))) * dt
        delta_y = (vx * np.sin(100*th*(math.pi/180))) * dt
        #rospy.loginfo("cos:%f"%(cos(100*th*(math.pi/180))))
        delta_th = vth * dt

        x += delta_x
        y += delta_y
        th -= delta_th
        angle = th
        angle = angle * 100
        mod = angle % 360
        if angle < 0 or angle >=360:
            angle = mod
        
       
        
        
        #self.pub.publish(angle)
        rospy.loginfo(angle)
        angle = (angle*(np.pi/180))
        
    # since all odometry is 6DOF we'll need a quaternion created from yaw
        odom_quat = tf.transformations.quaternion_from_euler(0, 0, angle)

    # first, we'll publish the transform over tf
        odom_broadcaster.sendTransform(
        (x, y, 0.),
        odom_quat,
        self.current_time,
        "base_link",
        "odom"
    )

    # next, we'll publish the odometry message over ROS
        odom = Odometry()
        odom.header.stamp = self.current_time
        odom.header.frame_id = "odom"

        

    # set the position
        odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))

    # set the velocity
        odom.child_frame_id = "base_link"
        odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))

    # publish the message
        self.odom_pub.publish(odom)

        self.last_time = self.current_time
       
        
test()