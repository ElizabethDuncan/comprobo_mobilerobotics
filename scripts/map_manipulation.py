#!/usr/bin/env python
import numpy as np
import scipy.misc.pilutil as smp
import pickle
import rospy

map_vis = pickle.load( open( "starMapCut.p", "rb" ) )
map_info = pickle.load( open( "map_info.p", "rb" ) )

# xmin = 1000
# ymin = 975
# xmax = 1410
# ymax = 1205

# x = xmax - xmin
# y = ymax - ymin

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



img = smp.toimage( map_vis )
img.show()
flag = True
while flag == True:
	continue
