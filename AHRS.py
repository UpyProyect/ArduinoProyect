#!/usr/bin/env python
import serial

serial_port = serial.Serial("/dev/ttyUSB0", baudrate = 9600)
while True:
	string = str(serial_port.readline())
	print(string)

port.close()

#To check which port is used type in the terminal: python -m serial.tools.list_ports