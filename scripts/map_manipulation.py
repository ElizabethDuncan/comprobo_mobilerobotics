#!/usr/bin/env python
import numpy as np
import scipy.misc.pilutil as smp
import pickle
import rospy

map_vis = pickle.load( open( "starMapCut.p", "rb" ) )
map_info = pickle.load( open( "map_info.p", "rb" ) )

print type(map_info)
for i in map_info:
	for k in i:
		print k

xmin = 1000
ymin = 975
xmax = 1410
ymax = 1205

x = xmax - xmin
y = ymax - ymin

#map_vis = np.zeros( (y,x,3), dtype=np.uint8)



img = smp.toimage( map_vis )
img.show()
flag = True
while flag == True:
	continue
