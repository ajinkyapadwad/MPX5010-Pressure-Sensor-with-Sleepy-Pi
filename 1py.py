#python function to run the MPX5010DP pressure sensor with Arduino Uno


from nanpy import Arduino
from nanpy import serial_manager
serial_manager.connect('/dev/ttyS0')        # serial connection to Arduino
from time import sleep

LED =13                       # LED on Arduino Pin 10 (with PWM)
Arduino.pinMode(LED, Arduino.OUTPUT)

print"Starting"
print"5 blinks"
for i in range(0,5):
    Arduino.digitalWrite(LED, Arduino.HIGH)
    sleep(0.5)
    Arduino.digitalWrite(LED, Arduino.LOW)
    sleep(0.5)

# print"Changing brightness of LED"
# bright = 128                           # Mid brightness
# Arduino.analogWrite(LED, bright)
# Arduino.digitalWrite(LED,Arduino.HIGH)          # Turn on LED

# for i in range(0,200):
#     bright = bright + 8
#     if (bright > 200):          # LED already full on at this point
#         bright = 0          # Minimum power to LED
#     Arduino.analogWrite(LED, bright)           # Change PWM setting/brightness
#     sleep(0.05)

Arduino.digitalWrite(LED,Arduino.LOW)          # Turn off LED
print"Finished"

