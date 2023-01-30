#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 04:55:09 2022

@author: kutay
"""

import rospy
from ogretici_paket.msg import BataryaDurum

def batarya_fonksiyonu(mesaj):
    rospy.loginfo("Robot şarjı: %s"%mesaj.batarya)

def mesajDinle():
    rospy.init_node("abone_dugumu")
    rospy.Subscriber("batarya_konusu",BataryaDurum,batarya_fonksiyonu)
    rospy.spin()
mesajDinle()    