#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 04:19:13 2022

@author: kutay
"""

import rospy
import actionlib
from ogretici_paket.msg import gorevDAction, gorevDGoal

def bildirimFonksiyonu(bilgi):
    print("Gorev tamamlama durumu: ",bilgi.oran)

def istekteBulun():
    rospy.init_node("action_CLİENT")
    istemci=actionlib.SimpleActionClient("gorev",gorevDAction)
    istemci.wait_for_server()
    istek=gorevDGoal()
    istek.birim1=9
    istemci.send_goal(istek,feedback_cb=bildirimFonksiyonu)
    istemci.wait_for_result()
    x=istemci.get_result().sonuc1
    return x
cikti =istekteBulun()
print("son durum: ",cikti)    