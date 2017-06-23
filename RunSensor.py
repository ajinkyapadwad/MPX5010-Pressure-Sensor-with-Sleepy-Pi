"""
Simple program to contiually read air pressure values from MPX5010DP sensor connected to Sleepy Pi 2
Connection :
"""

#import modules:
from pyfirmata import Arduino, util
from time import sleep
import os

#set variables:
board = Arduino('/dev/ttyS0')

it = util.Iterator(board)
it.start()

a0 = board.get_pin('a:0:i')
maxVal = 10000

valAvg = 0
finalVal = 0
valArray = []
sleep(3)
valNum=0
try:
    while True:
        valSum = 0
        for valNum in range(maxVal):
            val = a0.read()
            val=val*1000
            valSum = valSum + val
        valAvg = valSum / maxVal
        print "Avg : ", valAvg           
        
    
except Exception as e:
    print "python exception : ",e
    board.exit()
    os._exit()
