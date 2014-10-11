#!/usr/bin/env python
# Marena Richardson, October 9, 2014. Path Finding Project. 

import rospy 
import math
import astar
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3, Point, Quaternion
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import tf
from tf.transformations import euler_from_quaternion
import matplotlib.pyplot as plt

class Follow_Path:
	def __init__(self):
		self.pixels = astar.get_pixel_list()
		#self.pixels = [(1072, 1026), (1071, 1026), (1070, 1026), (1069, 1026), (1068, 1026), (1067, 1026), (1066, 1026), (1065, 1026), (1064, 1026), (1063, 1026), (1062, 1026), (1061, 1026), (1060, 1026), (1059, 1026), (1058, 1026), (1057, 1026), (1056, 1026), (1055, 1026), (1054, 1026), (1053, 1026), (1052, 1026), (1051, 1026), (1050, 1026), (1049, 1026), (1048, 1026), (1047, 1026), (1046, 1026), (1045, 1026), (1044, 1026), (1043, 1026), (1042, 1026), (1041, 1026), (1040, 1026), (1039, 1026), (1038, 1026), (1037, 1026), (1036, 1026), (1035, 1026), (1034, 1026), (1033, 1026), (1032, 1026), (1031, 1026), (1030, 1026), (1029, 1026), (1028, 1026), (1027, 1026), (1026, 1026), (1025, 1026), (1024, 1026), (1023, 1026)]
		self.coords = []
		self.pixel_to_coords()
		self.current_ind = 5
		self.directed_angle = None
		self.done = False
		self.last_distance = 10
		#plt.plot([p[0] for p in self.pixels], [p[1] for p in self.pixels], 'o')
		#plt.plot([p[0] / 0.05 for p in self.coords], [p[1] / 0.05 for p in self.coords], 'o')
		#plt.show()

	def pixel_to_coords(self):
		pixel_start = self.pixels[0]
		for i in range(0, len(self.pixels)):
			self.coords.append(((self.pixels[i][0]-pixel_start[0]) * 0.05, -(self.pixels[i][1]-pixel_start[1]) * 0.05))

	def get_directed_angle(self):
		mini_goal = self.coords[self.current_ind]
		distance = math.sqrt((self.pose[0] - mini_goal[1])**2 + (-self.pose[1] - mini_goal[0])**2)
		if distance < 0.25 or round(self.last_distance, 2) < round(distance, 2):
			if self.current_ind != -1 and self.current_ind != len(self.coords) - 1:
				self.current_ind += 5
				self.last_distance = 10
			else:
				self.done = True
			try:
				mini_goal = self.coords[self.current_ind]
			except IndexError:
				self.current_ind = -1 
				mini_goal = self.coords[-1]
		else:
			self.last_distance = distance
		vector_orientation = [-math.sin(self.orientation), math.cos(self.orientation)]
		vector_goal = [mini_goal[0] / math.hypot(mini_goal[0], mini_goal[1]), mini_goal[1] / math.hypot(mini_goal[0], mini_goal[1])]
		self.directed_angle = math.degrees(math.atan2(vector_goal[1], vector_goal[0]) - math.atan2(vector_orientation[1], vector_orientation[0]))
		if self.directed_angle > 180:
			self.directed_angle = -(360 - self.directed_angle)
		print mini_goal, distance, self.directed_angle * 0.2, self.current_ind

	def odom_received(self, odom_data):
		orient = odom_data.pose.pose.orientation
		pose = odom_data.pose.pose.position
		self.pose = (pose.x, pose.y)
		rotation = (orient.x, orient.y, orient.z, orient.w)
		self.orientation = tf.transformations.euler_from_quaternion(rotation)[2]
		self.get_directed_angle()

	def main(self):
		pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
		sub = rospy.Subscriber('/odom', Odometry, self.odom_received)
		rospy.init_node('follow_path', anonymous=True)
		r = rospy.Rate(10)
		while not rospy.is_shutdown() and self.done == False: 
			if self.directed_angle != None:
				if math.fabs(self.directed_angle) > 8:
					msg = Twist(angular=Vector3(z = self.directed_angle * 0.01))
				else:
					msg = Twist(linear=Vector3(x=0.1), angular=Vector3(z= self.directed_angle * 0.05))
				pub.publish(msg)
		if self.done == True:
			print "Done"
			msg = Twist(linear=Vector3(x=0), angular=Vector3(z=0))
			pub.publish(msg)
			r.sleep()

if __name__ == '__main__':
	try:
		myProgram = Follow_Path()
		myProgram.main()
	except rospy.ROSInterruptException: pass