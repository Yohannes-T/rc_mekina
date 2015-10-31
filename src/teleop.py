#!/usr/bin/env python
import rospy
from std_msgs.msg import *
import sys, tty, select

rospy.init_node("teleop")
rate = rospy.Rate(2)
pub = rospy.Publisher("/forward", String, queue_size = 10)
while not rospy.is_shutdown():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = str(sys.stdin.read(1))
	if(key == "w"):
		pub.publish("Forward")
	elif(key == "d"):
		pub.publish("Right")
	elif(key == "a"):
		pub.publish("Left")
	elif(key == "i"):
		pub.publish("No turning")
	else:
		pub.publish("Stop")

rospy.spin()

