import serial
import os

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1, bytesize=8, parity='N', stopbits=1)
print(ser.name)

'''['\x01'] is the format that .readline() sees the data as'''

'''xdo functions'''
'''move function'''
def mouseMove(x,y):
	mM = "xdotool mousemove_relative -- " + str(x) + " " + str(y)
	'''print(mM)''''''test line to see what mM becomes'''
	os.system(mM)
'''click functions'''
def mouseClick(direction,B):
	cM = "xdotool mouse" + direction + " " + str(B)
	os.system(cM)

'''rate of travel variable'''
x = 10
y = 10

run = True
while run==True:
	a = '\x00'
	a = ser.readline(1)
	'''print(x)'''  '''test line to see raw data from serial port'''
	if a=='\x01':
		'''print("Left Button")'''
		B=1
		mouseClick("down",B)
		mouseClick("up",B)
	if a=='\x02':
		'''print("Right Button")'''
		B=3
		mouseClick("down",B)
		mouseClick("up",B)
	if a=='\x03':
		'''print("Down")'''
		mouseMove(0,y)
	if a=='\x04':
		'''print("Up")'''
		mouseMove(0,-y)
	if a=='\x05':
		'''print("Left")'''
		mouseMove(-x,0)
	if a=='\x06':
		'''print("Right")'''
		mouseMove(x,0)
ser.close
