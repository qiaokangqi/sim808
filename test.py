#!/usr/bin/env python
# coding=utf-8
__author__ = 'yangzhan'
import serial,time,math
#AT+CGNSINF
def getGPS():
	"""
	通过sim808获取串口返回的GPS坐标
	"""
	#modem = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) #树莓派
	modem = serial.Serial('COM5',9600,timeout=1)
	modem.write("AT+CGNSPWR=1\r")
	modem.readline()
	GPSStatus = modem.readline()
	time.sleep(2)

	modem.write("AT+CGNSINF\r")
	modem.readline()
	data = modem.readline()
	print data
	if data.startswith("+CGNSINF"):
		data = data.split(",")
		if data[3]=='':
			print "GPS未连接"
			
		else:
			#Latitude ±dd.dddddd [-90.000000,90.000000]
			Latitude = float(data[3])
			#Longitude ±ddd.dddddd [-180.000000,180.000000]
			Longitude = float(data[4])
			print "Latitude=",Latitude,";Longitude=",Longitude
			return (Latitude,Longitude)
		modem.close()


if __name__ == '__main__':
	getGPS()
