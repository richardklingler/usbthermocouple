# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Logger(object):
    def setupUi(self, Logger):
        Logger.setObjectName("Logger")
        Logger.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(Logger)
        self.centralwidget.setObjectName("centralwidget")
        self.button_connect = QtWidgets.QPushButton(self.centralwidget)
        self.button_connect.setGeometry(QtCore.QRect(190, 20, 121, 21))
        self.button_connect.setObjectName("button_connect")
        self.combo_ports = QtWidgets.QComboBox(self.centralwidget)
        self.combo_ports.setGeometry(QtCore.QRect(20, 20, 151, 22))
        self.combo_ports.setObjectName("combo_ports")
        self.check_date = QtWidgets.QCheckBox(self.centralwidget)
        self.check_date.setGeometry(QtCore.QRect(340, 20, 201, 21))
        self.check_date.setObjectName("check_date")
        self.button_date = QtWidgets.QPushButton(self.centralwidget)
        self.button_date.setGeometry(QtCore.QRect(660, 20, 121, 21))
        self.button_date.setObjectName("button_date")
        self.plotter = QtWidgets.QLabel(self.centralwidget)
        self.plotter.setGeometry(QtCore.QRect(20, 90, 760, 360))
        self.plotter.setStyleSheet("color: rgb(239, 41, 41);\n"
"background-color: rgb(186, 189, 182);")
        self.plotter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plotter.setObjectName("plotter")
        self.temp1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.temp1.setGeometry(QtCore.QRect(20, 60, 151, 31))
        self.temp1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.temp1.setDigitCount(6)
        self.temp1.setObjectName("temp1")
        self.temp2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.temp2.setGeometry(QtCore.QRect(190, 60, 151, 31))
        self.temp2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.temp2.setDigitCount(6)
        self.temp2.setObjectName("temp2")
        Logger.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Logger)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 14))
        self.menubar.setObjectName("menubar")
        Logger.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Logger)
        self.statusbar.setObjectName("statusbar")
        Logger.setStatusBar(self.statusbar)

        self.retranslateUi(Logger)
        QtCore.QMetaObject.connectSlotsByName(Logger)

    def retranslateUi(self, Logger):
        _translate = QtCore.QCoreApplication.translate
        Logger.setWindowTitle(_translate("Logger", "USB Thermo Logger"))
        self.button_connect.setText(_translate("Logger", "Connect"))
        self.check_date.setText(_translate("Logger", "Send Date/Time on connect"))
        self.button_date.setText(_translate("Logger", "Date/Time"))
        self.plotter.setText(_translate("Logger", "TextLabel"))
