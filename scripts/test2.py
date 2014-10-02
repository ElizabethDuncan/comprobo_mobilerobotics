import numpy as np
import scipy.misc.pilutil as smp
import pickle
import rospy
from geometry_msgs.msg import Twist, Vector3
from nav_msgs.srv import GetMap

# run roscore
# run rosrun map_server map_serr /home/jackfan108/comprobo2014/mobile_robotics/starmap.yaml


# rospy.wait_for_service("static_map")
# static_map = rospy.ServiceProxy("static_map", GetMap)
# mapinfo = static_map().map.info.origin
# print 'mapinfo: '
# print mapinfo
# try:
# 	map1 = static_map().map
# except:
# 	print "error receiving map"

# pickle.dump( map1.data, open( "exampleArray2.p", "wb" ) )
data = pickle.load( open( "exampleArray2.p", "rb" ) )
print 'type of data is ' + str(type(data))
print 'length of data is ' + str(len(data))


map_vis = np.zeros( (2048,2048,3), dtype=np.uint8)
for i in range(2048):
	for k in range(2048):
		d = data[2048*i+k]
		#print type(d)
		if d == -1:
			map_vis[i,k] = [128,128,128]
		elif d == 0:
			map_vis[i,k] = [255,255,255]
		else:
			#print d
			map_vis[i,k] = [0,0,0]

# make the origin red
for i in range(1023,1026):
	for k in range(1023,1026):
		map_vis[i,k] = [255,0,0]

x = 1323
y = 1123
for i in range(y, y+3):
	for k in range(x, x+3):
		map_vis[i,k] = [0,0,255]

#print map_vis
#print data
img = smp.toimage( map_vis )
img.show()
flag = True
while flag == True:
	a = raw_input("type something to close the window: ")
	flag = False
img.close()



# Create a 1024x1024x3 array of 8 bit unsigned integers
#data = np.zeros( (512,512,3), dtype=np.uint8 )

#data[512/2,512/2] = [254,0,0]       # Makes the middle pixel red
#data[512/2,512/2+1] = [0,0,255]       # Makes the next pixel blue

#img = smp.toimage( data )       # Create a PIL image
#img.show()                      # View in default viewer