#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Vector3

class pathNavigation:

	def __init__(self):
		#Get map data
		rospy.wait_for_service("static_map")
		static_map = rospy.ServiceProxy("static_map", GetMap)
		try:
			map = static_map().map
		except:
			print "error receiving map"

	def process(self):
		print "map"
		print map


if __name__ == '__main__':
	path = pathNavigation()
	path.process()
