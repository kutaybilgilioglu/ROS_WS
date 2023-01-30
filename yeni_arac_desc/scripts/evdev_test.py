#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 06:26:41 2022

@author: kutay
"""

import os 
import sys
import threading
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int64

import subprocess
rospy.init_node('fm430')
p = ''
a = String()
pub = rospy.Publisher("/barcode",String,queue_size=10)
cmd = ['cat', '/dev/hidraw4']  # the external command to run
timeout_s = 1  # how many seconds to wait 
while True:
    try:

        try:
            p = subprocess.run(cmd,capture_output=True,timeout=timeout_s).stdout
        except subprocess.TimeoutExpired:
            print(p)
            
            a.data = p
            pub.publish(a)
    except KeyboardInterrupt:
        break
