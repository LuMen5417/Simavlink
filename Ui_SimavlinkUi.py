# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator.2013-20160524CL\Desktop\Simavlink\SimavlinkUi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from src import freqSerial
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QColor
from mavlink import *
from Mythread import *
import time
import threading


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(727, 523)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(727, 523))
        Dialog.setMaximumSize(QtCore.QSize(727, 523))
        Dialog.setSizeGripEnabled(True)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 10, 480, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(5, 15, 10, 230))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(10, 240, 480, 10))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(485, 15, 10, 230))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(500, 15, 10, 230))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(505, 10, 210, 10))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(505, 240, 210, 10))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Dialog)
        self.line_8.setGeometry(QtCore.QRect(710, 15, 10, 230))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(Dialog)
        self.line_9.setGeometry(QtCore.QRect(10, 250, 705, 10))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(Dialog)
        self.line_10.setGeometry(QtCore.QRect(5, 255, 10, 260))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(Dialog)
        self.line_11.setGeometry(QtCore.QRect(10, 510, 705, 10))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(Dialog)
        self.line_12.setGeometry(QtCore.QRect(710, 255, 10, 260))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(510, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(220, 60, 71, 31))
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 60, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 190, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 190, 41, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(175, 190, 41, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 190, 41, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(285, 190, 41, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(165, 190, 16, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(220, 190, 16, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(275, 190, 16, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 160, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(510, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(610, 70, 71, 31))
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(510, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(610, 110, 71, 31))
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(690, 70, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(690, 110, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")

        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(510, 150, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")

        self.radioButton_1 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_1.setGeometry(QtCore.QRect(621, 150, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_1")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 190, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(20, 350, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(190, 350, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(120, 100, 171, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.line_13 = QtWidgets.QFrame(Dialog)
        self.line_13.setGeometry(QtCore.QRect(10, 140, 480, 10))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(20, 400, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(190, 400, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(20, 450, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(190, 450, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")

        self.label_sys = QtWidgets.QLabel(Dialog)
        self.label_sys.setGeometry(QtCore.QRect(131, 260, 50, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_sys.setFont(font)
        self.label_sys.setObjectName("label_sys")

        self.lineEdit_sys = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_sys.setGeometry(QtCore.QRect(181, 260, 40, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_sys.setFont(font)
        self.lineEdit_sys.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_sys.setObjectName("lineEdit_sys")

        self.label_comp = QtWidgets.QLabel(Dialog)
        self.label_comp.setGeometry(QtCore.QRect(226, 260, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_comp.setFont(font)
        self.label_comp.setObjectName("label_sys")

        self.lineEdit_comp = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_comp.setGeometry(QtCore.QRect(296, 260, 40, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_comp.setFont(font)
        self.lineEdit_comp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_comp.setObjectName("lineEdit_sys")

        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(90, 350, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(260, 350, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(90, 400, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(260, 400, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_12.setGeometry(QtCore.QRect(90, 450, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_13.setGeometry(QtCore.QRect(260, 450, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(20, 300, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")

        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(90, 300, 171, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")

        self.line_14 = QtWidgets.QFrame(Dialog)
        self.line_14.setGeometry(QtCore.QRect(360, 255, 10, 260))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(380, 260, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(380, 300, 321, 192))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.serial0 = None
        self.label_serial0connect_true = 0
        self.mythread = MyThread()
        self.send_flag = False

        self.pushButton.clicked.connect(self.serialconnect)
        self.pushButton_3.clicked.connect(self.sendbutton)
        self.t = None
        self.thread_stop = False

        self.t_browser = None
        self.mavlink_message = ''
        self.msgInterval = 0
        self.sendNum = 1

        self.mavlink_arg0 = 0
        self.mavlink_arg1 = 0
        self.mavlink_arg2 = 0
        self.mavlink_arg3 = 0
        self.mavlink_arg4 = 0
        self.mavlink_arg5 = 0
        self.sendmsg_hex = []
        self.sendmsg_num = 0

    def serialconnect(self):
        if self.label_serial0connect_true != 1:
            serialNum = self.spinBox.value()
            COM = "COM" + str(serialNum)
            baudrate = self.comboBox_3.currentText()
            try:
                baudrate = int(baudrate)
                print("COM:%s,baudrate:%s" % (COM, baudrate))
                self.serial0 = freqSerial.connect_serial(COM, baudrate)
            except Exception as e:
                print(repr(e))
                QMessageBox.warning(Dialog, "警告",
                                    "串口波特率不对", QMessageBox.Yes)
                self.serial0 = None

            if self.serial0 is not None:
                self.label_serial0connect_true = 1

            if self.label_serial0connect_true == 0:
                QMessageBox.warning(None, "警告", "打开串口失败", QMessageBox.Yes)
            else:
                self.pushButton.setText("连接成功")

                self.t_browser = threading.Thread(target=self.thread_browser)
                self.t_browser.start()
        else:
            self.serial0.close()
            self.serial0 = None
            self.label_serial0connect_true = 0
            self.pushButton.setText("连接")

    def mavlinkSet(self):
        self.mavlink_message = self.comboBox_4.currentText()

        if self.lineEdit_8.text() != '':
            self.mavlink_arg0 = int(self.lineEdit_8.text())

        if self.lineEdit_9.text() != '':
            self.mavlink_arg1 = int(self.lineEdit_9.text())

        if self.lineEdit_10.text() != '':
            self.mavlink_arg2 = int(self.lineEdit_10.text())

        if self.lineEdit_11.text() != '':
            self.mavlink_arg3 = int(self.lineEdit_11.text())

        if self.lineEdit_12.text() != '':
            self.mavlink_arg4 = int(self.lineEdit_12.text())

        if self.lineEdit_13.text() != '':
            self.mavlink_arg5 = int(self.lineEdit_13.text())

    def sendSet(self):
        if self.lineEdit_6.text() != '':
            self.sendNum = int(self.lineEdit_6.text())

        if self.lineEdit_7.text() != '':
            self.msgInterval = int(self.lineEdit_7.text())

        self.circle_flag = self.radioButton.isChecked()

    def mavlinkInit(self, SendCallfunc, flag):
        if flag == "send":
            fp = open("mavlink_send.log", "wb")
        if flag == "recv":
            fp = open("mavlink_recv.log", "wb")
        self.mavlink = MAVLink(file=fp, srcSystem=1, srcComponent=0)
        self.mavlink.set_send_callback(SendCallfunc)

        if self.lineEdit_sys.text() != '':
            self.mavlink.srcSystem = int(self.lineEdit_sys.text())

        if self.lineEdit_comp.text() != '':
            self.mavlink.srcComponent = int(self.lineEdit_comp.text())

    def mavlinkSend(self, mavlink_message, arg0, arg1, arg2, arg3, arg4, arg5):
        if mavlink_message == "heartbeat":
            self.mavlink.heartbeat_send(arg0, arg1, arg2, arg3, arg4, arg5)

        if mavlink_message == "ping":
            tm = time.time()
            tm = int(tm * 1000000)
            arg0 = tm
            print("tm:", tm)
            seq = arg1
            self.ping_msg = [arg0, seq]
            self.mavlink.ping_send(arg0, arg1, arg2, arg3, arg4)

        if mavlink_message == "file_transfer_protocol":
            data = range(251)
            data = list(data)
            data = bytes(data)
            self.mavlink.file_transfer_protocol_send(arg0, arg1, arg2, data)

    def serialcallfunc(self, mavmsg):
        byte_array = mavmsg.get_msgbuf()
        hex_list = []
        head_msg = b'\xFA\xFF\x32\x48'
        buf = head_msg + byte_array[1:]

        hex_array = list(buf)

        for i in hex_array:
            byte_hex = hex(i)
            if len(byte_hex) == 3:
                byte_hex = byte_hex.replace('x', 'x0')
            hex_list.append(byte_hex)

        print("msg:", hex_list)

        self.serial0.write(buf)

    def sendbutton(self):
        self.SendCallfunc = None

        if self.serial0 != None:
            self.SendCallfunc = self.serialcallfunc

        if self.SendCallfunc == None:
            QMessageBox.warning(None, "警告", "发送失败, 发送方式没有设置！", QMessageBox.Yes)
            return None

        self.mavlinkSet()
        self.sendSet()

        if self.msgInterval <= 0:
            QMessageBox.warning(None, "警告", "发送失败, 报文间隔设置错误！", QMessageBox.Yes)
            return None

        self.mavlinkInit(self.SendCallfunc, "send")
        if self.send_flag == False:
            self.t = threading.Thread(target=self.thread_send)
            self.t.start()
            self.thread_stop = False
            self.send_flag = True
            self.pushButton_3.setText("正在发送")
        else:
            print("Thread stop!")
            self.thread_stop = True
            self.send_flag = False
            self.pushButton_3.setText("发送")

    def thread_send(self):
        if self.circle_flag == True:
            while True:
                if self.thread_stop == True:
                    break

                self.mavlinkSend(self.mavlink_message, self.mavlink_arg0,
                                 self.mavlink_arg1, self.mavlink_arg2,
                                 self.mavlink_arg3, self.mavlink_arg4,
                                 self.mavlink_arg5)
                time.sleep(self.msgInterval / 1000)

                print("continue thread send the msg!")
        else:
            for i in range(self.sendNum):
                if self.thread_stop == True:
                    break
                self.mavlinkSend(self.mavlink_message, self.mavlink_arg0,
                                 self.mavlink_arg1, self.mavlink_arg2,
                                 self.mavlink_arg3, self.mavlink_arg4,
                                 self.mavlink_arg5)

                self.sendmsg_num = i + 1
                print("thread send the msg:", i)
                #self.textBrowser.append("thread send the msg:%d" % i)
                time.sleep(self.msgInterval / 1000)

        self.thread_stop = False
        self.send_flag = False
        self.pushButton_3.setText("发送")

    def thread_browser(self):
        text = ""
        ping_flag = 0
        delay_tm = 0
        recv_msg = 0
        list_hex = []

        while True:
            if self.serial0 == None or self.label_serial0connect_true == 0:
                break

            if self.serial0.isOpen():
                try:
                    n = self.serial0.inWaiting()
                    byte_char = self.serial0.read(n)
                    #text = str(byte_char, encoding="utf-8")
                    list_hex = list(byte_char)

                    if self.mavlink_message != "ping" and self.radioButton_1.isChecked() and list_hex != []:
                        recv_msg += 1

                    if self.mavlink_message == "ping" and list_hex != []:

                        if list_hex[-4] == 0:
                            self.mavlinkInit(self.SendCallfunc, "recv")
                            tm = time.time()
                            tm = int(tm * 1000000)
                            arg0 = tm
                            arg1 = 1

                            self.mavlinkSend("ping", arg0, arg1, 1, 0, 0, 0)

                        if list_hex[-4] == 1:
                            ping_flag = 1
                            recv_tm = time.time()
                            recv_tm = int(recv_tm * 1000000)

                            delay_tm = recv_tm - self.ping_msg[0]

                    for i in list_hex:
                        byte_hex = hex(i)
                        if len(byte_hex) == 3:
                            byte_hex = byte_hex.replace('x', 'x0')

                        text += byte_hex + " "
                except Exception as e:
                    print(repr(e))
                    break

            if text != "":
                if ping_flag == 1:
                    self.textBrowser.append(
                        "接收报文: 类型-ping 延时- %d us" % delay_tm)
                else:
                    self.textBrowser.append("接收报文:")

                text += "\n"
                self.textBrowser.append(text)

                if ping_flag != 1:
                    self.textBrowser.append(
                        "===================================")
                    self.textBrowser.append("环回报告:")
                    self.textBrowser.append("发送报文 - %d" % self.sendmsg_num)
                    self.textBrowser.append("接收报文 - %d" % recv_msg)
                    self.textBrowser.append(
                        "===================================\n")

            # time.sleep(0.1)

            text = ""
        self.sendmsg_num = 0

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Simavlink_v1.7"))
        self.label.setText(_translate("Dialog", "串口配置"))
        self.label_2.setText(_translate("Dialog", "Mavlink配置"))
        self.label_3.setText(_translate("Dialog", "发送配置"))
        self.label_4.setText(_translate("Dialog", "串口号："))
        self.label_5.setText(_translate("Dialog", "波特率："))
        self.pushButton.setText(_translate("Dialog", "连接"))
        self.label_6.setText(_translate("Dialog", "网口配置"))
        self.label_7.setText(_translate("Dialog", "网口地址："))
        self.label_8.setText(_translate("Dialog", "."))
        self.label_9.setText(_translate("Dialog", "."))
        self.label_10.setText(_translate("Dialog", "."))
        self.pushButton_2.setText(_translate("Dialog", "测试"))
        self.label_11.setText(_translate("Dialog", "报文个数："))
        self.label_12.setText(_translate("Dialog", "报文间隔："))
        self.label_13.setText(_translate("Dialog", "个"))
        self.label_14.setText(_translate("Dialog", "ms"))
        self.radioButton.setText(_translate("Dialog", "连续发包"))
        self.radioButton_1.setText(_translate("Dialog", "环回检查"))
        self.pushButton_3.setText(_translate("Dialog", "发送"))
        self.label_15.setText(_translate("Dialog", "arg_0："))
        self.label_16.setText(_translate("Dialog", "arg_1："))
        self.comboBox_3.setItemText(0, _translate("Dialog", "9600"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "38400"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "57600"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "115200"))
        self.label_17.setText(_translate("Dialog", "arg_2："))
        self.label_18.setText(_translate("Dialog", "arg_3："))
        self.label_19.setText(_translate("Dialog", "arg_4："))
        self.label_20.setText(_translate("Dialog", "arg_5："))
        self.label_21.setText(_translate("Dialog", "报文："))
        self.comboBox_4.setItemText(0, _translate("Dialog", "heartbeat"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "ping"))
        self.comboBox_4.setItemText(2, _translate(
            "Dialog", "file_transfer_protocol"))
        self.label_22.setText(_translate("Dialog", "Mavlink报文接收"))
        self.label_sys.setText(_translate("Dialog", "SysID:"))
        self.label_comp.setText(_translate("Dialog", "CompID:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
