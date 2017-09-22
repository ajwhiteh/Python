import serial
import os
import threading

ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1, bytesize=8, parity='N', stopbits=1)
print(ser.name)

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
def leftButton():
	if a=='\x01':
		'''print("Left Button")'''
		B=1
		mouseClick("down",B)
		mouseClick("up",B)
def rightButton():
	if a=='\x02':
		'''print("Right Button")'''
		B=3
		mouseClick("down",B)
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

run = True
while run==True:
	a = ser.readline(1)

	
	'''Button Threads'''
	lB =threading.Thread(target=leftButton)
	lB.start()
	rB =threading.Thread(target=rightButton)
	rB.start()
	'''Move Threads'''
	uM =threading.Thread(target=upMv)
	dM =threading.Thread(target=downMv)
	lM =threading.Thread(target=leftMv)
	rM =threading.Thread(target=rightMv)
	serial.threaded.ReaderThread(uM)
	dM.start()
	lM.start()
	rM.start()
	
	
ser.close
