#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 16:45:23 2022

@author: kutay
"""
import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Bool
import numpy as np
import time
class point:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.index = np.array([])
    def add_node(self,node):
        self.index = np.append(self.index,node)
list = []

donus = False
run = True
last_node = -1
count = 0
class main():
    def __init__(self):
        
                
        rospy.init_node("odom_reader")
        rospy.on_shutdown(self.shutdown)
        rospy.Subscriber("odom",Odometry,self.callback)
        rospy.Subscriber("turn",Bool,self.donusCallback)
        rospy.spin()
        
    def donusCallback(self,mesaj):
        global donus
        global run
        donus = mesaj.data
        if donus== False:
            run = True
        
        
    def callback(self,mesaj):
            global donus,run, count, last_node
            kayit = True
    
            x = round(mesaj.pose.pose.position.x,2)
            y = round(mesaj.pose.pose.position.y,2)
            if last_node == -1 and donus:
                    list.append(point(x,y))
                    
                    
                    last_node = count
                    count+=1
                    run = False
            elif donus and run:
                rospy.loginfo("in")
                for i in range(len(list)):
                    if abs(list[i].x - x) < 0.2 and abs(list[i].y - y)< 0.2:
            
                        list[i].add_node(last_node)
                        list[last_node].add_node(i)
                        i = last_node
                        
                        kayit = False
                    
                
                if kayit:        
                    list.append(point(x,y))
                    list[count].add_node(last_node)
                    
                    list[count-1].add_node(count)
                    
                    last_node = count
                    count+=1
                run = False
            
    def shutdown(self):
        for obj in list:
                    print(obj.x,obj.y)
                    print(obj.index)
               

main()        
