import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, 
	QWidget, QAction, QTabWidget, QVBoxLayout, QScrollArea, QGridLayout, QComboBox,
	QGroupBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
 
class App(QMainWindow):
 
	def __init__(self):
		super().__init__()
		self.title = 'Shop Tech'
		self.left = 10
		self.top = 30
		self.width = 640
		self.height = 520
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
 
		self.table_widget = MyTableWidget(self)
		self.setCentralWidget(self.table_widget)
 
		self.show()


class MyTableWidget(QWidget):
 
	def __init__(self, parent):
		super(QWidget, self).__init__(parent)
		self.layout = QVBoxLayout(self)
 
		####Saw Options and Variables
		#saw selection
		self.saw_list = ['S1', 'S2', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12',
			'S15', 'S17', 'S18', 'S19', 'S21', 'S25', 'S27', 'S28', 'S30', 'S250']
		self.saws = QComboBox()
		self.saws.addItems(self.saw_list)
		self.saws.activated.connect(self.saw_select)
		#Starts
		
		#Last date serviced
		
		#Air filter
		
		#Worm gear
		
		#Clutch Drum
		
		#Clutch bearing
		
		#Sprocket
		
		#Chain Catch
		
		#Bar
		
		#Spark Plug
		
		#Caps
		
		#Sliders
		
		#Pull Cord
		
		#Misc
		
 
		# Initialize tab screen
		self.tabs = QTabWidget()
		self.tab1 = self.createTab1()
		self.tab2 = self.createTab2()
		self.tab3 = self.createTab3()
		self.tabs.resize(300,200)
 
		# Add tabs
		self.tabs.addTab(self.tab1,"Saws")
		self.tabs.addTab(self.tab2,"Operations")
		self.tabs.addTab(self.tab3,"Inventory")
 
		# Add tabs to widget
		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)
 
	# Saw information
	def createTab1(self):
		# Tab properties init
		tab = QScrollArea()
		tab.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		tab_widget = QWidget()
		
		# Create first tab
		# Create tabs grid
		tabGrid = QGridLayout()
		tabGrid.addWidget(self.createSawSelect(), 0, 0)
		
		# Set into tab
		tab_widget.setLayout(tabGrid)
		tab.setWidget(tab_widget)
		
		return tab
		
	# Saw operations	
	def createTab2(self):
		tab = QWidget()
		
		# Create second tab
		# Create tabs grid
		tabGrid = QGridLayout()
		
		# Set into tab
		tab.setLayout(tabGrid)
		
		return tab
		
	# Saw Part Inventory
	def createTab3(self):
		tab = QWidget()
		
		# Create second tab
		# Create tabs grid
		tabGrid = QGridLayout()
		
		# Set into tab
		tab.setLayout(tabGrid)
		
		return tab
	
	# Saw Dropdown creation	
	def createSawSelect(self):
		groupBox = QGroupBox("Saw")
		box = QVBoxLayout()
		
		box.addWidget(self.saws)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
		
	@pyqtSlot()
	def saw_select(self):
		saw_num = str(self.saws.currentText())
		print(saw_num)
	
 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
