import sys
import csv
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, 
	QWidget, QAction, QTabWidget, QVBoxLayout, QScrollArea, QGridLayout,
	 QComboBox, QGroupBox, QLineEdit, qApp)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from csv_mod import CSV_Handle
 
class App(QMainWindow):
 
	def __init__(self):
		super().__init__()
		
		#self.setStyleSheet(open("darkstyle.qss", "r").read())
		
		self.title = 'Shop Tech'
		self.left = 10
		self.top = 30
		self.width = 640
		self.height = 520
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
		
		self.table_widget = MyTableWidget(self)
		self.setCentralWidget(self.table_widget)
		
		self.csv_data = CSV_Handle()
 
		self.show()
		
	@pyqtSlot()
	def csv_update(self):
		'''transfers data from report folder to csv'''
		#print('Updated')
		self.csv_data.fill_file_list()
		self.csv_data.csv_transfer()
		
	def todo(self):
		'''Opens window with all saws needing attention'''


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
		tab = QWidget()
		
		# Create second tab
		# Create tabs grid
		tabGrid = QGridLayout()
		tabGrid.addWidget(self.createSawSelectOperations())
		
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
		box.addStretch(1)
		
		groupBox.setLayout(box)
		
		return groupBox
		
		
	@pyqtSlot()
	def saw_select_maint_logs(self):
		'''Take selected saw and display latest info'''
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
		print(str(self.saws2.currentText()))
		
		
	
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
 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
