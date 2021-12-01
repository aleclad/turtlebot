#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
import serial
import time
import json

# ----------------------------------------------------------
# serialSetup()
# initialize serial port
# ----------------------------------------------------------
def serialSetup(port,baud):
    # initialize serial port
    try:
        serialPort = serial.Serial(port=port, baudrate=baud, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        #serialPort = serial.Serial(port=port, baudrate=baud)
    except serial.serialutil.SerialException:
        print("DEVICE NOT CONNECTED!")
        exit()
    return serialPort


# ----------------------------------------------------------
# listen()
# ----------------------------------------------------------
def listen(serialPort):

    dataIn = ""
    while(True):
        # Wait until there is data waiting in the serial buffer
        if(serialPort.in_waiting > 0):
            while(serialPort.in_waiting > 0):
            # Read data out of the buffer until a carraige return / new line is found
                serialString = serialPort.readline()
                dataIn += serialString.decode('Ascii')
            return dataIn


# ----------------------------------------------------------
# send()
# send data without waiting for reply
# ----------------------------------------------------------
def send(serialPort, dataOut):

    serialPort.write(dataOut.encode())
    time.sleep(1)

    return


# initialize connection to arduino controlling braccio
filePath = '/dev/ttyACM0'     #/dev/ttyACM0
serialPort = serialSetup(filePath,115200)
time.sleep(8)

def talker():
    pub = rospy.Publisher('chatter', Bool, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = Bool()
    msg.data = False
    pub.publish(msg)
    print('test')
    while not rospy.is_shutdown():
	barcode = listen(serialPort)
	print(repr(barcode))
	if barcode == '1234567\r\n':
		print('success')
		msg.data = not msg.data
		pub.publish(msg)
		#print(listen(serialPort))

        
        #rospy.loginfo(True)
        #pub.publish(True)
        rate.sleep()
   
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass






