#!/usr/bin/env python
import numpy as np
import scipy.misc.pilutil as smp
import pickle
import rospy
from geometry_msgs.msg import Twist, Vector3
from nav_msgs.srv import GetMap

# specify xmin and ymin
# this program will show the cut map
# and save the new map as a pickle file

data = pickle.load( open( "exampleArray2.p", "rb" ) )

print 'done loading data'
print 'cutting...'

xmin = 1000
ymin = 975
xmax = 1410
ymax = 1205

map_info = np.zeros((ymax-ymin,xmax-xmin), dtype=np.int8)
map_vis = np.zeros( (ymax-ymin,xmax-xmin,3), dtype=np.uint8)
topleft = [2048,2048]
bottomright = [0,0]
for i in range(ymin,ymax):
	for k in range(xmin,xmax):
		d = data[2048*i+k]
		#print type(d)
		if d == -1:
			map_vis[i-ymin,k-xmin] = [128,128,128]
			map_info[i-ymin][k-xmin] = -1
		elif d == 0:
			map_vis[i-ymin,k-xmin] = [255,255,255]
			map_info[i-ymin][k-xmin] = 0
		else:
			map_vis[i-ymin,k-xmin] = [0,0,0]
			map_info[i-ymin][k-xmin] = 1

pickle.dump( map_vis, open( "starMapCut.p", "wb" ) )
pickle.dump( map_info, open ( "map_info.p", "wb" ) )

img = smp.toimage( map_vis )
img.show()
flag = True
while flag == True:
	#name = raw_input("Please enter file name you want to save as(pickle file): ")
	flag = False

#pickle.dump( map_vis, open( name + '.p', "wb" ) )