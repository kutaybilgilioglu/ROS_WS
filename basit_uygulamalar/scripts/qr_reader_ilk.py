#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 18:56:44 2022

@author: cigdem
"""

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
import tf
import time

odom_broadcaster = tf.TransformBroadcaster()

pub = rospy.Publisher("qr_odom", Odometry, queue_size=50)

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

#th = 0.0
#vx = 0.0
#vy = 0.0
#vth = 0.0
current_time = time.time()


def test():
    rospy.init_node('qr_reader')
    rospy.on_shutdown(file_close)
    rospy.Subscriber("qr_values",String,qrCallback)


    
    rospy.spin()

def qrCallback(mesaj):
        
        global file, degerler, x_str, y_str, str_split, q_id
        global x,y
        
        
        degerler = mesaj.data
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

        rospy.loginfo(q_id)
        rospy.loginfo(x_str)
        rospy.loginfo(y_str)   
        rospy.loginfo(x)
        rospy.loginfo(y)           
               
        
        file.write(q_id)
        file.write(" ")
        file.write(x_str)
        file.write(" ")
        file.write(y_str)
        
        
        odom_quat = tf.transformations.quaternion_from_euler(0, 0, 0)

        odom_broadcaster.sendTransform(
        (x, y, 0.),
        odom_quat,
        current_time,
        "base_link",
        "odom"
    )
        odom = Odometry()
            
        odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))

        odom.child_frame_id = "base_link"
        odom.twist.twist = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))

        pub.publish(odom)


        
test()

    
    
  