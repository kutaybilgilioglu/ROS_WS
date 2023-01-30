#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 02:04:05 2022

@author: kutay
"""

import rospy
import sys
import termios
import tty
from std_msgs.msg import Int32MultiArray
from select import select
import time
x = 0
y = 0

def saveTerminalSettings():
        return termios.tcgetattr(sys.stdin)

settings = saveTerminalSettings()


def restoreTerminalSettings(old_settings):
    
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    
    
class test():
    def __init__(self):
        global settings
        while rospy.is_shutdown:    
            rospy.init_node("tele_op")
            rospy.on_shutdown(self.shutdown)
            self.pub = rospy.Publisher("teleop",Int32MultiArray,queue_size=10)
            self.motor = Int32MultiArray()
            self.key = self.getKey()
            if (self.key == '\x03'):
                    break
            self.kontrol()
    
    def getKey(self):
            global settings
            tty.setraw(sys.stdin.fileno())
            # sys.stdin.read() returns a string on Linux
            rlist, _, _ = select([sys.stdin], [], [], 0.1)
            if rlist:
                key = sys.stdin.read(1)
            else:
                key = ''
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
            return key
    def kontrol(self):
        global x,y
        
        if self.key == 'w':
            if  x != 240 and y !=240:
                x+=30
                y+=30
        elif self.key == 's':
            x=0
            y=0
        elif self.key == 'x':
            if x != -240 and y != -240:
                x-=30
                y-=30
        elif self.key == 'a':
            if x-y==0:
                x=0
                y=0
            if x != -240 and y!= 240:
                x-=30
                y+=30
        elif self.key == 'd':
            if x-y==0:
                x=0
                y=0
            if x != 240 and y != -240:
                x+=30
                y-=30
        self.motor.data = [x,y]
        self.pub.publish(self.motor)
        
        
    def shutdown(self):
        global settings
        
        
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        x=0
        y=0
        self.motor.data = [x,y]
        self.pub.publish(self.motor)
        #time.sleep(0.01)
        

test()