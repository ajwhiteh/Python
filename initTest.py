import serial
import os
import threading
import sys
import glob

def list_ports():
    """ Lists serial port names
        EnvironmentError for unsupported or unknown platforms
        returns a list of the serial ports available on the system"""
    """if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]"""
    if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


"""print(list_ports())'''list_ports function test'''"""

"""Find and test serial Ports for controller"""

'''test'''"""
print(openPorts)
print(numPorts)"""

def establishConnection():
	openPorts = list_ports()
	numPorts = len(openPorts)
	i=0
	while (i <= numPorts):
		if (numPorts!=0):
			COM = openPorts[i]
			global ser
			ser = serial.Serial(port=COM, baudrate=115200, timeout=1, bytesize=8, parity='N', stopbits=1)
			if (ser.readline(16)=="Controller Ready"):
				print(ser.name)
				return True
			elif (i==numPorts - 1):
				i = 0
			else:
				i+=1
		else:
			openPorts = list_ports()
			numPorts = len(openPorts)

'''['\x01'] is the format that .readline() sees the data as'''

'''xdo functions'''
'''move'''
def mouseMove(x,y):
	mM = "xdotool mousemove_relative -- " + str(x) + " " + str(y)
	'''print(mM)''''''test line to see what mM becomes'''
	os.system(mM)
'''click'''
def mouseClick(direction,B):
	cM = "xdotool mouse" + direction + " " + str(B)
	os.system(cM)

'''read then send functions'''
def leftButtonDown():
	if a=='\x01':
		'''print("Left Button")'''
		B=1
		mouseClick("down",B)
def leftButtonUp():
	if a=='\x00':
		B=1
		mouseClick("up",B)
def rightButtonDown():
	if a=='\x02':
		'''print("Right Button")'''
		B=3
		mouseClick("down",B)
def rightButtonUp():
	if a=='\x07':
		B=3
		mouseClick("up",B)
def downMv():
	if a=='\x03':
		'''print("Down")'''
		mouseMove(0,y)
def upMv():
	if a=='\x04':
		'''print("Up")'''
		mouseMove(0,-y)
def leftMv():
	if a=='\x05':
		'''print("Left")'''
		mouseMove(-x,0)
def rightMv():
	if a=='\x06':
		'''print("Right")'''
		mouseMove(x,0)


'''rate of travel variable'''
x = 10
y = 10

run = False
while True:
	run = establishConnection()
	while run==True:
		
		try:
			ser.inWaiting()
		except:
			print("Disconnected")
			run = False
			break
		
		a=ser.readline(1)

		'''Button Threads'''
		lBd =threading.Thread(target=leftButtonDown)
		lBd.start()
		lBu =threading.Thread(target=leftButtonUp)
		lBu.start()
		rBd =threading.Thread(target=rightButtonDown)
		rBd.start()
		rBu =threading.Thread(target=rightButtonUp)
		rBu.start()
		'''Move Threads'''
		uM =threading.Thread(target=upMv)
		dM =threading.Thread(target=downMv)
		lM =threading.Thread(target=leftMv)
		rM =threading.Thread(target=rightMv)
		uM.start()
		dM.start()
		lM.start()
		rM.start()
