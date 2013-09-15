# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'servo_gui.ui'
#
# Created: Sun Sep 15 02:04:48 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(378, 117)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.left = QtGui.QPushButton(self.centralwidget)
        self.left.setObjectName(_fromUtf8("left"))
        self.horizontalLayout.addWidget(self.left)
        self.right = QtGui.QPushButton(self.centralwidget)
        self.right.setObjectName(_fromUtf8("right"))
        self.horizontalLayout.addWidget(self.right)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Servo controller", None))
        self.left.setText(_translate("MainWindow", "Left", None))
        self.left.setShortcut(_translate("MainWindow", "Left", None))
        self.right.setText(_translate("MainWindow", "Right", None))
        self.right.setShortcut(_translate("MainWindow", "Right", None))
        self.label.setText(_translate("MainWindow", "x", None))

