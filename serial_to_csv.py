import serial
import csv
import time
from sys import platform


#<<TO-DO>>
'''
Need to test read loop
Need to figure out loop termination condition
Need to add field names to the CSV(possibly)
'''


#check operating system to use correct serial port
if platform == "linux" or platform == "linux2":
    #linux
    ser = serial.Serial('/dev/ttyACM0', timeout=1, baudrate=115200)
elif platform == "darwin":
    #macos x
    ser = serial.Serial('/dev/tty.HC-05-DevB', timeout=1 , baudrate=115200)
elif platform == "win32":
    #windows (Don't know if this will work with windows 11)
    ser = serial.Serial(port="COM4",timeout =1, baudrate=115200)

ser.flushInput()

#read loop
while True:
    try:
        '''this loop needs to be tested and modified, this may not read the
        way we want'''

        ser_read = ser.readline()
        decoded = float(ser_read[0:len(ser_read)-2].decode('utf-8'))
        print(decoded)
        writer = csv.writer(f,delimiter=',')
        writer.writerow([time.time(),decoded])
        
    except KeyboardInterrupt:
        #this condition will not work in a practical setting
        print("Keyboard Interrupt")
        break