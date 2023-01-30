#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 03:15:28 2022

@author: kutay
"""

import rospy
from ogretici_paket.srv import GecenZaman

def istekteBulun(x):
    rospy.wait_for_service("zaman")
    try:
        servis=rospy.ServiceProxy("zaman",GecenZaman)
        cevap=servis(x)
        return cevap.gecen_sure
    except rospy.ServiceException:
        print("Servis ahatsı")
hedef=float(input("Hedef Konum Giriniz: "))
out=istekteBulun(hedef)
print("Hedefe varana kadar sure: ", out)        