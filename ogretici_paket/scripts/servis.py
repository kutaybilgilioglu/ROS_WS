#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 03:09:19 2022

@author: kutay
"""

import rospy
from ogretici_paket.srv import GecenZaman

def gecenZamanFonksiyonu(istek):
    robot_hiz=0.5
    sure=istek.hedef_konum/robot_hiz
    return sure

def cevapGonder():
    rospy.init_node("server_dugumu")
    rospy.Service("zaman",GecenZaman,gecenZamanFonksiyonu)
    rospy.spin()
cevapGonder()    