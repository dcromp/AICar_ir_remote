#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO
import time
import rospy
from AlphaBot import AlphaBot2

class SimpleMover(object):
	def __init__(self):
		self.Ab = AlphaBot2()
		rospy.Subscriber('/action', String, self.move_cb)
		rospy.spin()

	def move_cb(self, msg):
		action = msg
		if msg == "foward":
			self.Ab.forward()
		if msg == "left":
			self.Ab.left()
		if msg == "stop":
			self.Ab.stop()
		if msg == "right":
			self.Ab.right()
		if msg == "backward":
			self.Ab.backward()


if __name__ == '__main__':
    try:
		rospy.init_node('simple_mover')
		SimpleMover()
	except rospy.ROSInterruptException:
        rospy.logerr('Could not start SimpleMover node.')
		GPIO.cleanup()
