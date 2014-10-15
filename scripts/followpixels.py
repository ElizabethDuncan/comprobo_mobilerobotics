#!/usr/bin/env python
# Marena Richardson, October 9, 2014. Path Finding Project. 

import rospy 
import math
#import astar
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3, Point, Quaternion
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import tf
from tf.transformations import euler_from_quaternion
import matplotlib.pyplot as plt
import map_manipulation

class Follow_Path:
	def __init__(self):
		#self.pixels = astar.get_pixel_list()
		self.pixels = [(24, 49), (25, 49), (26, 49), (27, 49), (28, 49), (29, 49), (30, 49), (31, 49), (32, 49), (33, 49), (34, 49), (35, 49), (36, 49), (37, 49), (38, 49), (39, 49), (40, 49), (41, 49), (42, 49), (43, 49), (44, 49), (45, 49), (46, 49), (47, 49), (48, 49), (49, 49), (50, 49), (51, 49), (52, 49), (53, 49), (54, 49), (55, 49), (56, 49), (57, 49), (58, 49), (59, 49), (60, 49), (61, 49), (62, 49), (63, 49), (64, 49), (65, 49), (66, 49), (67, 49), (68, 49), (69, 49), (70, 49), (71, 49), (72, 49), (73, 49), (74, 49), (75, 49), (76, 49), (77, 49), (78, 49), (79, 49), (80, 49), (81, 49), (82, 49), (83, 49), (84, 49), (85, 49), (86, 49), (87, 49), (88, 49), (89, 49), (90, 49), (91, 49), (92, 49), (93, 50), (94, 51), (95, 52), (96, 53), (97, 54), (98, 55), (99, 56), (100, 57), (101, 58), (102, 59), (103, 60), (104, 61), (105, 62), (106, 63), (107, 64), (108, 65), (109, 66), (110, 67), (111, 68), (112, 69), (113, 70), (114, 71), (115, 71), (116, 71), (117, 71), (118, 72), (119, 73), (120, 74), (121, 75), (122, 76), (123, 77), (124, 78), (125, 79), (126, 80), (127, 81), (128, 82), (129, 83), (130, 84), (131, 85), (132, 86), (133, 87), (134, 88), (135, 89), (136, 90), (137, 91), (138, 92), (139, 93), (140, 94), (141, 95), (142, 96), (143, 96), (144, 96), (145, 96), (146, 96), (147, 96), (148, 97), (149, 97), (150, 97), (151, 97), (152, 97), (153, 97), (154, 97), (155, 97), (156, 97), (157, 97), (158, 97), (159, 97), (160, 97), (161, 97), (162, 98), (163, 99), (164, 100), (165, 100), (166, 100), (167, 100), (168, 100), (169, 100), (170, 100), (171, 100), (172, 100), (173, 100), (174, 100), (175, 100), (176, 100), (177, 100), (178, 101), (179, 102), (180, 103), (181, 104), (182, 105), (183, 106), (184, 107), (185, 108), (186, 109), (187, 110), (188, 111), (189, 112), (190, 113), (191, 114), (192, 114), (193, 115), (194, 116), (195, 117), (196, 118), (197, 119), (198, 120), (199, 121), (200, 122), (201, 123), (202, 124), (203, 125), (204, 126), (205, 127), (206, 128), (207, 129), (208, 130), (209, 131), (210, 132), (211, 133), (212, 134), (213, 135), (214, 136), (215, 137), (216, 138), (216, 139), (216, 140), (216, 141), (216, 142), (216, 143), (216, 144), (216, 145), (216, 146), (216, 147), (217, 148), (217, 149), (217, 150), (217, 151), (217, 152), (217, 153), (217, 154), (217, 155), (217, 156), (217, 157), (217, 158), (217, 159), (217, 160), (217, 161), (217, 162), (217, 163), (217, 164), (217, 165), (217, 166), (217, 167), (218, 168), (219, 169), (220, 170), (221, 171), (222, 172), (223, 173), (224, 174), (225, 175), (226, 176), (227, 177), (228, 178), (229, 179), (230, 180), (231, 181), (232, 182), (233, 183), (234, 184), (235, 185), (236, 186), (237, 187), (238, 188), (239, 189), (240, 190), (241, 191), (242, 192), (243, 193), (244, 194), (245, 195), (246, 196), (247, 197), (248, 198), (249, 199)]
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
				self.last_mini_goal = mini_goal
				self.current_ind += 5
				self.last_distance = 10
			else:
				self.done = True
			try:
				mini_goal = self.coords[self.current_ind]
			except IndexError:
				self.current_ind = -1 
				mini_goal = self.coords[-1]
			xdif = mini_goal[0] - self.last_mini_goal[0]
			ydif = mini_goal[1] - self.last_mini_goal[1]
			self.vector_goal = [xdif / math.hypot(xdif, ydif), ydif / math.hypot(xdif, ydif)]
		else:
			self.last_distance = distance
		vector_orientation = [-math.sin(self.orientation), math.cos(self.orientation)]
		self.directed_angle = math.degrees(math.atan2(self.vector_goal[1], self.vector_goal[0]) - math.atan2(vector_orientation[1], vector_orientation[0]))
		if self.directed_angle > 180:
			self.directed_angle = -(360 - self.directed_angle)
		print distance, vector_orientation, self.vector_goal, self.directed_angle, self.current_ind
		"""
		print self.pixels
		data = map_manipulation.open_files()
		map_vis = astar.paint_point(self.pixels, data[0], [0, 225, 0])
		img = smp.toimage( map_vis )
  		img.show() """

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