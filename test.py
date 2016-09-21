import serial,time,math

modem = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

modem.write("AT+CGNSPWR=1\r")
modem.readline()
status = modem.readline()
time.sleep(2)
modem.write("AT+CGNSSEQ=\"RMC\"\r")
modem.readline()
status = modem.readline()
time.sleep(2)
modem.write("AT+CGNSTST=1\r")
modem.readline()
status = modem.readline()

time.sleep(2)


print "Starting loop..."
while True:
	try:
		line = modem.readline()
		if line.startswith("$GPGGA"):
			index = line.split(",")
			print index
			tempNdata = index[2] / 100
			tempEdata = index[4] / 100
			Ndata = math.floor(tempNdata)
			Edata = math.floor(tempEdata)
			tempNdata = (tempNdata - Ndata) * 100
			tempEdata = (tempEdata - Edata) * 100
			Ndata += tempNdata / 60
			Edata += tempEdata / 60
			print ('Got it! N: %s and E: %s',(Ndata,Edata))
		time.sleep(1)
	except:
		print "quitting"
		modem.write("AT+CGNSTST=0\r")
		modem.readline()
		exit(0)