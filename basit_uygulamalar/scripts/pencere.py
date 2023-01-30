#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 04:38:45 2022

@author: kutay
"""

import sys
from PyQt5 import QtWidgets,QtCore

def arayuz():
    nesne = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    
    pencere.setWindowTitle("PyQt5 arayüz")
    pencere.setGeometry(250,100,600,300)
    
    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)
    etiket1.setText("konum x")
    etiket2.setText("konum y")
    
    satir1= QtWidgets.QLineEdit(pencere)
    satir2= QtWidgets.QLineEdit(pencere)
    
    mizanpaj = QtWidgets.QFormLayout()
    mizanpaj.addRow(etiket1,satir1)
    mizanpaj.addRow(etiket2,satir2)
    
    pencere.setLayout(mizanpaj)
    
    
    '''
    buton1 = QtWidgets.QPushButton(pencere)
    buton2 = QtWidgets.QPushButton(pencere)
    buton3 = QtWidgets.QPushButton(pencere)
    buton4 = QtWidgets.QPushButton(pencere)
    buton1.setText("1")
    buton2.setText("2")
    buton3.setText("3")
    buton4.setText("4")
    
    mizanpaj = QtWidgets.QGridLayout()
    
    mizanpaj.addWidget(buton1,1,1)
    mizanpaj.addWidget(buton2,1,2)
    mizanpaj.addWidget(buton3,2,1)
    mizanpaj.addWidget(buton4,2,2)
    pencere.setLayout(mizanpaj)
    
    
    satir = QtWidgets.QLineEdit(pencere)
    satir.setReadOnly(True)
    buton = QtWidgets.QPushButton(pencere)
    buton.move(0,20)
    buton.setText("Gonder")
    def guncelle():
        satir.setText("1.22")
    buton.clicked.connect(guncelle)
    
    
    
    
    slider = QtWidgets.QSlider(QtCore.Qt.Horizontal,pencere)
    slider.move(300,150)
    slider.setMinimum(0)
    slider.setMaximum(10)
    slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
    slider.setTickInterval(2)
    slider.setValue(8)
    

    spin = QtWidgets.QDoubleSpinBox(pencere)
    spin.setRange(5,25)
    spin.setSingleStep(0.05)
    
    
    combo = QtWidgets.QComboBox(pencere)
    combo.addItem("scan")
    combo.addItem("odom")
    combo.addItem("cmd_vel")
    
    print(combo.count())
    
    combo.setItemText(2,"kamera")
    
    kontrol1 = QtWidgets.QCheckBox(pencere)
    kontrol2 = QtWidgets.QCheckBox(pencere)
    kontrol3 = QtWidgets.QCheckBox(pencere)
    
    kontrol1.setText("1")
    kontrol2.setText("2")
    kontrol3.setText("3")
    
    kontrol1.move(100,50)
    kontrol2.move(100,70)
    kontrol3.move(100,90)
    
    radio1 = QtWidgets.QRadioButton(pencere)
    radio2 = QtWidgets.QRadioButton(pencere)
    radio3 = QtWidgets.QRadioButton(pencere)
    
    radio1.setText("1")
    radio2.setText("2")
    radio3.setText("3")
    
    radio1.move(100,50)
    radio2.move(100,70)
    radio3.move(100,90)
    
    radio3.setCheckable(False)
    
    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Kaydet")
    buton.setEnabled(False)
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Kamera Kontrol")
    etiket.move(300,150)
    satir = QtWidgets.QLineEdit(pencere)
    #satir.setText("2.4")
    #satir.setReadOnly(True)
    satir.setEchoMode(QtWidgets.QLineEdit.Password)'''
    pencere.show()
    sys.exit(nesne.exec_())
    
arayuz()