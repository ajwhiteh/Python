import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon



class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'This Window Title'
		self.left = 10
		self.top = 10
		self.width = 320
		self.height = 200
		self.initUI()
		
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		button = QPushButton('Py button', self)
		button.setToolTip('This is a button')
		button.move(120,75)
		button.clicked.connect(self.on_click)
		
		self.show()
		
	@pyqtSlot()
	def on_click(self):
		print('Button click')
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
