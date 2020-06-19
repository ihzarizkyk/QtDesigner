# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        Form.setMinimumSize(QtCore.QSize(640, 480))
        Form.setMaximumSize(QtCore.QSize(640, 480))
        Form.setStyleSheet("*{\n"
"background:#fff;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 40, 501, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../gambar/ngobrolin1.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.logout = QtWidgets.QPushButton(Form)
        self.logout.setGeometry(QtCore.QRect(230, 310, 161, 41))
        self.logout.setStyleSheet("background:red;\n"
"font-size:15px;\n"
"font-weight:bold;\n"
"color:white;")
        self.logout.setFlat(False)
        self.logout.setObjectName("logout")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.logout.setText(_translate("Form", "KELUAR"))
