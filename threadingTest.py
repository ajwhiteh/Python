import serial
import os

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1, bytesize=8, parity='N', stopbits=1)
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
x = 2
y = 2

run = True
while run==True:
	a = ser.readline(1)
	
	leftButton()
	rightButton()
	downMv()
	upMv()
	leftMv()
	rightMv()
ser.close
