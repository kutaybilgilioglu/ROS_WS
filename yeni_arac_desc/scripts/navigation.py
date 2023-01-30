#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 06:26:41 2022

@author: kutay
"""
import rospy
import math
from std_msgs.msg import String
from std_msgs.msg import Int8
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
class Node:
   def __init__(self, dataval,on,arka,onsag,onsol,arkasag,arkasol):
      self.dataval = dataval
      self.on = on
      self.arka = arka
      self.sag = onsag
      self.sol = onsol
      self.arkasag = arkasag
      self.arkasol = arkasol
inverse = False
old_x = 100
old_y = 100
old_msg = ""
scenario_list = []
scenario_list.append("Q42 Q41 Q8 Q9 Q10 Q11 Q48 Q49 Q50 Q51 Q52 Q18 Q19 Q20 Q21 Q23 Q24 Q36 Q37 Q38 Q39 Q40 Q4 Q3 Q31 Q32 Q33 Q34 Q35 Q26 Q25 Q24 Q23 Q21 Q21 Q43 Q44 Q45 Q46 Q47 Q9 Q8 Q41 Q42 Q22")
scenario_list.append("Q42 Q44 Q8 Q9 Q47 Q46 Q45 Q44 Q43 Q20 Q21 Q23 Q24 Q25 Q26 Q35 Q34 Q33 Q32 Q31 Q3 Q4 Q40 Q39 Q38 Q37 Q36 Q24 Q23 Q21 Q20 Q19 Q18 Q52 Q51 Q50 Q49 Q48 Q11 Q10 Q9 Q8 Q41 Q42 Q22")
scenario_list.append("Q41 Q42 Q23 Q24 Q25 Q26 Q35 Q34 Q33 Q32 Q31 Q3 Q4 Q5 Q6 Q8 Q9 Q47 Q46 Q45 Q44 Q43 Q19 Q18 Q52 Q51 Q50 Q49 Q48 Q11 Q10 Q9 Q8 Q6 Q5 Q40 Q39 Q38 Q37 Q36 Q24 Q23 Q42 Q41 Q7")
scenario_list.append("Q41 Q42 Q23 Q24 Q36 Q37 Q38 Q39 Q40 Q5 Q6 Q8 Q9 Q10 Q11 Q48 Q49 Q50 Q51 Q52 Q18 Q19 Q43 Q44 Q45 Q46 Q47 Q9 Q8 Q6 Q5 Q4 Q3 Q31 Q32 Q33 Q34 Q35 Q26 Q25 Q42 Q41 Q7")
scenario_list[0] = scenario_list[0].split(" ")
scenario_list[1] = scenario_list[1].split(" ")
scenario_list[2] = scenario_list[2].split(" ")
scenario_list[3] = scenario_list[3].split(" ")
index = -1
old_msg = ""
last_checkpoint = ""
list = []
list.append(Node('Q1','Q2','','','','','Q30'))
list.append(Node('Q2','Q3','Q1','','Q31','',''))
list.append(Node('Q3','','Q2','','','','Q31'))
list.append(Node('Q4','Q5','Q3','','Q40','',''))
list.append(Node('Q5','Q6','Q4','','','','Q40'))
list.append(Node('Q6','Q8','Q5','','Q41','',''))
list.append(Node('Q7','','','','','',''))
list.append(Node('Q8','Q9','Q6','','','','Q41'))
list.append(Node('Q9','Q10','Q8','','Q47','',''))
list.append(Node('Q10','Q11','Q9','','','','Q47'))
list.append(Node('Q11','Q12','Q10','','Q48','',''))
list.append(Node('Q12','Q13','Q11','','','','Q48'))
list.append(Node('Q13','','Q12','','Q14','',''))
list.append(Node('Q14','Q15','','','','','Q13'))
list.append(Node('Q15','','Q14','','Q16','',''))
list.append(Node('Q16','','Q17','Q15','','',''))
list.append(Node('Q17','Q16','Q18','','','Q52',''))
list.append(Node('Q18','Q17','Q19','Q52','','',''))
list.append(Node('Q19','Q18','Q20','','','Q43',''))
list.append(Node('Q20','Q19','Q21','Q43','','',''))
list.append(Node('Q21','Q20','Q23','','','Q42',''))
list.append(Node('Q22','','','','','',''))
list.append(Node('Q23','Q21','Q24','Q42','','',''))
list.append(Node('Q24','Q23','Q25','','','Q36',''))
list.append(Node('Q25','Q24','Q26','Q36','','',''))
list.append(Node('Q26','Q25','Q27','','','Q35',''))
list.append(Node('Q27','Q26','Q28','Q35','','',''))
list.append(Node('Q28','Q27','','','','Q29',''))
list.append(Node('Q29','','Q30','Q28','','',''))
list.append(Node('Q30','Q29','','','','Q1',''))
list.append(Node('Q31','','','','','Q3','Q2'))
list.append(Node('Q32','Q33','Q31','','','',''))
list.append(Node('Q33','Q34','Q32','','','',''))
list.append(Node('Q34','Q35','Q33','','','',''))
list.append(Node('Q35','','Q34','Q26','Q27','',''))
list.append(Node('Q36','','Q37','Q24','Q25','',''))
list.append(Node('Q37','Q36','Q38','','','',''))
list.append(Node('Q38','Q37','Q39','','','',''))
list.append(Node('Q39','Q38','Q40','','','',''))
list.append(Node('Q40','Q39','','','','Q5','Q4'))
list.append(Node('Q41','Q42','','','','Q8','Q6'))
list.append(Node('Q42','','Q41','Q21','Q23','',''))
list.append(Node('Q43','','Q44','Q19','Q20','',''))
list.append(Node('Q44','Q43','Q45','','','',''))
list.append(Node('Q45','Q44','Q46','','','',''))
list.append(Node('Q46','Q45','Q47','','','',''))
list.append(Node('Q47','Q46','','','','Q10','Q9'))
list.append(Node('Q48','Q49','','','','Q12','Q11'))
list.append(Node('Q49','Q50','Q48','','','',''))
list.append(Node('Q50','Q51','Q49','','','',''))
list.append(Node('Q51','Q52','Q50','','','',''))
list.append(Node('Q52','','Q51','Q17','Q18','',''))

class tmp_nav:
   
   for i in range(0,len(scenario_list[0])-2):
      tmp = scenario_list[0][i].strip("Q")
      tmp = int(tmp)-1
      tmp_next = scenario_list[0][i+1]
      if list[tmp].on == tmp_next:
         print("on")
      elif list[tmp].arka == tmp_next:
         print("arka")
      elif list[tmp].sag == tmp_next:
         print("onsag")
      elif list[tmp].sol == tmp_next:
         print("onsol")
      elif list[tmp].arkasag == tmp_next:
         print("arkasag")
      elif list[tmp].arkasol == tmp_next:
         print("arkasol")
      
      


class navigate():
   def __init__(self):
      rospy.init_node("nav")
      rospy.Subscriber("/odom",Odometry,self.odomCb)
      rospy.Subscriber("/barcode",String,self.barcodeCb)
      self.nav_message = Int8()
      self.nav_msg_test = String()
      self.pub = rospy.Publisher("/nav",Int8,queue_size=10)
      rospy.spin()
   def odomCb(self,msg):
      global inverse
      orientation_q = msg.pose.pose.orientation
      orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
      (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
      yaw = yaw*(180/math.pi)
      if yaw < 0:
        yaw = yaw + 360
      if (yaw<45 and yaw >0) or (yaw<360 and yaw>225):
         inverse = False
      else:
         inverse = True
      #print(inverse)
   def barcodeCb(self,mesaj):
      global old_msg,index,inverse
      if old_msg != mesaj.data and mesaj.data != "Q22" and mesaj.data != "Q7" and index!=1:
         index +=1
         old_msg = mesaj.data
      
         tmp = scenario_list[0][index].strip("Q")
         tmp = int(tmp)-1
         tmp_next = scenario_list[0][index+1]
      #print(inverse)
         if inverse == False:
            if list[tmp].on == tmp_next:
               print("on")
            elif list[tmp].arka == tmp_next:
               print("arka")
            elif list[tmp].sag == tmp_next:
               print("onsol")
            elif list[tmp].sol == tmp_next:
               print("onsag")
            elif list[tmp].arkasag == tmp_next:
               print("arkasag")
            elif list[tmp].arkasol == tmp_next:
               print("arkasol")
         
         
         else:
         
            if list[tmp].on == tmp_next:
               print("arka")
            elif list[tmp].arka == tmp_next:
               print("on")
            elif list[tmp].sag == tmp_next:
               print("arkasag")
            elif list[tmp].sol == tmp_next:
               print("arkasol")
            elif list[tmp].arkasag == tmp_next:
               print("onsol")
            elif list[tmp].arkasol == tmp_next:
               print("onsag")
      if index ==-1:
         index+=1 

      

navigate()