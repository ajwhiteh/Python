import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
	QComboBox, QLabel, QGridLayout, QGroupBox, QRadioButton, QVBoxLayout,
	QCheckBox, QLineEdit, QAction, QFileDialog)
from PyQt5.QtCore import pyqtSlot, Qt, QDate, QTime, QDateTime
from PyQt5.QtGui import QIcon

#application init as class
class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'End of Week Log'
		self.left = 10
		self.top = 30
		self.width = 640
		self.height = 480
		self.wormGroup = QGroupBox("")
		self.initUI()
		
	
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		grid = QGridLayout()
		grid.addWidget(self.createSawGroup(), 0, 0)
		grid.addWidget(self.createBarNumGroup(), 0, 1)
		grid.addWidget(self.createNameGroup(), 0, 2)
		grid.addWidget(self.createDateGroup(), 0, 3)
		grid.addWidget(self.createSAVE(), 0, 5)
		grid.addWidget(self.createStartGroup(), 1, 0)
		grid.addWidget(self.createFilterGroup(), 1, 1)
		grid.addWidget(self.createClutchGroup(), 2, 0)
		grid.addWidget(self.createBaringGroup(), 2, 1)
		grid.addWidget(self.createSprocketGroup(), 1, 3)
		grid.addWidget(self.createChainCatchGroup(), 1, 4)
		self.createWormGroup()
		grid.addWidget(self.wormGroup, 2, 2)
		grid.addWidget(self.createBarGroup(), 1, 5)
		grid.addWidget(self.createSparkGroup(), 2, 3)
		grid.addWidget(self.createCapsGroup(), 2, 4)
		grid.addWidget(self.createSliderGroup(), 1, 2)
		grid.addWidget(self.createPullcordGroup(), 2, 5)
		self.setLayout(grid)
		
		'''
		saveFile = QAction("&Save File", self)
		saveFile.setShortcut("Ctrl+S")
		saveFile.setStatusTip('Save File')
		saveFile.triggered.connect(self.file_save)
		
		fileMenu.addAction(saveFile)
		'''
		
		self.show()
		
	#File saving
	'''
	def file_save(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		name, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
		file = open(name, 'r')
		text = self.docEdit.toPlainText()
		file.write(text)
		file.close()
    '''
    
	def tempDataCollector(self):
		
		for i in range(1,4):
			if self.wormGroup.self.topGroup.radio1.isChecked():
				print ("radio1 " + "is Checked")
        
        
	def createSAVE(self):
		save_button = QPushButton('&Save', self)
		save_button.setToolTip('Save all choices to a log')
		save_button.clicked.connect(self.tempDataCollector)
		
		return save_button
		
	@pyqtSlot()
	def save_click(self):
		print('save click')
		
		
	
	def createSawGroup(self):
		groupBox = QGroupBox("Saw")
		box = QVBoxLayout()
		
		saw_list = ['S1', 'S2']
		
		#saw selection
		saws = QComboBox()
		saws.addItems(saw_list)
		
		box.addWidget(saws)
		box.addStretch(1)

		groupBox.setLayout(box)
		
		return groupBox
		
	def createBarNumGroup(self):
		groupBox = QGroupBox("Bar #")
		
		bar = QLineEdit()
		
		box = QVBoxLayout()
		box.addWidget(bar)
		box.addStretch(1)
		groupBox.setLayout(box)
		
		return groupBox
		
	def createNameGroup(self):
		groupBox = QGroupBox("Name")
		
		name = QLineEdit()
		
		box = QVBoxLayout()
		box.addWidget(name)
		box.addStretch(1)
		groupBox.setLayout(box)
		
		return groupBox
		
		
	def createDateGroup(self):
		groupBox = QGroupBox("Date")
		
		#date stamp
		date = QLineEdit()
		now = QDate.currentDate()
		date.setText(now.toString(Qt.ISODate))
		
		box = QVBoxLayout()
		box.addWidget(date)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
		
	def createStartGroup(self):
		groupBox = QGroupBox("Starts")

		radio1 = QRadioButton("Yes")
		radio2 = QRadioButton("No")
		radio3 = QRadioButton("Not used")

		radio1.setChecked(True)

		vbox = QVBoxLayout()
		vbox.addWidget(radio1)
		vbox.addWidget(radio2)
		vbox.addWidget(radio3)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)

		return groupBox
		
	def createFilterGroup(self):
		groupBox = QGroupBox("Air Filter")

		radio1 = QRadioButton("Swapped")
		radio2 = QRadioButton("No Filter")

		radio1.setChecked(True)

		vbox = QVBoxLayout()
		vbox.addWidget(radio1)
		vbox.addWidget(radio2)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)

		return groupBox
		
	def createClutchGroup(self):
		groupBox = QGroupBox("Clutch Drum")

		check1 = QCheckBox("Cleaned")
		check2 = QCheckBox("Greased")
		
		#inner damage group
		radio1 = QRadioButton("Yes")
		radio2 = QRadioButton("No")
		radio2.setChecked(True)
		
		damGroup = QGroupBox("Damage")
		dam_vbox = QVBoxLayout()
		dam_vbox.addWidget(radio1)
		dam_vbox.addWidget(radio2)
		dam_vbox.addStretch(1)
		damGroup.setLayout(dam_vbox)
		
		#inner burn group
		radio3 = QRadioButton("Yes")
		radio4 = QRadioButton("No")
		radio4.setChecked(True)
		
		burnGroup = QGroupBox("Burns")
		burn_vbox = QVBoxLayout()
		burn_vbox.addWidget(radio3)
		burn_vbox.addWidget(radio4)
		burn_vbox.addStretch(1)
		burnGroup.setLayout(burn_vbox)

		#Clutch drum group
		vbox = QVBoxLayout()
		vbox.addWidget(check1)
		vbox.addWidget(check2)
		vbox.addWidget(damGroup)
		vbox.addWidget(burnGroup)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)

		return groupBox
		
	def createBaringGroup(self):
		groupBox = QGroupBox("Clutch Bearing")

		check1 = QCheckBox("Greased")
		
		#inner worn group
		radio1 = QRadioButton("Yes")
		radio2 = QRadioButton("No")
		radio2.setChecked(True)
		
		wornGroup = QGroupBox("Worn")
		worn_vbox = QVBoxLayout()
		worn_vbox.addWidget(radio1)
		worn_vbox.addWidget(radio2)
		worn_vbox.addStretch(1)
		wornGroup.setLayout(worn_vbox)
		
		#inner beveled group
		radio3 = QRadioButton("Yes")
		radio4 = QRadioButton("No")
		radio4.setChecked(True)
		
		bevelGroup = QGroupBox("Beveled")
		bevel_vbox = QVBoxLayout()
		bevel_vbox.addWidget(radio3)
		bevel_vbox.addWidget(radio4)
		bevel_vbox.addStretch(1)
		bevelGroup.setLayout(bevel_vbox)

		#Clutch baring group
		vbox = QVBoxLayout()
		vbox.addWidget(check1)
		vbox.addWidget(wornGroup)
		vbox.addWidget(bevelGroup)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)

		return groupBox
		
	def createSprocketGroup(self):
		groupBox = QGroupBox("Sprocket")
		
		#inner damage group
		radio1 = QRadioButton("Yes")
		radio2 = QRadioButton("No")
		radio2.setChecked(True)
		
		damGroup = QGroupBox("Worn")
		dam_vbox = QVBoxLayout()
		dam_vbox.addWidget(radio1)
		dam_vbox.addWidget(radio2)
		dam_vbox.addStretch(1)
		damGroup.setLayout(dam_vbox)

		#Sprocket group
		vbox = QVBoxLayout()
		vbox.addWidget(damGroup)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)

		return groupBox
		
	def createChainCatchGroup(self):
		groupBox = QGroupBox("Chain Catch")
		
		#inner intact group
		radio1 = QRadioButton("Yes")
		radio2 = QRadioButton("No")
		radio2.setChecked(True)
		
		intGroup = QGroupBox("Intact")
		int_vbox = QVBoxLayout()
		int_vbox.addWidget(radio1)
		int_vbox.addWidget(radio2)
		int_vbox.addStretch(1)
		intGroup.setLayout(int_vbox)

		#Sprocket group
		vbox = QVBoxLayout()
		vbox.addWidget(intGroup)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)

		return groupBox
		
	def createWormGroup(self):
		groupBox = QGroupBox("Worm Gear")
		
		#inner top wear group
		radio1 = QRadioButton("Yes")
		radio2 = QRadioButton("No")
		radio2.setChecked(True)
		
		topGroup = QGroupBox("Top Wear")
		top_vbox = QVBoxLayout()
		top_vbox.addWidget(radio1)
		top_vbox.addWidget(radio2)
		top_vbox.addStretch(1)
		topGroup.setLayout(top_vbox)
		
		#inner side wear group
		radio3 = QRadioButton("Yes")
		radio4 = QRadioButton("No")
		radio4.setChecked(True)
		
		sideGroup = QGroupBox("Side Wear")
		side_vbox = QVBoxLayout()
		side_vbox.addWidget(radio3)
		side_vbox.addWidget(radio4)
		side_vbox.addStretch(1)
		sideGroup.setLayout(side_vbox)

		#Worm gear group
		vbox = QVBoxLayout()
		vbox.addWidget(topGroup)
		vbox.addWidget(sideGroup)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)

		self.wormGroup = groupBox
		
		#return groupBox
		
	def createBarGroup(self):
		groupBox = QGroupBox("Bar")
		
		check1 = QCheckBox("Cleaned")
		check2 = QCheckBox("Deburred")
		
		vbox = QVBoxLayout()
		vbox.addWidget(check1)
		vbox.addWidget(check2)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)
		
		return groupBox
		
	def createSparkGroup(self):
		groupBox = QGroupBox("Sparkplug")
		
		radio1 = QRadioButton("Yes")
		radio2 = QRadioButton("No")
		radio3 = QRadioButton("Yes")
		radio4 = QRadioButton("No")
		radio5 = QRadioButton("Yes")
		radio6 = QRadioButton("No")
		
		radio2.setChecked(True)
		radio4.setChecked(True)
		radio6.setChecked(True)
		
		#inner discolor group
		dcgroup = QGroupBox("Discolored")
		dc_vbox = QVBoxLayout()
		dc_vbox.addWidget(radio1)
		dc_vbox.addWidget(radio2)
		dc_vbox.addStretch(1)
		dcgroup.setLayout(dc_vbox)
		
		
		#inner wet group
		wetgroup = QGroupBox("Wet")
		wet_vbox = QVBoxLayout()
		wet_vbox.addWidget(radio3)
		wet_vbox.addWidget(radio4)
		wet_vbox.addStretch(1)
		wetgroup.setLayout(wet_vbox)
		
		#inner carbon build-up group
		carbongroup = QGroupBox("Carbon Build-up")
		car_vbox = QVBoxLayout()
		car_vbox.addWidget(radio5)
		car_vbox.addWidget(radio6)
		car_vbox.addStretch(1)
		carbongroup.setLayout(car_vbox)
		
		#sparkplug group
		vbox = QVBoxLayout()
		vbox.addWidget(dcgroup)
		vbox.addWidget(wetgroup)
		vbox.addWidget(carbongroup)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)
		
		return groupBox
		
	def createCapsGroup(self):
		groupBox = QGroupBox("Caps")
		
		radio1 = QRadioButton("Yes")
		radio2 = QRadioButton("No")
		radio3 = QRadioButton("Yes")
		radio4 = QRadioButton("No")
		
		radio2.setChecked(True)
		radio4.setChecked(True)
		
		check1 = QCheckBox("O-ring Cleaned")
		check2 = QCheckBox("O-ring Cleaned")
		
		#inner oil group
		oil_group = QGroupBox("Oil")
		oil_vbox = QVBoxLayout()
		oil_vbox.addWidget(check1)
		#inner inner leak group
		oil_leak_group = QGroupBox("Leaks")
		leak_vbox = QVBoxLayout()
		leak_vbox.addWidget(radio1)
		leak_vbox.addWidget(radio2)
		leak_vbox.addStretch(1)
		oil_leak_group.setLayout(leak_vbox)
		#end inner inner....
		oil_vbox.addWidget(oil_leak_group)
		oil_vbox.addStretch(1)
		oil_group.setLayout(oil_vbox)
		
		#inner gas group
		gas_group = QGroupBox("Gas")
		gas_vbox = QVBoxLayout()
		gas_vbox.addWidget(check2)
		#inner inner leak group
		gas_leak_group = QGroupBox("Leaks")
		gleak_vbox = QVBoxLayout()
		gleak_vbox.addWidget(radio3)
		gleak_vbox.addWidget(radio4)
		gleak_vbox.addStretch(1)
		gas_leak_group.setLayout(gleak_vbox)
		#end inner inner....
		gas_vbox.addWidget(gas_leak_group)
		gas_vbox.addStretch(1)
		gas_group.setLayout(gas_vbox)
		
		#caps group
		vbox = QVBoxLayout()
		vbox.addWidget(oil_group)
		vbox.addWidget(gas_group)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)
		
		return groupBox
		
	def createSliderGroup(self):
		groupBox = QGroupBox("Sliders")
		sliderGroup = QGroupBox("In Place")
		
		check1 = QCheckBox("Slider 1")
		check2 = QCheckBox("Slider 2")
		
		slider_vbox = QVBoxLayout()
		slider_vbox.addWidget(check1)
		slider_vbox.addWidget(check2)
		slider_vbox.addStretch(1)
		sliderGroup.setLayout(slider_vbox)
		
		vbox = QVBoxLayout()
		vbox.addWidget(sliderGroup)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)
		
		return groupBox
		
	def createPullcordGroup(self):
		groupBox = QGroupBox("Pull Cord")
		fray_group = QGroupBox("Frayed")
		short_group = QGroupBox("Short Pull")
		ret_group = QGroupBox("Fully Retracts")
		
		radio1 = QRadioButton("Yes")
		radio2 = QRadioButton("No")
		radio3 = QRadioButton("Yes")
		radio4 = QRadioButton("No")
		radio5 = QRadioButton("Yes")
		radio6 = QRadioButton("No")
		
		radio2.setChecked(True)
		radio4.setChecked(True)
		radio6.setChecked(True)
		
		#inner fray group
		fray_vbox = QVBoxLayout()
		fray_vbox.addWidget(radio1)
		fray_vbox.addWidget(radio2)
		fray_vbox.addStretch(1)
		fray_group.setLayout(fray_vbox)
		
		#inner short pull group
		short_vbox = QVBoxLayout()
		short_vbox.addWidget(radio3)
		short_vbox.addWidget(radio4)
		short_vbox.addStretch(1)
		short_group.setLayout(short_vbox)
		
		#inner full retract group
		ret_vbox = QVBoxLayout()
		ret_vbox.addWidget(radio5)
		ret_vbox.addWidget(radio6)
		ret_vbox.addStretch(1)
		ret_group.setLayout(ret_vbox)
		
		#pull cord group
		vbox = QVBoxLayout()
		vbox.addWidget(fray_group)
		vbox.addWidget(short_group)
		vbox.addWidget(ret_group)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)
		
		return groupBox


#execute application
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
