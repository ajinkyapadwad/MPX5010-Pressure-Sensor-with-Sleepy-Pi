"""
Simple program to contiually read air pressure values from MPX5010DP sensor connected to Sleepy Pi 2
Analog read at Sleepy Pi (Almost Arduino Uno !), reads an input sample per 100 uSecs. (= 10,000 readings per second)

"""

#import modules:
from pyfirmata import Arduino, util
from time import sleep
import os
from time import sleep

class RunSensor:
	def _init_(self):
		#set variables:
		self.board = Arduino('/dev/ttyS0')

		#start a thread
		self.it = util.Iterator(board)
		self.it.start()

		#set Analog pin 0 as input and configure
		self.a0 = board.get_pin('a:0:i')

		#set variables to continually read and print average for better accuracy
		self.maxVal = 10000
		self.valAvg = 0
		self.finalVal = 0
		self.valArray = []
		self.valNum=0

		#Start sensing
		ReadValues()

	def ReadValues(self):
		try:
			while True:
				self.valSum = 0
				for self.valNum in range(self.maxVal):
					self.val = self.a0.read()
					self.val=self.val*1000
					self.valSum = self.valSum + self.val
				self.valAvg = self.valSum / self.maxVal
				# print "Avg : ", self.valAvg           
				print "Pressure:", self.valAvg
							
		except Exception as e:
			print "python exception : ",e
			self.board.exit()
			self.os._exit()

		sys.exit(0)

def main():
	run = RunSensor()
	sys.exit(0)

if __name__ == "__main__":
	main()