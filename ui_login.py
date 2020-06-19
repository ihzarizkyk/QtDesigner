# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        Form.setMinimumSize(QtCore.QSize(640, 480))
        Form.setMaximumSize(QtCore.QSize(640, 480))
        Form.setStyleSheet("*{\n"
"background: #000;\n"
"}\n"
"\n"
"QLineEdit{\n"
"font-size:20px;\n"
"}")
        self.welcome = QtWidgets.QLabel(Form)
        self.welcome.setGeometry(QtCore.QRect(10, 10, 621, 61))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.welcome.setFont(font)
        self.welcome.setStyleSheet("background:#fff;")
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.setObjectName("welcome")
        self.notice = QtWidgets.QLabel(Form)
        self.notice.setGeometry(QtCore.QRect(130, 80, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.notice.setFont(font)
        self.notice.setStyleSheet("background:yellow;")
        self.notice.setAlignment(QtCore.Qt.AlignCenter)
        self.notice.setObjectName("notice")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 210, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background:#fff;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 300, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:#fff;")
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(190, 200, 321, 41))
        self.username.setStyleSheet("background:#fff;\n"
"border-radius:15px;")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(190, 290, 321, 41))
        self.password.setStyleSheet("background:#fff;\n"
"border-radius:15px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(200, 400, 131, 41))
        self.login.setStyleSheet("background:green;\n"
"font-size:15px;\n"
"font-weight:bold;")
        self.login.setObjectName("login")
        self.reset = QtWidgets.QPushButton(Form)
        self.reset.setGeometry(QtCore.QRect(370, 400, 131, 41))
        self.reset.setStyleSheet("background:red;\n"
"font-size:15px;\n"
"font-weight:bold;")
        self.reset.setObjectName("reset")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.welcome.setText(_translate("Form", "SELAMAT DATANG"))
        self.notice.setText(_translate("Form", "Masukkan Username dan Password Anda"))
        self.label.setText(_translate("Form", "USERNAME"))
        self.label_2.setText(_translate("Form", "PASSWORD"))
        self.login.setText(_translate("Form", "LOGIN"))
        self.reset.setText(_translate("Form", "RESET"))
