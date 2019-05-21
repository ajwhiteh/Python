import sys
import csv
import itertools
from datetime import datetime
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, 
	QWidget, QAction, QTabWidget, QVBoxLayout, QScrollArea, QGridLayout,
	 QComboBox, QGroupBox, QLineEdit, qApp, QMessageBox, QLabel, QHBoxLayout,
	 QTextEdit)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from csv_mod import CSV_Handle

class ScrollMessageBox(QMessageBox):
	def __init__(self, l, *args, **kwargs):
		QMessageBox.__init__(self, *args, **kwargs)
		scroll = QScrollArea(self)
		scroll.setWidgetResizable(True)
		self.content = QWidget()
		scroll.setWidget(self.content)
		lay = QVBoxLayout(self.content)
		lay.addWidget(QLabel(l, self))
		self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())
		self.setStyleSheet("QScrollArea{min-width:400 px; min-height: 300 px}")
 
class App(QMainWindow):
 
	def __init__(self):
		super().__init__()
		
		#self.setStyleSheet(open("darkstyle.qss", "r").read())
		
		self.title = 'Shop Tech'
		self.left = 10
		self.top = 30
		self.width = 940
		self.height = 650
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		exitAct = QAction(QIcon('exit.png'), '&Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.setStatusTip('Exit Application')
		exitAct.triggered.connect(qApp.quit)
		
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAct)
		
		updateAct = QAction('&Update Reports', self)
		updateAct.triggered.connect(self.csv_update)
		
		todoAct = QAction('&To Do List', self)
		todoAct.triggered.connect(self.todo)
		
		toolsMenu = menubar.addMenu('&Tools')
		toolsMenu.addAction(updateAct)
		toolsMenu.addAction(todoAct)
		
		self.table_widget = MyTableWidget(self)
		self.setCentralWidget(self.table_widget)
		
		self.csv_data = CSV_Handle()
 
		self.show()
		
	@pyqtSlot()
	def csv_update(self):
		'''transfers data from report folder to csv'''
		self.csv_data.fill_file_list()
		if not self.csv_data.get_files_list():
			QMessageBox.about(self, "Update", "No Files to Update   \n")
		else:
			self.csv_data.csv_transfer()
			QMessageBox.about(self, "Update", "Files Updated   \n")
		
	@pyqtSlot()
	def todo(self):
		'''Opens window with all saws needing attention'''
		# Get saw list from maint_logs.csv with newest errors
		#test_saw = ['S1']
		saws = ['S1', 'S2', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12',
			'S15', 'S17', 'S18', 'S19', 'S21', 'S25', 'S27', 'S28', 'S30', 'S250']
		problem = ['', 'No start', 'Needs air filter', 'worm gear top wear',
			'worm gear side wear', 'clutch drum not clean', 'clutch drum not greased',
			'clutch drum damage', 'clutch drum burn', 'bearing not greased',
			'bearing worn', 'bearing beveled', 'sprocket damaged', 'chain catch broken',
			'bar not cleaned', 'bar not deburred', 'sparkplug discolored',
			'sparkplug wet', 'sparkplug carbon buildup', 'oil cap leaks',
			'gas cap leaks', 'oil cap not clean', 'gas cap not clean', 
			'slider 1 missing', 'slider 2 missing', 'pull cord frayed',
			'pull cord short',	'pull cord wont retact']

		saw_message = str()
		saw_master = ['']
		saw_master += itertools.repeat('True', 2)
		saw_master += itertools.repeat('False', 2)
		saw_master += itertools.repeat('True', 5)
		saw_master.append('False')
		saw_master.append('True')
		saw_master.append('False')
		saw_master += itertools.repeat('True', 15)
		saw_master.append('')
		for saw in saws:
			saw_data = self.csv_data.csv_search_latest(saw)
			saw_master[0] = saw
			del saw_data[1:4]
			if saw_data != saw_master:
				saw_message += saw + ':'
				for i in range(len(saw_data) - 1):
					if saw_data[i] != saw_master[i]:
						saw_message += ' ' + problem[i] + ','
				if saw_data[-1] != saw_master[-1]:
					saw_message += ' ' + saw_data[-1] + ','
				saw_message = saw_message[:-1]
				saw_message += '\n'
				
		
		#print(saw_master, saw_data, saw_message)
		output = ScrollMessageBox(saw_message, None)
		output.exec_()


