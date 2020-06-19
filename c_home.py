'''
Author : Mochammad Ihza Rizky Karim 
'''

from PyQt5 import QtWidgets
from ui_home import Ui_Home 
import c_login

class C_Home(QtWidgets.QMainWindow, Ui_Home):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()

		self.logout.clicked.connect(self.logout_pressed)

	def logout_pressed(self):
		self.form = c_login.C_Login()
		self.form.show()
		self.close()	
