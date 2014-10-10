#!/usr/bin/env python
import numpy as np
import scipy.misc.pilutil as smp
import pickle
import rospy

blue = [0,0,255]
red = [255,0,0]

# Variables from mapcut - size of map
xmin = 1000
ymin = 975
xmax = 1410
ymax = 1205

origin = (1024-xmin, 1024-ymin)
goal = (205, 115)

xlen = xmax - xmin
ylen = ymax - ymin


def create_robot_origin(origin):
	x = origin[0]
	y = origin[1]
	for i in range(y, y+3):
		for k in range(x, x+3):
			map_vis[i,k] = blue

def create_robot_goal(goal):
	x = goal[0]
	y = goal[1]
	for i in range(y, y+3):
		for k in range(x, x+3):
			map_vis[i,k] = red


# -1: Unknown
# 0 : Free Space
# 1 : Occupied
# 2 : Path
# 3 : Buffer Obstacle
def mapBuffer(map_info, map_vis):
	for i in range(xlen):
		for j in range(ylen):
			if map_info[j][i] == 1:
				for k in range(-5,6):
					for l in range(-5,6):
						map_info[j+k][i+l] = 3
						map_vis[j+k][i+l] = [255,0,255]
	return (map_info, map_vis)

def store_changes(map_vis, map_info):
	pickle.dump( map_vis, open( "starMapCut.p", "wb" ) )
	pickle.dump( map_info, open ( "map_info.p", "wb" ) )

def open_files():
	map_vis = pickle.load( open( "starMapCut.p", "rb" ) )
	map_info = pickle.load( open( "map_info.p", "rb" ) )
	return map_vis, map_info

def show_map(map_vis):
	img = smp.toimage( map_vis )
	img.show()

def keep_map_open():
	flag = True
	while flag == True:
		continue


if __name__ == '__main__':

	files = open_files()
	map_vis = files[0]
	map_info = files[1]
	#create_robot_goal(goal)
	#create_robot_origin(origin)

	map_info = mapBuffer(map_info, map_vis)[0]
	map_vis = mapBuffer(map_info, map_vis)[1]

	store_changes(map_info, map_vis)

	show_map(map_vis)
	
	keep_map_open()