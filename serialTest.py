import serial
ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1, bytesize=8, parity='N', stopbits=1)
print(ser.name)

'''['\x01'] is the format that .readline() sees the data as'''


run = True
while run==True:
	x = '\x00'
	x = ser.readline(1)
	'''print(x)'''  '''test line to see raw data from serial port'''
	if x=='\x01':
		print("Left Button")
	if x=='\x02':
		print("Right Button")
	if x=='\x03':
		print("Down")
	if x=='\x04':
		print("Up")
	if x=='\x05':
		print("Left")
	if x=='\x06':
		print("Right")
ser.close
