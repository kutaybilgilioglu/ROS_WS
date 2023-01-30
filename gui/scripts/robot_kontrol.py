#!/usr/bin/env python3
# -- coding: utf-8 --

# Form implementation generated from reading ui file 'robot_kontrol.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import rospy,time
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from std_msgs.msg import Float64MultiArray, Float64, String, Int16, Bool,Int32MultiArray
from nav_msgs.msg import Odometry
from nav_msgs.msg import OccupancyGrid
import cv2
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import sip


clock=True
start_time=0
start=0

def _color_converter(value):
    if value == -1:
        return 0xcd / 0xff
    return (100 - value) / 100.0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 732)
        MainWindow.setStyleSheet("#centra""l_widget{\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    background-color: rgb(46, 52, 54);\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(290, 270, 841, 411))
        self.frame.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_map = QtWidgets.QLabel(self.frame)
        self.label_map.setGeometry(QtCore.QRect(-4, 6, 831, 401))
        self.label_map.setText("")
        self.label_map.setObjectName("label_map")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(280, 10, 841, 261))
        self.widget_2.setStyleSheet("#widget_2{\n"
"    background-color: rgb(0,0,0);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.frame_8 = QtWidgets.QFrame(self.widget_2)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 321, 261))
        self.frame_8.setStyleSheet("#frame_8{\n"
"    border-color: rgb(186, 189, 182);\n"
"background-color: rgb(28, 26, 29);\n"
"}\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_cam = QtWidgets.QLabel(self.frame_8)
        self.label_cam.setGeometry(QtCore.QRect(10, 10, 311, 251))
        self.label_cam.setText("")
        self.label_cam.setObjectName("label_cam")
        self.frame_7 = QtWidgets.QFrame(self.widget_2)
        self.frame_7.setGeometry(QtCore.QRect(320, 0, 521, 261))
        self.frame_7.setStyleSheet("#frame_7{\n"
"background-color: rgb(28, 26, 29);\n"
"}\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_konum = QtWidgets.QLabel(self.frame_7)
        self.label_konum.setGeometry(QtCore.QRect(20, 40, 211, 61))
        self.label_konum.setStyleSheet("font: 75 14pt \"Ubuntu Mono\";\n"
"color: rgb(0, 255, 0);")
        self.label_konum.setObjectName("label_konum")
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 75 11pt \"Ubuntu Mono\";\n"
"color: rgb(253, 252, 255);")
        self.label_5.setObjectName("label_5")
        self.widget_4 = QtWidgets.QWidget(self.frame_7)
        self.widget_4.setGeometry(QtCore.QRect(240, 30, 201, 91))
        self.widget_4.setObjectName("widget_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget_4)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 10, 201, 61))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_8 = QtWidgets.QLabel(self.frame_7)
        self.label_8.setGeometry(QtCore.QRect(230, 10, 241, 31))
        self.label_8.setStyleSheet("font: 75 13pt \"Ubuntu Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setGeometry(QtCore.QRect(360, 120, 131, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/newcircle.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame_7)
        self.label.setGeometry(QtCore.QRect(200, 120, 131, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/newcircle.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 131, 131))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/icons/newcircle.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_hiz = QtWidgets.QLabel(self.frame_7)
        self.label_hiz.setGeometry(QtCore.QRect(100, 150, 35, 31))
        self.label_hiz.setStyleSheet("font: 75 17pt \"Ubuntu Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_hiz.setObjectName("label_hiz")
        self.label_10 = QtWidgets.QLabel(self.frame_7)
        self.label_10.setGeometry(QtCore.QRect(90, 180, 41, 31))
        self.label_10.setStyleSheet("font: 75 20pt \"Ubuntu Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_akim = QtWidgets.QLabel(self.frame_7)
        self.label_akim.setGeometry(QtCore.QRect(250, 160, 45, 31))
        self.label_akim.setStyleSheet("font: 75 17pt \"Ubuntu Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_akim.setObjectName("label_akim")
        self.label_15 = QtWidgets.QLabel(self.frame_7)
        self.label_15.setGeometry(QtCore.QRect(250, 190, 31, 31))
        self.label_15.setStyleSheet("font: 75 20pt \"Ubuntu Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setGeometry(QtCore.QRect(400, 180, 61, 31))
        self.label_4.setStyleSheet("font: 75 20pt \"Ubuntu Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_sicaklik = QtWidgets.QLabel(self.frame_7)
        self.label_sicaklik.setGeometry(QtCore.QRect(410, 150, 41, 31))
        self.label_sicaklik.setStyleSheet("font: 75 20pt \"Ubuntu Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_sicaklik.setObjectName("label_sicaklik")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(10, 10, 271, 411))
        self.widget_3.setStyleSheet("#widget_3{\n"
"background-color: rgb(28, 26, 29);\n"
"}\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 101, 41))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/icons/icons/batteryyrm.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_buzzer = QtWidgets.QLabel(self.widget_3)
        self.label_buzzer.setGeometry(QtCore.QRect(160, 140, 91, 91))
        self.label_buzzer.setText("")
        self.label_buzzer.setPixmap(QtGui.QPixmap(":/icons/icons/uyarii.png"))
        self.label_buzzer.setScaledContents(True)
        self.label_buzzer.setObjectName("label_buzzer")
        self.btn_io = QtWidgets.QPushButton(self.widget_3)
        self.btn_io.setEnabled(True)
        self.btn_io.setGeometry(QtCore.QRect(30, 20, 81, 81))
        self.btn_io.setAutoFillBackground(False)
        self.btn_io.setStyleSheet("background-color: rgb(28, 26, 29);\n"
"")
        self.btn_io.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/onoff-r.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_io.setIcon(icon)
        self.btn_io.setIconSize(QtCore.QSize(81, 81))
        self.btn_io.setObjectName("btn_io")
        self.btn_lock = QtWidgets.QPushButton(self.widget_3)
        self.btn_lock.setGeometry(QtCore.QRect(170, 20, 81, 81))
        self.btn_lock.setStyleSheet("#btn_lock{\n"
"background-color: rgb(28, 26, 29);\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.btn_lock.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/lockk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_lock.setIcon(icon1)
        self.btn_lock.setIconSize(QtCore.QSize(61, 61))
        self.btn_lock.setObjectName("btn_lock")
        self.label_battery = QtWidgets.QLabel(self.widget_3)
        self.label_battery.setGeometry(QtCore.QRect(40, 150, 51, 20))
        self.label_battery.setStyleSheet("font: 75 18pt \"Ubuntu Mono\";\n"
"color: rgb(253, 252, 255);")
        self.label_battery.setTextFormat(QtCore.Qt.PlainText)
        self.label_battery.setScaledContents(False)
        self.label_battery.setObjectName("label_battery")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(170, 110, 91, 20))
        self.label_7.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"color: rgb(253, 252, 255);")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(180, 210, 51, 17))
        self.label_9.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"color: rgb(253, 252, 255);")
        self.label_9.setObjectName("label_9")
        self.frame_2 = QtWidgets.QFrame(self.widget_3)
        self.frame_2.setGeometry(QtCore.QRect(10, 280, 251, 111))
        self.frame_2.setStyleSheet("border-color: rgb(0, 255, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.label_fair = QtWidgets.QLabel(self.frame_2)
        self.label_fair.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.label_fair.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Ubuntu Condensed\";")
        self.label_fair.setObjectName("label_fair")
        self.label_saat_sure = QtWidgets.QLabel(self.frame_2)
        self.label_saat_sure.setGeometry(QtCore.QRect(160, 80, 81, 31))
        self.label_saat_sure.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Ubuntu Condensed\";")
        self.label_saat_sure.setObjectName("label_saat_sure")
        self.label_12 = QtWidgets.QLabel(self.widget_3)
        self.label_12.setGeometry(QtCore.QRect(150, 260, 81, 20))
        self.label_12.setStyleSheet("font: 57 10pt \"Ubuntu\";\n"
"color: rgb(253, 252, 255);")
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(230, 260, 21, 21))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/icons/icons/radiows.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.comboBox = QtWidgets.QComboBox(self.widget_3)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(30, 180, 81, 21))
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 26, 29);\n"
"font: 75 italic 10pt \"Ubuntu Condensed\";")
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setFrame(True)
        self.comboBox.setHidden(True)
        self.comboBox.setModelColumn(0)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 420, 271, 261))
        self.widget.setStyleSheet("#widget{\n"
"    background-color: rgb(0,0,0);\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 420, 271, 261))
        self.frame_4.setStyleSheet("#frame_4{\n"
"    background-color: rgb(28, 26, 29);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_4)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 50, 251, 71))
        self.plainTextEdit.setStyleSheet("background-color: rgb(28, 26, 29);\n"
"border-color: rgb(254, 249, 249);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Ubuntu Condensed\";")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(10, 140, 231, 20))
        self.label_13.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"color: rgb(253, 252, 255);")
        self.label_13.setObjectName("label_13")
        self.checkBox_bos = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_bos.setGeometry(QtCore.QRect(20, 10, 101, 23))
        self.checkBox_bos.setStyleSheet("font: 9pt \"Ubuntu\";\n"
"color: rgb(0, 0, 0);")
        self.checkBox_bos.setObjectName("checkBox_bos")
        self.checkBox_yuklu = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_yuklu.setGeometry(QtCore.QRect(150, 10, 92, 23))
        self.checkBox_yuklu.setStyleSheet("font: 9pt \"Ubuntu\";\n"
"color: rgb(0, 0, 0);")
        self.checkBox_yuklu.setObjectName("checkBox_yuklu")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(10, 170, 251, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(28, 26, 29);\n"
"border-color: rgb(254, 249, 249);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Ubuntu Condensed\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setGeometry(QtCore.QRect(200, 220, 51, 25))
        self.pushButton.setStyleSheet("background-color: rgb(28, 26, 29);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1129, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        rospy.init_node("arayuz")
        self.pub=rospy.Publisher("navigasyon",String,queue_size=10)
        self.navigasyon=String()
        rospy.Subscriber("battery_state",String,self.bateryCall)
        rospy.Subscriber("odom",Odometry,self.odomCallback)
        rospy.Subscriber("engel_durum",Bool,self.panelCall)
        rospy.Subscriber("buzzer",Bool,self.buzzerCall)
        rospy.Subscriber("volt_deger",Float64,self.akimCall)
        rospy.Subscriber("hiz_deger",Float64MultiArray,self.hizCall)
        rospy.Subscriber("map",OccupancyGrid,self.mapCallback,queue_size=10)
        self.bridge = CvBridge()
        rospy.Subscriber("usb_cam/image_raw/compressed",CompressedImage,self.kameracall)
        rospy.Subscriber("qr_values",String,self.qrCall)
        
        
        MainWindow.setWindowTitle(_translate("MainWindow", "KOU Rover"))
        #self.label_konum.setText(_translate("MainWindow", "40.0078 40.00876"))
        self.label_5.setText(_translate("MainWindow", "LOCATİON DATA:"))
        self.label_8.setText(_translate("MainWindow", "Vehicle Mission Time Period:"))
        #self.label_hiz.setText(_translate("MainWindow", "5"))
        self.label_10.setText(_translate("MainWindow", "m/s"))
        self.label_akim.setText(_translate("MainWindow", "12.2"))
        self.label_15.setText(_translate("MainWindow", "V"))
        self.label_4.setText(_translate("MainWindow", "°C"))
        self.label_sicaklik.setText(_translate("MainWindow", "20"))
        #self.label_battery.setText(_translate("MainWindow", "%45"))
        self.label_7.setText(_translate("MainWindow", "Security Lock"))
        self.label_9.setText(_translate("MainWindow", "Caution"))
        self.label_fair.setText(_translate("MainWindow", "engel tespit edildi"))
        self.label_saat_sure.setText(_translate("MainWindow", "00:00:15"))
        self.label_12.setText(_translate("MainWindow", "Fair Safe Mod"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Stop Mod"))
        #self.comboBox.setItemText(0, _translate("MainWindow", "Stop Mod"))
        #self.comboBox.setItemText(1, _translate("MainWindow", "Low Power"))
        self.label_13.setText(_translate("MainWindow", "Please write the robot rotation"))
        self.checkBox_bos.setText(_translate("MainWindow", "Empty Circuit"))
        self.checkBox_yuklu.setText(_translate("MainWindow", "Loaded"))
        self.pushButton.setText(_translate("MainWindow", "Right"))
        self.pushButton.clicked.connect(self.clickMethod)

    def qrCall(self,mesaj):
        self.plainTextEdit.appendPlainText(str(mesaj))
        
    def qr_yaz(self):
        """
        file=open("QR","r")
        for x in file:
            print(x)
            self.plainTextEdit.appendPlainText(x)
        """   
    
    def hizCall(self,mesaj):
        for e in mesaj.data:
            if  not sip.isdeleted(self.label_hiz):
                self.label_hiz.setText(str(e))
        
    def clickMethod(self):
        self.navigasyon=self.lineEdit.text()
        self.pub.publish(self.navigasyon)
        
    def bateryCall(self,mesaj):
        batarya=str(mesaj).split(' ')
        batarya1=batarya[1].strip('"')
        if  not sip.isdeleted(self.label_battery):
            self.label_battery.setText(batarya1)
        
        deger=float(batarya1.strip('%'))
        if deger<25.0:
            if not sip.isdeleted(self.comboBox):
                self.comboBox.setHidden(False)
                self.comboBox.setItemText(0, "Productive mod")
                self.comboBox.setItemText(1, "Safe Mod")
            
    def odomCallback(self,mesaj):
        x = str(round(mesaj.pose.pose.position.x,4))
        y = str(round(mesaj.pose.pose.position.y,4))
        x = x +" "+ y
        if  not sip.isdeleted(self.label_konum):
            self.label_konum.setText(x)
        
    def panelCall(self,mesaj):
        t1=time.time()
        current=t1-start
        if mesaj:
            self.label_fair.setText("Obstacle encountered. Waiting time..")
            if current<=15:
                time = 15-current
                time = str(time)
                time = "00:00:"+time
                if  not sip.isdeleted(self.label_saat_sure):
                    self.label_saat_sure.setText(time)
        else:
            if  not sip.isdeleted(self.label_fair):
                self.label_fair.setText("Linetarcking..")
                self.label_fair.setText("")
            if  not sip.isdeleted(self.label_saat_sure):
                    self.label_saat_sure.setText("00:00:15")

            
    def buzzerCall(self,mesaj):
        if mesaj:
            if  not sip.isdeleted(self.label_buzzer):
                self.label_buzzer.setPixmap(QtGui.QPixmap(":/icons/icons/uyarirm.png"))
                self.label_buzzer.setScaledContents(True)
        else:
            if  not sip.isdeleted(self.label_buzzer):
                self.label_buzzer.setPixmap(QtGui.QPixmap(":/icons/icons/uyarii.png"))
                self.label_buzzer.setScaledContents(True)
            
    def akimCall(self,mesaj):
        a=str(mesaj).split(' ')
        b=float(a[1])
        if  not sip.isdeleted(self.label_akim):
            self.label_akim.setText("13.2")
        

    
    def mapCallback(self,mesaj):
        from PyQt5.QtGui import QImage
        from PyQt5.QtGui import QColor
        np_data = np.array([_color_converter(e) for e in mesaj.data])
#
#        
        reshaped = np.flipud(np.reshape(np_data, (mesaj.info.height, mesaj.info.width)))
               
        for i in range(0,len(reshaped)):
            for j in range(0,len(reshaped)):
                print("")
                reshaped[i][j] = round(reshaped[i][j]*255)
        
        width = 401
        height = 831
        dim = (width,height)
        reshaped=cv2.resize(reshaped,dim,interpolation = cv2.INTER_AREA)
        reshaped = cv2.rotate(reshaped,cv2.ROTATE_90_COUNTERCLOCKWISE)
        
        #cv2.imshow("teast",reshaped)
        reshaped = np.float32(reshaped)
        
        
        #cv2.imshow("test",reshaped)
        
        qimg = QtGui.QImage(reshaped.data, reshaped.shape[1], reshaped.shape[0], QImage.Format_RGB32)
       
        pixmap01 = QtGui.QPixmap.fromImage(qimg)
        pixmap_img = QtGui.QPixmap(pixmap01)
        self.label_map.setPixmap(pixmap_img)
        self.label_map.setAlignment(QtCore.Qt.AlignCenter)
        self.label_map.setScaledContents(True)
        self.label_map.setMinimumSize(1,1)
        if  not sip.isdeleted(self.label_map):
            self.label_map.show()
        
    def kameracall(self,mesaj):
        
        from PyQt5.QtGui import QImage
        global clock
        global start_time
        if clock:
            start_time = time.time()
            clock = False
        current_time = time.time()
        elapsed = current_time - start_time
        dakika = int(elapsed/60)
        saniye = str(int(elapsed-(dakika*60)))
        dakika = str(dakika)
        zaman = dakika +":"+saniye
        
        if  not sip.isdeleted(self.lcdNumber):
            self.lcdNumber.display(zaman)
 
        
        img=self.bridge.compressed_imgmsg_to_cv2(mesaj,"bgr8")
        image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        #Flipped = cv2.flip(image,1)
        qimg = QtGui.QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap01 = QtGui.QPixmap.fromImage(qimg)
        pixmap_img = QtGui.QPixmap(pixmap01)
        self.label_cam.setPixmap(pixmap_img)
        self.label_cam.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cam.setScaledContents(True)
        self.label_cam.setMinimumSize(1,1)
        if  not sip.isdeleted(self.label_cam):
            self.label_cam.show()
        
        
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    rospy.spin()
