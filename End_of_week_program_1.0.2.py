import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QPushButton, 
	QComboBox, QLabel, QGridLayout, QGroupBox, QRadioButton, QVBoxLayout,
	QCheckBox, QLineEdit, QAction, QProgressBar, QCalendarWidget, QFileDialog,
        QColorDialog, QMessageBox, QFontDialog, QTextEdit)
from PyQt5.QtCore import pyqtSlot, Qt, QDate, QTime, QDateTime
from PyQt5.QtGui import QIcon, QColor

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'End of Week Log'
		self.left = 10
		self.top = 30
		self.width = 640
		self.height = 480
		
		#worm gear selections
		self.radio_wg_top_y = QRadioButton("Yes")
		self.radio_wg_top_n = QRadioButton("No")
		self.radio_wg_top_y.setChecked(True)
		self.radio_wg_side_y = QRadioButton("Yes")
		self.radio_wg_side_n = QRadioButton("No")
		self.radio_wg_side_y.setChecked(True)
		
		#saw selection
		self.saw_list = ['S1', 'S2', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12',
			'S15', 'S17', 'S18', 'S19', 'S21', 'S25', 'S27', 'S28', 'S30', 'S250']
		self.saws = QComboBox()
		self.saws.addItems(self.saw_list)
		
		#bar entry
		self.bar = QLineEdit()
		
		#crew name entry
		self.crew_name = QLineEdit()
		
		#date stamp
		self.date = QLineEdit()
		self.now = QDate.currentDate()
		self.date.setText(self.now.toString(Qt.ISODate))
		
		#start selection
		self.rad_start_y = QRadioButton("Yes")
		self.rad_start_n = QRadioButton("No")
		self.rad_start_na = QRadioButton("Not used")
		self.rad_start_n.setChecked(True)
		
		#filter selection
		self.rad_filt_swap = QRadioButton("Swapped")
		self.rad_filt_non = QRadioButton("No Filter")
		self.rad_filt_non.setChecked(True)
		
		#Clutch selections
		#operations
		self.chk_cltch_cln = QCheckBox("Cleaned")
		self.chk_cltch_grsd = QCheckBox("Greased")
		#damage selection
		self.rad_dmg_y = QRadioButton("Yes")
		self.rad_dmg_n = QRadioButton("No")
		self.rad_dmg_y.setChecked(True)
		#burn selection
		self.rad_brn_y = QRadioButton("Yes")
		self.rad_brn_n = QRadioButton("No")
		self.rad_brn_y.setChecked(True)
		
		#Bearing slections
		#grease check
		self.chk_bear_grsd = QCheckBox("Greased")
		#worn selection
		self.rad_bear_worn_y = QRadioButton("Yes")
		self.rad_bear_worn_n = QRadioButton("No")
		self.rad_bear_worn_y.setChecked(True)
		#beveled selection
		self.rad_bear_bev_y = QRadioButton("Yes")
		self.rad_bear_bev_n = QRadioButton("No")
		self.rad_bear_bev_y.setChecked(True)
		
		#sprocket selections
		#damage selection
		self.rad_spkt_dmg_y = QRadioButton("Yes")
		self.rad_spkt_dmg_n = QRadioButton("No")
		self.rad_spkt_dmg_y.setChecked(True)
		
		#chain catch intact selection
		self.rad_chnctch_y = QRadioButton("Yes")
		self.rad_chnctch_n = QRadioButton("No")
		self.rad_chnctch_n.setChecked(True)
		
		#bar checkoff list
		self.chk_bar_cln = QCheckBox("Cleaned")
		self.chk_bar_dbr = QCheckBox("Deburred")
		
		#spark plug selections
		self.rad_sprkp_disc_y = QRadioButton("Yes")
		self.rad_sprkp_disc_n = QRadioButton("No")
		self.rad_sprkp_wet_y = QRadioButton("Yes")
		self.rad_sprkp_wet_n = QRadioButton("No")
		self.rad_sprkp_cb_y = QRadioButton("Yes")
		self.rad_sprkp_cb_n = QRadioButton("No")
		self.rad_sprkp_disc_y.setChecked(True)
		self.rad_sprkp_wet_y.setChecked(True)
		self.rad_sprkp_cb_y.setChecked(True)
		
		#cap selections
		self.rad_oil_leak_y = QRadioButton("Yes")
		self.rad_oil_leak_n = QRadioButton("No")
		self.rad_gas_leak_y = QRadioButton("Yes")
		self.rad_gas_leak_n = QRadioButton("No")
		self.rad_gas_leak_y.setChecked(True)
		self.rad_oil_leak_y.setChecked(True)
		self.chk_oil_cln = QCheckBox("O-ring Cleaned")
		self.chk_gas_cln = QCheckBox("O-ring Cleaned")
		
		#Sliders checks
		self.chk_sldr_1 = QCheckBox("Slider 1")
		self.chk_sldr_2 = QCheckBox("Slider 2")
		
		#pull cor selections
		self.rad_pc_fray_y = QRadioButton("Yes")
		self.rad_pc_fray_n = QRadioButton("No")
		self.rad_pc_short_y = QRadioButton("Yes")
		self.rad_pc_short_n = QRadioButton("No")
		self.rad_pc_rtact_y = QRadioButton("Yes")
		self.rad_pc_rtact_n = QRadioButton("No")
		self.rad_pc_fray_y.setChecked(True)
		self.rad_pc_short_y.setChecked(True)
		self.rad_pc_rtact_n.setChecked(True)
		
		#create UI
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
		grid.addWidget(self.createWormGroup(), 2, 2)
		grid.addWidget(self.createBarGroup(), 1, 5)
		grid.addWidget(self.createSparkGroup(), 2, 3)
		grid.addWidget(self.createCapsGroup(), 2, 4)
		grid.addWidget(self.createSliderGroup(), 1, 2)
		grid.addWidget(self.createPullcordGroup(), 2, 5)
		self.setLayout(grid)		
		
		saveFile = QAction("&Save File", self)
		saveFile.setShortcut("Ctrl+S")
		saveFile.setStatusTip('Save File')
		saveFile.triggered.connect(self.save_click)
		
		
		self.show()
	
	
        
	def createSAVE(self):
		save_button = QPushButton('&Save', self)
		save_button.setToolTip('Save all choices to a log')
		save_button.clicked.connect(self.save_click)
		
		return save_button
		
	@pyqtSlot()
	def save_click(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		auto_name = str(self.saws.currentText()) + "-" + str(self.date.text())
		name, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()",auto_name,"All Files (*);;Text Files (*.txt)", options=options)
		
		try:
			file = open(name, 'w+')
			text = self.output_text()
			file.write(text)
			file.close()
		except:
			pass
		
	def createWormGroup(self):
		groupBox = QGroupBox("Worm Gear")
		
		#inner top wear group		
		topGroup = QGroupBox("Top Wear")
		top_vbox = QVBoxLayout()
		top_vbox.addWidget(self.radio_wg_top_y)
		top_vbox.addWidget(self.radio_wg_top_n)
		top_vbox.addStretch(1)
		topGroup.setLayout(top_vbox)
		
		#inner side wear group
		sideGroup = QGroupBox("Side Wear")
		side_vbox = QVBoxLayout()
		side_vbox.addWidget(self.radio_wg_side_y)
		side_vbox.addWidget(self.radio_wg_side_n)
		side_vbox.addStretch(1)
		sideGroup.setLayout(side_vbox)

		#Worm gear group
		vbox = QVBoxLayout()
		vbox.addWidget(topGroup)
		vbox.addWidget(sideGroup)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)
		
		return groupBox
		
	def output_text(self):
		
		master_output = ""
					
		#saw selection
		saw = str(self.saws.currentText())
		saw += "\n"
		master_output += saw
				
		#bar entry
		bar = self.bar.text()
		bar += "\n"
		master_output += bar
		
		#crew name entry
		crew = self.crew_name.text()
		crew += "\n"
		master_output += crew
		
		#date stamp
		today = str(self.date.text())
		today += "\n"
		master_output += today
		
		#start selection
		starts = "Starts: "
		if self.rad_start_y.isChecked():
			starts += "Yes\n"
		if self.rad_start_n.isChecked():
			starts += "No\n"
		if self.rad_start_na.isChecked():
			starts += "Unknown\n"
		master_output += starts
		
		#filter selection
		air_filter = "Air Filter: "
		if self.rad_filt_swap.isChecked():
			air_filter += "Swapped\n"
		if self.rad_filt_non.isChecked():
			air_filter += "Non Installed\n"
		master_output += air_filter
		
		#worm gear selections output
		worm_gear = "Worm Gear:\n"
		if self.radio_wg_top_y.isChecked():
			worm_gear += "-top wear\n"
		if self.radio_wg_side_y.isChecked():
			worm_gear += "-side wear\n"
		master_output += worm_gear
	
		#Clutch output
		#operations
		clutch_out = "Clutch:\n"
		if self.chk_cltch_cln.isChecked() == False:
			clutch_out += "-Not cleaned\n"
		if self.chk_cltch_grsd.isChecked() == False:
			clutch_out += "-Not greased\n"
		#damage selection
		if self.rad_dmg_y.isChecked():
			clutch_out += "-Damaged\n"
		#burn selection
		if self.rad_brn_y.isChecked():
			clutch_out += "-Burned\n"
		master_output += clutch_out	
		
		#Bearing slections
		#grease check
		bearing_out = "Clutch Bearing:\n"
		if self.chk_bear_grsd.isChecked() == False:
			bearing_out += "-Not greased\n"
		#worn selection
		if self.rad_bear_worn_y.isChecked():
			bearing_out += "-Vertical Wear\n"
		#beveled selection
		if self.rad_bear_bev_y.isChecked():
			bearing_out += "-Beveled Wear\n"
		master_output += bearing_out
		
		#sprocket selections
		#damage selection
		sprocket_out = "Sprocket:\n"
		if self.rad_spkt_dmg_y.isChecked():
			sprocket_out += "-Worn\n"
		master_output += sprocket_out
				
		#chain catch intact selection
		chain_catch_out = "Chain Catch:\n"
		if self.rad_chnctch_n.isChecked():
			chain_catch_out += "-Worn\n"
		master_output += chain_catch_out
		
		#bar checkoff list
		bar_out = "Bar:\n"
		if self.chk_bar_cln.isChecked() == False:
			bar_out += "-Not cleaned\n"
		if self.chk_bar_dbr.isChecked() == False:
			bar_out += "-Not De-Burred\n"
		master_output += bar_out
		
		#spark plug selections
		spark_plug_out = "Spark Plug:\n"
		if self.rad_sprkp_disc_y.isChecked():
			spark_plug_out += "-Discolored\n"
		if self.rad_sprkp_wet_y.isChecked():
			spark_plug_out += "-Wet\n"
		if self.rad_sprkp_cb_y.isChecked():
			spark_plug_out += "-Carbon Buildup\n"
		master_output += spark_plug_out
		
		
		#cap selections
		caps_out = "Caps:\n"
		if self.rad_oil_leak_y.isChecked():
			caps_out += "-Oil cap Leaks\n"
		if self.rad_gas_leak_y.isChecked():
			caps_out += "-Gas cap Leaks\n"
		if self.chk_oil_cln.isChecked() == False:
			caps_out += "-Oil cap not cleaned\n"
		if self.chk_gas_cln.isChecked() == False:
			caps_out += "-Gas cap not cleaned\n"
		master_output += caps_out
		
		#Sliders checks
		sliders_out = "Sliders:\n"
		slider_num = 0
		if self.chk_sldr_1.isChecked() == False:
			slider_num += 1
		if self.chk_sldr_2.isChecked() == False:
			slider_num += 1
		sliders_out += "-" + str(slider_num) + " sliders missing\n"
		master_output += sliders_out
		
		#pull cor selections
		pull_cord_out = "Pull Cord:\n"
		if self.rad_pc_fray_y.isChecked():
			pull_cord_out += "-Frayed\n"
		if self.rad_pc_short_y.isChecked():
			pull_cord_out += "-Short Pull\n"
		if self.rad_pc_rtact_n.isChecked():
			pull_cord_out += "-Doesn't fully retract\n"
		master_output += pull_cord_out
			
		
		return master_output
		
	def createSawGroup(self):
		groupBox = QGroupBox("Saw")
		box = QVBoxLayout()
		
		box.addWidget(self.saws)
		box.addStretch(1)

		groupBox.setLayout(box)
		
		return groupBox
		
	def createBarNumGroup(self):
		groupBox = QGroupBox("Bar #")
		
		box = QVBoxLayout()
		box.addWidget(self.bar)
		box.addStretch(1)
		groupBox.setLayout(box)
		
		return groupBox
		
	def createNameGroup(self):
		groupBox = QGroupBox("Name")
		
		box = QVBoxLayout()
		box.addWidget(self.crew_name)
		box.addStretch(1)
		groupBox.setLayout(box)
		
		return groupBox
		
	def createDateGroup(self):
		groupBox = QGroupBox("Date")
		
		box = QVBoxLayout()
		box.addWidget(self.date)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createStartGroup(self):
		groupBox = QGroupBox("Starts")

		vbox = QVBoxLayout()
		vbox.addWidget(self.rad_start_y)
		vbox.addWidget(self.rad_start_n)
		vbox.addWidget(self.rad_start_na)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)

		return groupBox
		
	def createFilterGroup(self):
		groupBox = QGroupBox("Air Filter")

		vbox = QVBoxLayout()
		vbox.addWidget(self.rad_filt_swap)
		vbox.addWidget(self.rad_filt_non)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)

		return groupBox
		
	def createClutchGroup(self):
		groupBox = QGroupBox("Clutch Drum")
		
		damGroup = QGroupBox("Damage")
		dam_vbox = QVBoxLayout()
		dam_vbox.addWidget(self.rad_dmg_y)
		dam_vbox.addWidget(self.rad_dmg_n)
		dam_vbox.addStretch(1)
		damGroup.setLayout(dam_vbox)
		
		burnGroup = QGroupBox("Burns")
		burn_vbox = QVBoxLayout()
		burn_vbox.addWidget(self.rad_brn_y)
		burn_vbox.addWidget(self.rad_brn_n)
		burn_vbox.addStretch(1)
		burnGroup.setLayout(burn_vbox)

		#Clutch drum group
		vbox = QVBoxLayout()
		vbox.addWidget(self.chk_cltch_cln)
		vbox.addWidget(self.chk_cltch_grsd)
		vbox.addWidget(damGroup)
		vbox.addWidget(burnGroup)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)

		return groupBox
		
	def createBaringGroup(self):
		groupBox = QGroupBox("Clutch Bearing")

		wornGroup = QGroupBox("Worn")
		worn_vbox = QVBoxLayout()
		worn_vbox.addWidget(self.rad_bear_worn_y)
		worn_vbox.addWidget(self.rad_bear_worn_n)
		worn_vbox.addStretch(1)
		wornGroup.setLayout(worn_vbox)
		
		bevelGroup = QGroupBox("Beveled")
		bevel_vbox = QVBoxLayout()
		bevel_vbox.addWidget(self.rad_bear_bev_y)
		bevel_vbox.addWidget(self.rad_bear_bev_n)
		bevel_vbox.addStretch(1)
		bevelGroup.setLayout(bevel_vbox)

		#Clutch baring group
		vbox = QVBoxLayout()
		vbox.addWidget(self.chk_bear_grsd)
		vbox.addWidget(wornGroup)
		vbox.addWidget(bevelGroup)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)

		return groupBox
		
	def createSprocketGroup(self):
		groupBox = QGroupBox("Sprocket")
		
		damGroup = QGroupBox("Worn")
		dam_vbox = QVBoxLayout()
		dam_vbox.addWidget(self.rad_spkt_dmg_y)
		dam_vbox.addWidget(self.rad_spkt_dmg_n)
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
		
		intGroup = QGroupBox("Intact")
		int_vbox = QVBoxLayout()
		int_vbox.addWidget(self.rad_chnctch_n)
		int_vbox.addWidget(self.rad_chnctch_y)
		int_vbox.addStretch(1)
		intGroup.setLayout(int_vbox)

		#Chain-catch group
		vbox = QVBoxLayout()
		vbox.addWidget(intGroup)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)

		return groupBox
		
	def createBarGroup(self):
		groupBox = QGroupBox("Bar")
		
		vbox = QVBoxLayout()
		vbox.addWidget(self.chk_bar_cln)
		vbox.addWidget(self.chk_bar_dbr)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)
		
		return groupBox
		
	def createSparkGroup(self):
		groupBox = QGroupBox("Sparkplug")
			
		#inner discolor group
		dcgroup = QGroupBox("Discolored")
		dc_vbox = QVBoxLayout()
		dc_vbox.addWidget(self.rad_sprkp_disc_y)
		dc_vbox.addWidget(self.rad_sprkp_disc_n)
		dc_vbox.addStretch(1)
		dcgroup.setLayout(dc_vbox)
		
		
		#inner wet group
		wetgroup = QGroupBox("Wet")
		wet_vbox = QVBoxLayout()
		wet_vbox.addWidget(self.rad_sprkp_wet_y)
		wet_vbox.addWidget(self.rad_sprkp_wet_n)
		wet_vbox.addStretch(1)
		wetgroup.setLayout(wet_vbox)
		
		#inner carbon build-up group
		carbongroup = QGroupBox("Carbon Build-up")
		car_vbox = QVBoxLayout()
		car_vbox.addWidget(self.rad_sprkp_cb_y)
		car_vbox.addWidget(self.rad_sprkp_cb_n)
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
		
		#inner oil group
		oil_group = QGroupBox("Oil")
		oil_vbox = QVBoxLayout()
		oil_vbox.addWidget(self.chk_oil_cln)
		#inner inner leak group
		oil_leak_group = QGroupBox("Leaks")
		leak_vbox = QVBoxLayout()
		leak_vbox.addWidget(self.rad_oil_leak_y)
		leak_vbox.addWidget(self.rad_oil_leak_n)
		leak_vbox.addStretch(1)
		oil_leak_group.setLayout(leak_vbox)
		#end inner inner....
		oil_vbox.addWidget(oil_leak_group)
		oil_vbox.addStretch(1)
		oil_group.setLayout(oil_vbox)
		
		#inner gas group
		gas_group = QGroupBox("Gas")
		gas_vbox = QVBoxLayout()
		gas_vbox.addWidget(self.chk_gas_cln)
		#inner inner leak group
		gas_leak_group = QGroupBox("Leaks")
		gleak_vbox = QVBoxLayout()
		gleak_vbox.addWidget(self.rad_gas_leak_y)
		gleak_vbox.addWidget(self.rad_gas_leak_n)
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
		
		slider_vbox = QVBoxLayout()
		slider_vbox.addWidget(self.chk_sldr_1)
		slider_vbox.addWidget(self.chk_sldr_2)
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
		
		#inner fray group
		fray_vbox = QVBoxLayout()
		fray_vbox.addWidget(self.rad_pc_fray_y)
		fray_vbox.addWidget(self.rad_pc_fray_n)
		fray_vbox.addStretch(1)
		fray_group.setLayout(fray_vbox)
		
		#inner short pull group
		short_vbox = QVBoxLayout()
		short_vbox.addWidget(self.rad_pc_short_y)
		short_vbox.addWidget(self.rad_pc_short_n)
		short_vbox.addStretch(1)
		short_group.setLayout(short_vbox)
		
		#inner full retract group
		ret_vbox = QVBoxLayout()
		ret_vbox.addWidget(self.rad_pc_rtact_n)
		ret_vbox.addWidget(self.rad_pc_rtact_y)
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