class MyTableWidget(QWidget):
 
	def __init__(self, parent):
		super(QWidget, self).__init__(parent)
		
		self.layout = QVBoxLayout(self)
		
		self.csv_data = CSV_Handle()
 
		####Saw Options and Variables
		#saw selection
		self.saw_list = ['S1', 'S2', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12',
			'S15', 'S17', 'S18', 'S19', 'S21', 'S25', 'S27', 'S28', 'S30', 'S250']
		self.saws1 = QComboBox()
		self.saws1.addItems(self.saw_list)
		self.saws2 = QComboBox()
		self.saws2.addItems(self.saw_list)
		#Crew member name
		self.in_crew_name = QLineEdit()
		#Starts
		self.in_starts = QLineEdit()
		self.in_starts.setReadOnly(1)
		#Last date serviced
		self.in_date = QLineEdit()
		#Bar num attatched
		self.in_bar_num = QLineEdit()
		#Air filter
		self.in_air_filter = QLineEdit()
		#Worm gear
		self.in_worm_gear_top = QLineEdit()
		self.in_worm_gear_side = QLineEdit()
		#Clutch Drum
		self.in_clutch_drum_cln = QLineEdit()
		self.in_clutch_drum_grsd = QLineEdit()
		self.in_clutch_drum_dmg = QLineEdit()
		self.in_clutch_drum_brn = QLineEdit()
		#Clutch bearing
		self.in_clutch_bearing_grsd = QLineEdit()
		self.in_clutch_bearing_worn = QLineEdit()
		self.in_clutch_bearing_bev = QLineEdit()
		#Sprocket
		self.in_sprocket = QLineEdit()
		#Chain Catch
		self.in_chain_catch = QLineEdit()
		#Bar
		self.in_bar_cln = QLineEdit()
		self.in_bar_dbr = QLineEdit()
		#Spark Plug
		self.in_spark_plug_disc = QLineEdit()
		self.in_spark_plug_wet = QLineEdit()
		self.in_spark_plug_cb = QLineEdit()
		#Caps
		self.in_caps_oil_leak = QLineEdit()
		self.in_caps_gas_leak = QLineEdit()
		self.in_caps_oil_cln = QLineEdit()
		self.in_caps_gas_cln = QLineEdit()
		#Sliders
		self.in_slider1 = QLineEdit()
		self.in_slider2 = QLineEdit()
		#Pull Cord
		self.in_pull_cord_fray = QLineEdit()
		self.in_pull_cord_short = QLineEdit()
		self.in_pull_cord_retract = QLineEdit()
		#Misc
		self.in_misc = QLineEdit()
		
		# New operations vars
		self.now = datetime.now()
		self.current_date = self.now.strftime("%Y-%m-%d")
		
		self.date_box = QLineEdit()
		self.date_box.setText(self.current_date)
		self.date_box.setMaximumWidth(80)
		
		self.label1 = QLabel()
		self.label1.setText("Issue")
		
		self.issue_box = QLineEdit()
		
		self.label2 = QLabel()
		self.label2.setText("Solution")
		
		self.solution_box = QLineEdit()
		
		# New operations buttons
		self.new_op_date = QPushButton('Reset Date', self)
		self.new_op_date.setMaximumWidth(150)
		self.new_op_date.clicked.connect(self.date_reset)
		
		self.new_op_save = QPushButton('Save', self)
		self.new_op_save.setMaximumWidth(150)
		self.new_op_save.clicked.connect(self.save_click)
		
		self.new_op_cancel = QPushButton('Clear', self)
		self.new_op_cancel.setMaximumWidth(150)
		self.new_op_cancel.clicked.connect(self.cancel_click)
		
		# Previous operations vars
		self.previous_ops = QTextEdit()
		self.previous_ops.setFixedHeight(300)
 
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
		'''Create first tab that displays latest maint. logs per saw'''
		# Tab properties init
		tab = QScrollArea()
		tab.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		tab_widget = QWidget()
		
		# Create first tab
		# Create tabs grid
		tabGrid = QGridLayout()
		tabGrid.addWidget(self.createBarCleaned(), 0, 2)
		tabGrid.addWidget(self.createBarDeburred(), 0, 3)
		tabGrid.addWidget(self.createBarNum(), 0, 4)
		tabGrid.addWidget(self.createCapsGasCleaned(), 1, 0)
		tabGrid.addWidget(self.createCapsGasLeak(), 1, 1)
		tabGrid.addWidget(self.createCapsOilCleaned(), 1, 2)
		tabGrid.addWidget(self.createCapsOilLeak(), 1, 3)
		tabGrid.addWidget(self.createChainCatch(), 1, 4)
		tabGrid.addWidget(self.createClutchBearingBev(), 2, 0)
		tabGrid.addWidget(self.createClutchBearingGreased(), 2, 1)
		tabGrid.addWidget(self.createClutchBearingWorn(), 2, 2)
		tabGrid.addWidget(self.createClutchDrumBurn(), 2, 3)
		tabGrid.addWidget(self.createClutchDrumClean(), 2, 4)
		tabGrid.addWidget(self.createClutchDrumDamage(), 3, 0)
		tabGrid.addWidget(self.createClutchDrumGreased(), 3, 1)
		tabGrid.addWidget(self.createCrewName(), 6, 1)
		tabGrid.addWidget(self.createDate(), 3, 2)
		tabGrid.addWidget(self.createFilter(), 3, 3)
		tabGrid.addWidget(self.createMisc(), 3, 4)
		tabGrid.addWidget(self.createPullCordFray(), 4, 0)
		tabGrid.addWidget(self.createPullCordRetracts(), 4, 1)
		tabGrid.addWidget(self.createPullCordShort(), 4, 2)
		tabGrid.addWidget(self.createSawSelectMaint(), 0, 0)
		tabGrid.addWidget(self.createSawStarts(), 0, 1)
		tabGrid.addWidget(self.createSlider1(), 4, 3)
		tabGrid.addWidget(self.createSlider2(), 4, 4)
		tabGrid.addWidget(self.createSparkPlugCarbonBuildup(), 5, 0)
		tabGrid.addWidget(self.createSparkPlugDiscolored(), 5, 1)
		tabGrid.addWidget(self.createSparkPlugWet(), 5, 2)
		tabGrid.addWidget(self.createSprocket(), 5, 3)
		tabGrid.addWidget(self.createWormGearSide(), 5, 4)
		tabGrid.addWidget(self.createWormGearTop(), 6, 0)
		
		# Set into tab
		tab_widget.setLayout(tabGrid)
		tab.setWidget(tab_widget)
		
		return tab
		
	# Saw operations	
	def createTab2(self):
		'''Create second tab that displays previous operations and inputs new operations'''
		tab = QWidget()
		
		# Create tabs grid
		tabGrid = QGridLayout()
		tabGrid.addWidget(self.createSawSelectOperations(), 0, 0)
		tabGrid.addWidget(self.createNewOp(), 1, 0, 1, 8)
		tabGrid.addWidget(self.createPrevOp(), 2, 0, 1, 6)
		
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
	def createSawSelectMaint(self):
		groupBox = QGroupBox("Saw")
		box = QVBoxLayout()
		
		self.saw_select_maint_logs()
		self.saws1.activated.connect(self.saw_select_maint_logs)
		
		box.addWidget(self.saws1)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createSawSelectOperations(self):
		groupBox = QGroupBox("Saw")
		box = QVBoxLayout()
		
		self.saw_select_op_logs()
		self.saws2.activated.connect(self.saw_select_op_logs)
		
		box.addWidget(self.saws2)
		
		groupBox.setLayout(box)
		groupBox.setMaximumHeight(60)
		
		return groupBox
		
		
	@pyqtSlot()
	def saw_select_maint_logs(self):
		'''Take selected saw and display latest info from maint_logs csv'''
		saw_num = str(self.saws1.currentText())
		#lambda functions for bool to str
		t_to_y = lambda x : 'Yes' if x == 'True' else 'No'
		f_to_n = lambda x : 'No' if x == 'False' else 'Yes'
		f_to_y = lambda x : 'Yes' if x == 'False' else 'No'

		#autofill
		saw_data = self.csv_data.csv_search_latest(saw_num)
		self.in_starts.setText(t_to_y(saw_data[4]))
		self.in_date.setText(saw_data[1][:-9])
		self.in_bar_num.setText(saw_data[2])
		self.in_crew_name.setText(saw_data[3])
		self.in_air_filter.setText(t_to_y(saw_data[5]))
		self.in_worm_gear_top.setText(t_to_y(saw_data[6]))
		self.in_worm_gear_side.setText(t_to_y(saw_data[7]))
		self.in_clutch_drum_cln.setText(f_to_n(saw_data[8]))
		self.in_clutch_drum_grsd.setText(f_to_n(saw_data[9]))
		self.in_clutch_drum_dmg.setText(f_to_y(saw_data[10]))
		self.in_clutch_drum_brn.setText(f_to_y(saw_data[11]))
		self.in_clutch_bearing_grsd.setText(f_to_n(saw_data[12]))
		self.in_clutch_bearing_worn.setText(t_to_y(saw_data[13]))
		self.in_clutch_bearing_bev.setText(f_to_y(saw_data[14]))
		self.in_sprocket.setText(t_to_y(saw_data[15]))
		self.in_chain_catch.setText(f_to_n(saw_data[16]))
		self.in_bar_cln.setText(f_to_n(saw_data[17]))
		self.in_bar_dbr.setText(f_to_n(saw_data[18]))
		self.in_spark_plug_disc.setText(f_to_y(saw_data[19]))
		self.in_spark_plug_wet.setText(f_to_y(saw_data[20]))
		self.in_spark_plug_cb.setText(f_to_y(saw_data[21]))
		self.in_caps_oil_leak.setText(f_to_y(saw_data[22]))
		self.in_caps_gas_leak.setText(f_to_y(saw_data[23]))
		self.in_caps_oil_cln.setText(f_to_n(saw_data[24]))
		self.in_caps_gas_cln.setText(f_to_n(saw_data[25]))
		self.in_slider1.setText(f_to_n(saw_data[26]))
		self.in_slider2.setText(f_to_n(saw_data[27]))
		self.in_pull_cord_fray.setText(f_to_y(saw_data[28]))
		self.in_pull_cord_short.setText(f_to_y(saw_data[29]))
		self.in_pull_cord_retract.setText(f_to_n(saw_data[30]))
		self.in_misc.setText(saw_data[31])
		
		# Lambda functions for setting text color
		t_is_red = lambda x : "color : red;" if x == 'True' else "color : black;"
		t_is_black = lambda x : "color : black;" if x == 'True' else "color : red;"
		
		# Color text
		self.in_starts.setStyleSheet(t_is_black(saw_data[4]))
		self.in_air_filter.setStyleSheet(t_is_black(saw_data[5]))
		self.in_worm_gear_top.setStyleSheet(t_is_red(saw_data[6]))
		self.in_worm_gear_side.setStyleSheet(t_is_red(saw_data[7]))
		self.in_clutch_drum_cln.setStyleSheet(t_is_black(saw_data[8]))
		self.in_clutch_drum_grsd.setStyleSheet(t_is_black(saw_data[9]))
		self.in_clutch_drum_dmg.setStyleSheet(t_is_black(saw_data[10]))
		self.in_clutch_drum_brn.setStyleSheet(t_is_black(saw_data[11]))
		self.in_clutch_bearing_grsd.setStyleSheet(t_is_black(saw_data[12]))
		self.in_clutch_bearing_worn.setStyleSheet(t_is_red(saw_data[13]))
		self.in_clutch_bearing_bev.setStyleSheet(t_is_black(saw_data[14]))
		self.in_sprocket.setStyleSheet(t_is_red(saw_data[15]))
		self.in_chain_catch.setStyleSheet(t_is_black(saw_data[16]))
		self.in_bar_cln.setStyleSheet(t_is_black(saw_data[17]))
		self.in_bar_dbr.setStyleSheet(t_is_black(saw_data[18]))
		self.in_spark_plug_disc.setStyleSheet(t_is_black(saw_data[19]))
		self.in_spark_plug_wet.setStyleSheet(t_is_black(saw_data[20]))
		self.in_spark_plug_cb.setStyleSheet(t_is_black(saw_data[21]))
		self.in_caps_oil_leak.setStyleSheet(t_is_black(saw_data[22]))
		self.in_caps_gas_leak.setStyleSheet(t_is_black(saw_data[23]))
		self.in_caps_oil_cln.setStyleSheet(t_is_black(saw_data[24]))
		self.in_caps_gas_cln.setStyleSheet(t_is_black(saw_data[25]))
		self.in_slider1.setStyleSheet(t_is_black(saw_data[26]))
		self.in_slider2.setStyleSheet(t_is_black(saw_data[27]))
		self.in_pull_cord_fray.setStyleSheet(t_is_black(saw_data[28]))
		self.in_pull_cord_short.setStyleSheet(t_is_black(saw_data[29]))
		self.in_pull_cord_retract.setStyleSheet(t_is_black(saw_data[30]))
		
	@pyqtSlot()
	def saw_select_op_logs(self):
		'''Take Selected saw and display operations over time'''
		saw_select = str(self.saws2.currentText())
		self.previous_ops.setText(self.csv_data.operations_get(saw_select))
		
	@pyqtSlot()
	def save_click(self):
		'''Saves new operations to operations csv'''
		confirm = QMessageBox.question(self, ' ', "Save Operation?", QMessageBox.Yes | QMessageBox.No)
		if confirm == QMessageBox.Yes:
			# Save as csv: 'saw num', 'date', 'issue', 'operation'
			output = (self.saws2.currentText(), self.date_box.text(), self.issue_box.text(),
				self.solution_box.text())
			self.csv_data.operation_input(output)
			saw_select = str(self.saws2.currentText())
			self.previous_ops.setText(self.csv_data.operations_get(saw_select))
		if confirm == QMessageBox.No:
			pass
		
	@pyqtSlot()
	def cancel_click(self):
		'''Clears all data entered in operations inputs'''
		self.issue_box.setText('')
		self.solution_box.setText('')
		
	@pyqtSlot()
	def date_reset(self):
		'''Returns date to current date'''
		self.date_box.setText(self.current_date)
		
		
		
	# tab 1 widgets	
	
	def createSawStarts(self):
		groupBox = QGroupBox("Starts")
		box = QVBoxLayout()
		
		box.addWidget(self.in_starts)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createCrewName(self):
		groupBox = QGroupBox("Crew Member")
		box = QVBoxLayout()
		
		box.addWidget(self.in_crew_name)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createDate(self):
		groupBox = QGroupBox("Last Date Maintained")
		box = QVBoxLayout()
		
		box.addWidget(self.in_date)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createBarNum(self):
		groupBox = QGroupBox("Bar Num")
		box = QVBoxLayout()
		
		box.addWidget(self.in_bar_num)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createFilter(self):
		groupBox = QGroupBox("Filter Status")
		box = QVBoxLayout()
		
		box.addWidget(self.in_air_filter)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createWormGearTop(self):
		groupBox = QGroupBox("Worm Gear Top Wear")
		box = QVBoxLayout()
		
		box.addWidget(self.in_worm_gear_top)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createWormGearSide(self):
		groupBox = QGroupBox("Worm Gear Side Wear")
		box = QVBoxLayout()
		
		box.addWidget(self.in_worm_gear_side)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createClutchDrumClean(self):
		groupBox = QGroupBox("Clutch Drum Cleaned")
		box = QVBoxLayout()
		
		box.addWidget(self.in_clutch_drum_cln)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
	
	def createClutchDrumGreased(self):
		groupBox = QGroupBox("Clutch Drum Greased")
		box = QVBoxLayout()
		
		box.addWidget(self.in_clutch_drum_grsd)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createClutchDrumDamage(self):
		groupBox = QGroupBox("Clutch Drum Damage")
		box = QVBoxLayout()
		
		box.addWidget(self.in_clutch_drum_dmg)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createClutchDrumBurn(self):
		groupBox = QGroupBox("Clutch Drum Burn")
		box = QVBoxLayout()
		
		box.addWidget(self.in_clutch_drum_brn)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createClutchBearingGreased(self):
		groupBox = QGroupBox("Clutch Bearing Greased")
		box = QVBoxLayout()
		
		box.addWidget(self.in_clutch_bearing_grsd)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createClutchBearingWorn(self):
		groupBox = QGroupBox("Clutch Bearing Worn")
		box = QVBoxLayout()
		
		box.addWidget(self.in_clutch_bearing_worn)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createClutchBearingBev(self):
		groupBox = QGroupBox("Clutch Bearing Beveled")
		box = QVBoxLayout()
		
		box.addWidget(self.in_clutch_bearing_bev)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createSprocket(self):
		groupBox = QGroupBox("Sprocket Worn")
		box = QVBoxLayout()
		
		box.addWidget(self.in_sprocket)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createChainCatch(self):
		groupBox = QGroupBox("Chain Catch Intact")
		box = QVBoxLayout()
		
		box.addWidget(self.in_chain_catch)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createBarCleaned(self):
		groupBox = QGroupBox("Bar Cleaned")
		box = QVBoxLayout()
		
		box.addWidget(self.in_bar_cln)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createBarDeburred(self):
		groupBox = QGroupBox("Bar Deburred")
		box = QVBoxLayout()
		
		box.addWidget(self.in_bar_dbr)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createSparkPlugDiscolored(self):
		groupBox = QGroupBox("Spark Plug Discolored")
		box = QVBoxLayout()
		
		box.addWidget(self.in_spark_plug_disc)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createSparkPlugWet(self):
		groupBox = QGroupBox("Spark Plug Wet")
		box = QVBoxLayout()
		
		box.addWidget(self.in_spark_plug_wet)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createSparkPlugCarbonBuildup(self):
		groupBox = QGroupBox("Spark Plug Carbon Buildup")
		box = QVBoxLayout()
		
		box.addWidget(self.in_spark_plug_cb)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createCapsOilLeak(self):
		groupBox = QGroupBox("Oil Cap Leaks")
		box = QVBoxLayout()
		
		box.addWidget(self.in_caps_oil_leak)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createCapsGasLeak(self):
		groupBox = QGroupBox("Gas Cap Leaks")
		box = QVBoxLayout()
		
		box.addWidget(self.in_caps_gas_leak)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createCapsOilCleaned(self):
		groupBox = QGroupBox("Oil Cap Cleaned")
		box = QVBoxLayout()
		
		box.addWidget(self.in_caps_oil_cln)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createCapsGasCleaned(self):
		groupBox = QGroupBox("Gas Cap Cleaned")
		box = QVBoxLayout()
		
		box.addWidget(self.in_caps_gas_cln)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createSlider1(self):
		groupBox = QGroupBox("Slider 1 In Place")
		box = QVBoxLayout()
		
		box.addWidget(self.in_slider1)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createSlider2(self):
		groupBox = QGroupBox("Slider 2 In Place")
		box = QVBoxLayout()
		
		box.addWidget(self.in_slider2)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createPullCordFray(self):
		groupBox = QGroupBox("Pull Cord Frayed")
		box = QVBoxLayout()
		
		box.addWidget(self.in_pull_cord_fray)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createPullCordShort(self):
		groupBox = QGroupBox("Pull Cord Short")
		box = QVBoxLayout()
		
		box.addWidget(self.in_pull_cord_short)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createPullCordRetracts(self):
		groupBox = QGroupBox("Pull Cord Retracts")
		box = QVBoxLayout()
		
		box.addWidget(self.in_pull_cord_retract)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	def createMisc(self):
		groupBox = QGroupBox("Misc Comments")
		box = QVBoxLayout()
		
		box.addWidget(self.in_misc)
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
	# tab 2 widgets
	
	def createNewOp(self):
		groupBox = QGroupBox("New Operation")
		
		hbox1 = QHBoxLayout()
		hbox1.addWidget(self.date_box)
		hbox1.addWidget(self.label1)
		hbox1.addWidget(self.issue_box)
		hbox1.addWidget(self.label2)
		hbox1.addWidget(self.solution_box)
		
		hbox2 = QHBoxLayout()
		hbox2.addWidget(self.new_op_date)
		hbox2.addWidget(self.new_op_save)
		hbox2.addWidget(self.new_op_cancel)
		hbox2.setAlignment(Qt.AlignRight)
		
		vbox = QVBoxLayout()
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		
		groupBox.setLayout(vbox)
		groupBox.setMaximumHeight(120)
		
		return groupBox
		
		
	def createPrevOp(self):
		groupBox = QGroupBox("Previous Operations")
		
		vbox = QVBoxLayout()
		vbox.addWidget(self.previous_ops)
		
		groupBox.setLayout(vbox)
		
		return groupBox
		
	
 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
