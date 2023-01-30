#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 03:36:12 2022

@author: kutay
"""

import rospy
from geometry_msgs.msg import Twist
from basit_uygulamalar.srv import CemberHareket

def cemberFonksiyonu(istek):
    yon = istek.yon
    hiz_mesaji = Twist()
    lineer_hiz = 0.5
    hiz_mesaji.linear.x = lineer_hiz
    yaricap = istek.yaricap
    #w = v / r
    if yon == '-':
        hiz_mesaji.angular.z = -(lineer_hiz / yaricap)
    
    else:
        hiz_mesaji.angular.z = lineer_hiz / yaricap
    while not rospy.is_shutdown():
        pub.publish(hiz_mesaji)

rospy.init_node("cember_hareket")
pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
rospy.Service("cember_servis",CemberHareket,cemberFonksiyonu)
rospy.spin()