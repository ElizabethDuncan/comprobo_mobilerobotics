#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Vector3
from nav_msgs.srv import GetMap
import pickle

class pathNavigation:

	def __init__(self):
		rospy.wait_for_service("static_map")
		static_map = rospy.ServiceProxy("static_map", GetMap)
		try:
			self.map = static_map().map
		except:
			print "error receiving map"

		#self.map = pickle.load( open( "exampleArray.p", "rb" ) )



	def process(self):
		print "map"
		print self.map.info.origin.position.x
		#print self.map.info.height
		#print self.map.data
		#pickle.dump( self.map.data, open( "exampleArray.p", "wb" ) )


if __name__ == '__main__':
	path = pathNavigation()
	path.process()
