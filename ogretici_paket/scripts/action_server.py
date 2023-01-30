#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 04:05:09 2022

@author: kutay
"""

import rospy
import actionlib
from ogretici_paket.msg import gorevDAction, gorevDFeedback, gorevDResult

class ActionServer():
    def __init__(self):
        rospy.init_node("action_dugumu")
        self.a_server=actionlib.SimpleActionServer("gorev",gorevDAction,auto_start=False, execute_cb=self.cevapUret)
        self.a_server.start()
        rospy.spin()
    def cevapUret(self,istek):
        geri_bildirim=gorevDFeedback()
        sonuc=gorevDResult()
        rate=rospy.Rate(1)
        for i in range(1,istek.birim1):
            durum="%"+str(i*100/istek.birim1)
            geri_bildirim.oran=durum
            self.a_server.publish_feedback(geri_bildirim)
            rate.sleep()
        sonuc.sonuc1="gorev tamam"
        self.a_server.set_succeeded(sonuc)
        
a_s=ActionServer()        