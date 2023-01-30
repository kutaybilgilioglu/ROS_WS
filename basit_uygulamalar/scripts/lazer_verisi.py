#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 04:06:59 2022

@author: kutay
"""

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class LazerVerisi():
    def __init__(self):
        rospy.init_node("lazer_dugumu")
        self.pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
        self.hiz_mesaji = Twist()
        rospy.Subscriber("scan",LaserScan,self.lazerCallback)
        rospy.spin()
    def lazerCallback(self,mesaj):
        sol_on = list(mesaj.ranges[0:9])
        sag_on = list(mesaj.ranges[350:359])
        on = sol_on + sag_on
        sol = list(mesaj.ranges[80:100])
        sag = list(mesaj.ranges[260:280])
        arka = list(mesaj.ranges[170:190])
        print(on)    
        
#        min_on = min(on)
#        min_sol = min(sol)
#        min_sag = min(sag)
#        min_arka = min(arka)
#        print(min_on,min_sol,min_sag,min_arka)
#        if min_on < 1.0:
#            self.hiz_mesaji.linear.x =0
#            self.pub.publish(self.hiz_mesaji)
#        else:
#            self.hiz_mesaji.linear.x= 0.25
#            self.pub.publish(self.hiz_mesaji)
nesne = LazerVerisi()
        