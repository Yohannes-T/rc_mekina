#!/usr/bin/env python
import rospy
import serial
from std_msgs.msg import*

ser = serial.Serial()
ard_codes = {"Front Distance": "a", "Forward": "d", "Backward": "e",  "Stop": "f", "Right":"g", "Left":"h", "No turning": "i"}
def serial_write(command):
	try:
		ser.write(command)
	except:
		if(ser.isOpen()): ser.close()
		if not(ser.isOpen()):ser.open()

def p(d):
	serial_write(ard_codes[d])
def handler(distance):
	distance = eval(ser.readline())
	if(distance<10):
		p("Stop")
		print distance,"  stop"
	else:
		p("Forward")
		print distance,"forward"
def init():
	rospy.init_node("follow_me")	
	ser.baudrate = 9600
	ser.port='/dev/rfcomm0'
	rospy.Subscriber("/dist", String, handler) 
	ser.timeout = 2
	ser.open()
	rate = rospy.Rate(10)
	print "jkl;"
	if not(ser.isOpen()):
		rospy.logerr("Eroor: could not open bluetooth serial port")
	while not rospy.is_shutdown():
		try:
			p("Front Distance")
			distance = eval(ser.readline())
			if(distance<10):
				p("Stop")
				print distance,"  stop"
			else:
				p("Forward")
				print distance,"forward"
		except:
			if(ser.isOpen()):ser.close()
			if not(ser.isOpen()):ser.open()
			if not(ser.isOpen()): rospy.logger("could not open porsdt")
		rate.sleep()
	rospy.spin()
init()
	
	



