#!/usr/bin/env python
import rospy
import serial
from std_msgs.msg import*

#ser = serial.Serial()
ard_codes = {"Front Distance": "a", "Forward": "d", "Backward": "e",  "Stop": "f", "Right":"g", "Left":"h", "No turning": "i"}
'''
def serial_write(command):
	try:
		ser.write(command)
	except:
		if(ser.isOpen()): ser.close()
		if not(ser.isOpen()):ser.open()

def p(d):
	serial_write(ard_codes[d])
'''
def handler(d):
	global pub
	distance = eval(d.data)
	if(distance < 10):
		pub.publish("Stop")
		pub2.publish("request")
		print distance,"  stop"
	else:
		pub.publish("Forward")
		pub2.publish("request")
		print distance,"forward"
def init():
	global pub
	global pub2
	rospy.init_node("follow_me")	
#	ser.baudrate = 9600
#	ser.port='/dev/rfcomm0'
	rospy.Subscriber("/dist", String, handler) 
	pub2 = rospy.Publisher("/req",String,queue_size = 10)
	pub = rospy.Publisher("/forward", String, queue_size = 10)
#	ser.timeout = 2
#	ser.open()
	pub2.publish("request")
	rate = rospy.Rate(10)
	print "jkl;"
#	if not(ser.isOpen()):
#		rospy.logerr("Eroor: could not open bluetooth serial port")
	
	rospy.spin()
init()
	
	



