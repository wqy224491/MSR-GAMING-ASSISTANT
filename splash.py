# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Teddy Wan\Desktop\MSR GAMING ASSISTANT\QTdesign\splash.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashWindow(object):
    def setupUi(self, SplashWindow):
        SplashWindow.setObjectName("SplashWindow")
        SplashWindow.resize(640, 440)
        SplashWindow.setMinimumSize(QtCore.QSize(640, 440))
        SplashWindow.setMaximumSize(QtCore.QSize(640, 440))
        self.centralwidget = QtWidgets.QWidget(SplashWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splash = QtWidgets.QFrame(self.centralwidget)
        self.splash.setGeometry(QtCore.QRect(20, 20, 600, 400))
        self.splash.setStyleSheet("#splash {\n"
"    border-image: url(:/resources/Resources/bg/splash.png);\n"
"}")
        self.splash.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splash.setFrameShadow(QtWidgets.QFrame.Raised)
        self.splash.setObjectName("splash")
        self.splash_progress = QtWidgets.QProgressBar(self.splash)
        self.splash_progress.setGeometry(QtCore.QRect(50, 320, 501, 25))
        self.splash_progress.setMinimumSize(QtCore.QSize(0, 0))
        self.splash_progress.setMaximumSize(QtCore.QSize(600, 25))
        self.splash_progress.setBaseSize(QtCore.QSize(600, 25))
        self.splash_progress.setStyleSheet("#splash_progress  {\n"
"    border-image: url(:/resources/Resources/bg/splash_bar.png)\n"
"}\n"
"")
        self.splash_progress.setProperty("value", 0)
        self.splash_progress.setTextVisible(False)
        self.splash_progress.setObjectName("splash_progress")
        SplashWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashWindow)
        QtCore.QMetaObject.connectSlotsByName(SplashWindow)

    def retranslateUi(self, SplashWindow):
        _translate = QtCore.QCoreApplication.translate
        SplashWindow.setWindowTitle(_translate("SplashWindow", "MainWindow"))
import res_rc
