#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot_kontrol.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


#from nav_msgs.msg import Odometry
#from sensor_msgs.msg import Image
#from cv_bridge import CvBridge
from PyQt5 import QtCore, QtGui, QtWidgets
#import rospy
import numpy
#import cv2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1138, 732)
        MainWindow.setStyleSheet("#central_widget{\n"
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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(9, 9, 281, 261))
        self.widget.setStyleSheet("#widget{\n"
"    background-color: rgb(0,0,0);\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 141, 131))
        self.frame_3.setStyleSheet("#frame_3{\n"
"    background-color: rgb(28, 26, 29);\n"
"border-color: rgb(186, 189, 182);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/icons/circlee.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_sicaklik = QtWidgets.QLabel(self.frame_3)
        self.label_sicaklik.setGeometry(QtCore.QRect(40, 50, 71, 41))
        self.label_sicaklik.setStyleSheet("font: 75 22pt \"Ubuntu Mono\";\n"
"color: rgb(245, 72, 217)")
        self.label_sicaklik.setObjectName("label_sicaklik")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(70, 50, 71, 31))
        self.label_17.setStyleSheet("font: 75 22pt \"Ubuntu Mono\";\n"
"color: rgb(245, 72, 217)")
        self.label_17.setObjectName("label_17")
        self.frame_5 = QtWidgets.QFrame(self.widget)
        self.frame_5.setGeometry(QtCore.QRect(0, 130, 141, 131))
        self.frame_5.setStyleSheet("#frame_5{\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(28, 26, 29);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/circlee.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_hiz = QtWidgets.QLabel(self.frame_5)
        self.label_hiz.setGeometry(QtCore.QRect(60, 30, 91, 41))
        self.label_hiz.setStyleSheet("font: 75 22pt \"Ubuntu Mono\";\n"
"color:rgb(247, 157, 17)")
        self.label_hiz.setObjectName("label_hiz")
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setGeometry(QtCore.QRect(40, 70, 81, 31))
        self.label_19.setStyleSheet("font: 75 22pt \"Ubuntu Mono\";\n"
"color:rgb(247, 157, 17)")
        self.label_19.setObjectName("label_19")
        self.frame_6 = QtWidgets.QFrame(self.widget)
        self.frame_6.setGeometry(QtCore.QRect(140, 0, 141, 131))
        self.frame_6.setStyleSheet("#frame_6{\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(28, 26, 29);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(0, 10, 121, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/circlee.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_akim = QtWidgets.QLabel(self.frame_6)
        self.label_akim.setGeometry(QtCore.QRect(40, 50, 51, 31))
        self.label_akim.setStyleSheet("font: 75 22pt \"Ubuntu Mono\";\n"
"color:rgb(10, 21, 244);")
        self.label_akim.setObjectName("label_akim")
        self.frame_7 = QtWidgets.QFrame(self.widget)
        self.frame_7.setGeometry(QtCore.QRect(140, 130, 141, 131))
        self.frame_7.setStyleSheet("#frame_7{\n"
"    border-color: rgb(186, 189, 182);\n"
"background-color: rgb(28, 26, 29);\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setGeometry(QtCore.QRect(0, 10, 121, 121))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/icons/circlee.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_yuk = QtWidgets.QLabel(self.frame_7)
        self.label_yuk.setGeometry(QtCore.QRect(40, 40, 71, 41))
        self.label_yuk.setStyleSheet("font: 75 22pt \"Ubuntu Mono\";\n"
"color: rgb(53, 235, 25)")
        self.label_yuk.setObjectName("label_yuk")
        self.label_20 = QtWidgets.QLabel(self.frame_7)
        self.label_20.setGeometry(QtCore.QRect(40, 70, 71, 41))
        self.label_20.setStyleSheet("font: 75 22pt \"Ubuntu Mono\";\n"
"color: rgb(53, 235, 25)")
        self.label_20.setObjectName("label_20")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(290, 10, 841, 261))
        self.widget_2.setStyleSheet("#widget_2{\n"
"    background-color: rgb(0,0,0);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.frame_4 = QtWidgets.QFrame(self.widget_2)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 311, 261))
        self.frame_4.setStyleSheet("#frame_4{\n"
"    background-color: rgb(28, 26, 29);\n"
"    \n"
"    background-image: url(:/icons/icons/imu-removebg-preview(1).png);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.line = QtWidgets.QFrame(self.frame_4)
        self.line.setGeometry(QtCore.QRect(110, 80, 101, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame_4)
        self.line_2.setGeometry(QtCore.QRect(125, 105, 71, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame_4)
        self.line_3.setGeometry(QtCore.QRect(110, 118, 101, 31))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame_4)
        self.line_4.setGeometry(QtCore.QRect(125, 150, 71, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame_4)
        self.line_5.setGeometry(QtCore.QRect(110, 165, 101, 31))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.frame_4)
        self.line_6.setGeometry(QtCore.QRect(125, 195, 71, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.frame_4)
        self.line_7.setGeometry(QtCore.QRect(110, 40, 101, 31))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.frame_4)
        self.line_8.setGeometry(QtCore.QRect(125, 65, 71, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.frame_4)
        self.line_9.setGeometry(QtCore.QRect(110, 210, 101, 31))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.frame_4)
        self.line_10.setGeometry(QtCore.QRect(125, 240, 71, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setGeometry(QtCore.QRect(30, -40, 261, 261))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icons/icons/hizzrm.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(80, 170, 21, 17))
        self.label_13.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Ubuntu Condensed\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(80, 210, 21, 17))
        self.label_14.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Ubuntu Condensed\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(90, 90, 21, 17))
        self.label_15.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Ubuntu Condensed\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(90, 130, 21, 17))
        self.label_16.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Ubuntu Condensed\";")
        self.label_16.setObjectName("label_16")
        self.frame_9 = QtWidgets.QFrame(self.widget_2)
        self.frame_9.setGeometry(QtCore.QRect(590, 0, 251, 261))
        self.frame_9.setStyleSheet("#frame_9{\n"
"background-color: rgb(28, 26, 29);\n"
"}\n"
"")
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 191, 21))
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
        self.widget_4 = QtWidgets.QWidget(self.frame_9)
        self.widget_4.setGeometry(QtCore.QRect(20, 50, 201, 91))
        self.widget_4.setObjectName("widget_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget_4)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 10, 201, 61))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_8 = QtWidgets.QLabel(self.frame_9)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 241, 31))
        self.label_8.setStyleSheet("font: 75 13pt \"Ubuntu Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName("label_8")
        self.label_konum = QtWidgets.QLabel(self.frame_9)
        self.label_konum.setGeometry(QtCore.QRect(20, 180, 211, 61))
        self.label_konum.setStyleSheet("font: 75 14pt \"Ubuntu Mono\";\n"
"color: rgb(0, 255, 0);")
        self.label_konum.setObjectName("label_konum")
        self.frame_8 = QtWidgets.QFrame(self.widget_2)
        self.frame_8.setGeometry(QtCore.QRect(310, 0, 281, 261))
        self.frame_8.setStyleSheet("#frame_8{\n"
"    border-color: rgb(186, 189, 182);\n"
"background-color: rgb(28, 26, 29);\n"
"}\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(10, 270, 281, 411))
        self.widget_3.setStyleSheet("#widget_3{\n"
"background-color: rgb(28, 26, 29);\n"
"}\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(150, 40, 101, 41))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/icons/icons/batteryyrm.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_buzzer = QtWidgets.QLabel(self.widget_3)
        self.label_buzzer.setGeometry(QtCore.QRect(150, 120, 91, 91))
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
        self.btn_lock.setGeometry(QtCore.QRect(30, 130, 81, 61))
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
        self.label_battery.setGeometry(QtCore.QRect(180, 50, 51, 20))
        self.label_battery.setStyleSheet("font: 75 18pt \"Ubuntu Mono\";\n"
"color: rgb(253, 252, 255);")
        self.label_battery.setTextFormat(QtCore.Qt.PlainText)
        self.label_battery.setScaledContents(False)
        self.label_battery.setObjectName("label_battery")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(30, 190, 91, 20))
        self.label_7.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"color: rgb(253, 252, 255);")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(170, 190, 51, 17))
        self.label_9.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"color: rgb(253, 252, 255);")
        self.label_9.setObjectName("label_9")
        self.frame_2 = QtWidgets.QFrame(self.widget_3)
        self.frame_2.setGeometry(QtCore.QRect(10, 260, 251, 121))
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
        self.label_12.setGeometry(QtCore.QRect(160, 240, 81, 20))
        self.label_12.setStyleSheet("font: 57 10pt \"Ubuntu\";\n"
"color: rgb(253, 252, 255);")
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(240, 240, 21, 21))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/icons/icons/radiows.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.comboBox = QtWidgets.QComboBox(self.widget_3)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(160, 80, 81, 21))
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 87, 83);\n"
"font: 75 italic 10pt \"Ubuntu Condensed\";")
        self.comboBox.setFrame(True)
        self.comboBox.setModelColumn(0)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1138, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #rospy.init_node("arayuz")
        #rospy.Subscriber("odom",Odometry,self.odomCallback)
        #rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        #self.bridge=CvBridge()
        #rospy.spin()
        
        MainWindow.setWindowTitle(_translate("MainWindow", "KOU Rover"))
        self.label_sicaklik.setText(_translate("MainWindow", "25"))
        self.label_17.setText(_translate("MainWindow", "°C"))
        self.label_hiz.setText(_translate("MainWindow", "5"))
        self.label_19.setText(_translate("MainWindow", "km/h"))
        self.label_akim.setText(_translate("MainWindow", "5V"))
        self.label_yuk.setText(_translate("MainWindow", "25"))
        self.label_20.setText(_translate("MainWindow", "kg"))
        self.label_13.setText(_translate("MainWindow", "-10"))
        self.label_14.setText(_translate("MainWindow", "-20"))
        self.label_15.setText(_translate("MainWindow", "10"))
        self.label_16.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "LOCATİON DATA:"))
        self.label_8.setText(_translate("MainWindow", "Vehicle Mission Time Period:"))
        #self.label_konum.setText(_translate("MainWindow", "40.0078 40.00876"))
        self.label_battery.setText(_translate("MainWindow", "%45"))
        self.label_7.setText(_translate("MainWindow", "Security Lock"))
        self.label_9.setText(_translate("MainWindow", "Caution"))
        self.label_fair.setText(_translate("MainWindow", "engel tespit edildi"))
        self.label_saat_sure.setText(_translate("MainWindow", "00:00:15"))
        self.label_12.setText(_translate("MainWindow", "Fair Safe Mod"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Stop Mod"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Stop Mod"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Low Power"))
        
        
   
   #def odomCallback(self,mesaj):
    #    x = str(round(mesaj.pose.pose.position.x,4))
     #   y = str(round(mesaj.pose.pose.position.y,4))
      #  x = x +" "+ y
       # self.label_konum.setText(x)
        
   # def kameraCallback(self,mesaj1):
    #    self.foto=self.bridge.imgmsg_to_cv2(mesaj1,"bgr8")
     #   cv2.imshow(f"TO: {frame_8}",self.foto)
      #  cv2.waitKey(1)
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
