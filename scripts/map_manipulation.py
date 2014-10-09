#!/usr/bin/env python
import numpy as np
import scipy.misc.pilutil as smp
import pickle
import rospy

map_vis = pickle.load( open( "starMapCut.p", "rb" ) )
map_info = pickle.load( open( "map_info.p", "rb" ) )

xmin = 1000
ymin = 975
xmax = 1410
ymax = 1205

xlen = xmax - xmin
ylen = ymax - ymin

x = 1024-1000
y = 1024-975

for i in range(y, y+3):
	for k in range(x, x+3):
		map_vis[i,k] = [0,0,255]

x = 205
y = 115

for i in range(y, y+3):
	for k in range(x, x+3):
		map_vis[i,k] = [255,0,0]


#map_vis = np.zeros( (y,x,3), dtype=np.uint8)
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

map_info = mapBuffer(map_info, map_vis)[0]
map_vis = mapBuffer(map_info, map_vis)[1]

pickle.dump( map_vis, open( "starMapCut.p", "wb" ) )
pickle.dump( map_info, open ( "map_info.p", "wb" ) )

img = smp.toimage( map_vis )
img.show()
flag = True
while flag == True:
	continue
