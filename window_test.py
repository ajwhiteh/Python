#import pymongo
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
	QComboBox, QLabel)
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon


class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'End of Week Log'
		self.left = 10
		self.top = 30
		self.width = 640
		self.height = 480
		self.initUI()
		
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		saw_button = QPushButton('Saw Maintenance', self)
		saw_button.setToolTip('Saws Current condition and location')
		saw_button.move(10,10)
		saw_button.clicked.connect(self.saw_click)
		
		log_button = QPushButton('Saw Logs', self)
		log_button.setToolTip('Previous Saw Logs')
		log_button.move(140,10)
		log_button.clicked.connect(self.log_click)
		
		
		self.show()
	
	def saw_label(self):
		label = QLabel('Saw:', self)
		label.move(100,45)
		return label.show()
		
	
	'''	
	saw_select = QComboBox(self)
	saw_select.move(140,40)
	'''	
	
	def saw_click(self):
		print('saw click')
		label = QLabel('Saw:', self)
		label.move(100,45)
		
	@pyqtSlot()
	def log_click(self):
		print('log click')
		

		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
