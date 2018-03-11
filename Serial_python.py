import serial,time
ser = serial.Serial('/dev/ttyUSB1')
# ser.port('/dev/ttyUSB0')
ser.baudrate=38400
if ser.is_open:
	ser.close()
ser.open()

ser.write("AT+RESET\r\n")
ser.flush()
line = ser.readline()
print(line)
time.sleep(1)
ser.write("AT+INIT\r\n")
ser.flush()
line = ser.readline()
print(line)
time.sleep(1)
ser.write("AT+INQM=1,1,48\r\n")
ser.flush()
line = ser.readline()
print(line)
time.sleep(1)

while 1:
	if ser.is_open:
		ser.close()
	ser.open()
	ser.write("AT+INQ\r\n")
	ser.flush()
	line = ser.readline()
	signal_str = line.split(',')[-1]
	signal_int=int(signal_str,16)
	print(signal_int)
	
	
	ser.close()
	time.sleep(0.1)