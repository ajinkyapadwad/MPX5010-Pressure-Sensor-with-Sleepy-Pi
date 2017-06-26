"""
A simple program to run MPX5010DP pressure sensor with Sleepy Pi 2
Analog read at Sleepy Pi (on chip Arduino Uno), reads an input sample per 100 uSecs. (= 10,000 readings per second)
Author: Ajinkya Padwad
Connections: 
	Sensor	USE	Sleepy Pi 2
	pin 1	output	pin 14 (FC0)
	pin 2	GND	GND
	pin 3 	VDD	5V
"""

#import libraries
from pyfirmata import Arduino, util
from time import sleep
import os

#function to run the sensor
def RunSensor():
	print "wait for around 10 seconds..."
	#set the board
	board = Arduino('/dev/ttyS0')

	#print "sleeping..."
	sleep(2) #very important.

	#start a thread
	it = util.Iterator(board)
	it.start()
 	
	#set the analog input pin on the Arduino ( Sleepy Pi )
	a0 = board.get_pin('a:0:i')
 
	try:
		#ignore first few 'nonetype' garbage values
		for i in range(10):
 	      		garbage = a0.read()
			#print garbage
			sleep(0.1)

		#continually read values
    		while True:
			v = a0.read()*1000
			sleep(0.5)
        		print "Pressure: ", v, " kPa"
    		
	except KeyboardInterrupt:
    		board.exit()
    		os._exit()

#it all starts here !
RunSensor()
