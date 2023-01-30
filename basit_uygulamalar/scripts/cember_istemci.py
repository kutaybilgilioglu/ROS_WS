#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 03:42:40 2022

@author: kutay
"""

import rospy
from basit_uygulamalar.srv import CemberHareket

rospy.wait_for_service("cember_servis")
try:
    yaricap = float(input("Yaricap: "))
    yon=input("yon(saatYonu='+', saatYonuTersi='-': ")
    servis = rospy.ServiceProxy("cember_servis",CemberHareket)
    servis(yaricap,yon)
except rospy.ServiceException:
    print("servis hatasi")