#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Fri Jul  8 17:13:39 2022

@author: eliz
"""

import rospy,time
import numpy as np
from sensor_msgs.msg import LaserScan
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray, Float64, String, Int16, Bool,Int32MultiArray

import math
engel = False
donuldu = False
count=0
roll = pitch = yaw = 0.0
global target
global rderece
rderece=0
target=0
global kontrol,kontrol1,kontrol3,donusturuldu,test,test1,dur
test=test1=dur=True
kontrol=True
kontrol1=kontrol3=True
clock=False
tekrar_lazer=True
donusturuldu=False
x=0
y=0
don=False
global hiz
hiz=0
global engel_durum1
engel_durum1=False
global rtest
global yuk
tx = 0
yuk=False
start_time=0
class Lidar():
    def __init__(self):
        #rospy.on_shutdown(self.shutdown)
        rospy.init_node("lazer_dugumu")
        self.pub= rospy.Publisher("cmd_vel",Twist,queue_size=10)
        self.hiz=Twist()
        self.pub1 = rospy.Publisher("buzzer",Bool,queue_size=10)
        self.toogle_msg=Bool()
        self.pub2= rospy.Publisher("engel_durum",Bool,queue_size=10)
        self.engel_durum=Bool()
        rospy.Subscriber("yuk_deger",Bool,self.yukcall)
        #self.pub = rospy.Publisher("teleop",Int32MultiArray,queue_size=10)
        #self.motor = Int32MultiArray()
        rospy.Subscriber("odom",Odometry,self.robot_rotation)
        rospy.Subscriber("scan",LaserScan,self.lazercall)
        self.rate = rospy.Rate(5)
        rospy.spin()
        
    def yukcall(self,mesaj):
        global yuk
        yuk=mesaj
        
    def robot_stop(self):
        self.hiz.linear.x=0.0
        self.hiz.angular.z=0.0
        self.pub.publish(self.hiz)         
        
    def robot_forward(self):
        self.hiz.linear.x=0.5
        self.hiz.angular.z=0.0
        self.pub.publish(self.hiz)       
    
    def robot_rotation(self,mesaj):
        
        global roll, pitch, yaw,rderece,hiz
        orientation_q = mesaj.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
        rderece= yaw*(180/np.pi)
        if rderece < 0:
            rderece = rderece+360
        
        print("rderece: %f"%rderece)
        hiz=mesaj.twist.twist.linear.x
  
    def robot_turn(self,count,rderece):
        global donuldu,test,test1,kp,ki
        global x,y
        global target
        
        if count==0 or count==3:
            if test:
                target = rderece + 90
                if target >= 360:
                    target = target - 360
                test=False
                
            print("target: %f"%target)
            self.hiz.linear.x=0.0
            self.hiz.angular.z=(-1.0)
            self.pub.publish(self.hiz)
        else :
            if count==1 or count==2:
                if test1:
                    target = rderece - 90
                    if target < 0:
                        target = target + 360
                    test1=False

            print("target: %f"%target)
            self.hiz.linear.x=0.0
            self.hiz.angular.z=(1.0)
            self.pub.publish(self.hiz)    


        donme=abs(target-rderece)
        print("donme: %f"%donme)
        if donme<6:
            test=True
            test1=True
            donuldu=True
            #print("oldu")

    def lazercall(self,msg):
        deger=list()
        global x,y
        global engel, donuldu,donusturuldu,engel_durum1
        global derece1
        global derece
        global uzaklik,uzaklik1
        global count
        global x,y,boy,mesafe,min_on,engel_boy,gecmis,zaman,kontrol,kontrol1,kontrol3,dur
        global clock,tekrar_lazer
        global yer_degistirme
        global tx
        
        for i in range(0,1440):
                if i%4==0:
                    deger.append(msg.ranges[i])

        sag_on=list(deger[0:90])
        sol_on=list(deger[271:359])
        sag_arka=list(deger[91:180])
        sol_arka=list(deger[181:270])
        arka=sol_arka+sag_arka
        min_sag= min(sag_arka)
        min_arka= min(arka)
        print(deger[0],msg.ranges[0],deger[90],min_sag,min_arka)
        
        if deger[0]<1.0 and clock == False and tekrar_lazer:
            print("engelle karsilasildi.")
            clock = True
            self.robot_stop()
            start_time=time.time()

        elif deger[0]<1.0 and clock:
            current_time =time.time()
            elapsed = current_time - start_time
            self.toogle_msg.data=True
            self.pub1.publish(self.toogle_msg)
            
            if elapsed>15:
                clock = False
                tekrar_lazer = False
                self.toogle_msg.data=False
                self.pub1.publish(self.toogle_msg)
                print("15 saniye gecti")
        elif deger[0]>3.5 and clock:
            clock = False
            tekrar_lazer=True
            engel_durum1=False
            self.engel_durum=engel_durum1
            self.pub2.publish(self.engel_durum)
            print("Engel yoldan cekildi. Planlanmıs rotadan devam ediliyor...")
        elif deger[0]<1.0 and clock== False and tekrar_lazer==False:
            min_on=deger[0]
            engel_durum1=True
            self.engel_durum=engel_durum1
            self.pub2.publish(self.engel_durum)
            engel=True


        if engel:
            if  count==0:
                
                for i in range(0,91):
                    if deger[i+1]-deger[i]>2.0:
                        x=deger[i]
                        rospy.loginfo("x: %f"%x)
                        break
                uzaklik=abs(math.pow(x,2)-math.pow(min_on,2))

                uzaklik=math.sqrt(uzaklik)
                #derece1= np.arccos(x/min_on)*(180/np.pi)
                #uzaklik= abs(np.sin(derece1)*x)
                for i in range(270,359):
                    if deger[i]-deger[i+1]>3.0:
                        y=deger[i+1]
                        break    
                derece2= np.arccos(y/min_on)*(180/np.pi)
                boy= np.sin(derece2)*y
                if dur:
                    uzaklik1=1.0
                    print("uzaklik: %f"%uzaklik)
                    self.robot_stop()
                    dur=False
                #print(rderece)
                self.robot_turn(count,rderece)
                print("donus1")
                if donuldu:
                    self.hiz.angular.z = 0.0
                    self.pub.publish(self.hiz)
                    donuldu = False
                    yer_degistirme = 0
                    count=1
                    dur=True
                    
            elif count==1:
                #print("hiz: %f"%hiz)
                print(donuldu)
                #print("uzaklik: %f"%uzaklik1)
                if dur:
                    self.robot_stop()
                    t0=rospy.Time.now().to_sec()
                    
                    while yer_degistirme < uzaklik1:
                        self.robot_forward()
                        self.rate.sleep()
                        print("uzaklik: %f"%uzaklik1)
                        
                        t1=rospy.Time.now().to_sec()
                        yer_degistirme=abs(hiz*(t1-t0))
                        print("yerdegstirme: %f"%yer_degistirme)
                        
                    
                    self.robot_stop()
                    dur=False
                self.robot_turn(count,rderece)
                #print(rderece)
                #print(donuldu)
                if donuldu:
                    count=2
                    donuldu = False
                    yer_degistirme=0
                    dur=True
                    print("donus2")
            elif count==2:
                if kontrol:
                    self.robot_forward()
                    """
                    for i in range(270,359):
                        if deger[i+1]-deger[i]>3.0:
                            x=deger[i]
                            vderece=(i)
                            rospy.loginfo(x)
                            break
                    mino= min(sol_on)
                    for i in range(270,360):
                        if mino==deger[i]:
                            vderece1=i
                            #rospy.loginfo(x)
                            break
                    a=x*np.cos(vderece)
                    b=mino*np.cos(vderece1)
                    engel_boy=a-b
                    """
                    mesafe=abs((2*min_on)+0.9)
                    print(hiz)
                    print("mesafe: %f"%mesafe)
                    t0=rospy.Time.now().to_sec()
                    self.robot_forward()
                    self.rate.sleep()
                    while yer_degistirme < mesafe:
                        
                        t1=rospy.Time.now().to_sec()
                        yer_degistirme=abs(hiz*(t1-t0))
                    kontrol=False
                
                """
                if kontrol1:
                    self.robot_forward()
                    if min(sag_on)>0.1:
                        kontrol1=False
                """
                if dur:
                    self.robot_stop()
                    dur=False
                print(rderece)
                self.robot_turn(count,rderece)
                if donuldu:
                    count=3
                    donuldu = False
                    print("donus3")
                    yer_degistirme=0
                    dur=True
            elif count==3:
                print(hiz)
                uzaklik1=uzaklik1+0.3
                if dur:
                    t0=rospy.Time.now().to_sec()
                    #self.robot_forward()
                    self.robot_forward()
                    self.rate.sleep()
                    while yer_degistirme < uzaklik1:
                        
                        t1=rospy.Time.now().to_sec()
                        yer_degistirme=abs(hiz*(t1-t0))
                    self.robot_stop()
                    dur=False
                print(rderece)
                self.robot_turn(count,rderece)
                if donuldu:
                    count=4
                    donuldu = False
                    yer_degistirme=0
                    print("donus4")
                    dur=True
            else:
                self.robot_forward()
                print("dduz devam")
                engel=False
                count=0
                kontrol=True
                kontrol1=True
                tekrar_lazer=True
                engel_durum1=False
                self.engel_durum=engel_durum1
                self.pub2.publish(self.engel_durum)
        else:
            self.robot_forward()
            engel_durum1=False
            self.engel_durum=engel_durum1
            self.pub2.publish(self.engel_durum)
                
        deger.clear()
        
    def shutdown(self):
        self.hiz.linear.x=0.0
        self.hiz.angular.z=0.0
        self.pub.publish(self.hiz)
        time.sleep(0.05)
        
        
Lidar()