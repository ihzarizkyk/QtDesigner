'''
Author : Mochammad Ihza Rizky Karim 
'''

from PyQt5 import QtWidgets
from ui_login import Ui_Login
from c_home import C_Home

class C_Login(QtWidgets.QMainWindow, Ui_Login):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()

		self.login.clicked.connect(self.login_clicked)
		self.reset.clicked.connect(self.reset_clicked)

	def login_clicked(self):

		user = self.username.text()
		passwords = self.password.text()

		if(user == "ihzarizkyk" and passwords == "12354"):
			self.form = C_Home()
			self.form.show()
			self.close()
		else:
			print("PASSWORD SALAH")

	def reset_clicked(self):
		self.username.setText("")
		self.password.setText("")
