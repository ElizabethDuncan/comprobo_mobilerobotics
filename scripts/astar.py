#!/usr/bin/python
from collections import deque
import math
from Queue import PriorityQueue
import numpy as np
import scipy.misc.pilutil as smp
import pickle
import rospy

map_vis = pickle.load( open( "starMapCut.p", "rb" ) )
map_info = pickle.load( open( "map_info.p", "rb" ) )

visited = set()
nodesToExplore = deque([])
start = (24,49)
goal = (330, 165)




def isFree(pixel):
  if map_info[pixel[1]][pixel[0]] == 0:
    return True
  return False

class Node():
  def __init__(self, parent, pixels):
    self.pixels = pixels
    # self.coords = convert_to_m(pixels)
    self.parent = parent
    if self.parent != None:
      self.parent.assign_child(self)
    self.children = []

  def return_parent(self):
    return self.parent

  def return_full_path(self):
    path = []
    while self.parent != None:
      path.append(self.parent.pixels)
      self = self.parent
    return path

  def assign_child(self, child):
    self.children.append(child)

  def convert_to_m(self):
    constant = .05
    width = 102.4
    return (self.pixels[0] * constant - width, self.pixels[1] * constant - width)



"""

Priority Queue used for A* heuristic
Returns the node with the lowest value first

"""
class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item

"""

A* Heuristic
Finds the "as the crow flies" distance between a given node and the goal node

"""
def manhattan_distance(node):

  current_x = node.pixels[0]
  current_y = node.pixels[1]

  goal_x = goal[0]
  goal_y = goal[1]

  distance = math.sqrt((goal_x - current_x)**2 + (goal_y - current_y)**2)

  return distance


"""

Get surrounding pixels (+/- 1) for a given x, y

"""

def get_surrounding_pixels(location):
  # Find the pixels of all the neighbors
  child_right = (location[0] + 1, location[1])
  child_left = (location[0] - 1, location[1])
  child_up = (location[0], location[1] + 1)
  child_down = (location[0], location[1] - 1)
  child_right_down = (location[0] + 1, location[1] - 1)
  child_right_up = (location[0] + 1, location[1] + 1)
  child_left_down = (location[0] - 1, location[1] - 1)
  child_left_up = (location[0] - 1, location[1] + 1)

  return [child_right, child_left, child_up, child_down, child_right_down, child_right_up, child_left_up, child_left_down]



"""

BFS implementation using the Node object
Flattened - tested with goal 500 away x and y

"""

def expand_tree(node):

  priorityqueue = MyPriorityQueue()

  while True:
    print node.pixels
    # Check if current node is the goal node
    if node.pixels == goal:
      break
    print 'node.pixels',node.pixels

    surrounding_area = get_surrounding_pixels(node.pixels)
    
    # Iterate through the all 8 pixels around the current x, y point
    for current_pixel in surrounding_area:
      
      # Only add pixel is a child if it isn't visisted already
      if current_pixel not in visited and isFree(current_pixel):
        # Create new node
        next = Node(node, current_pixel)
        visited.add(next.pixels)
        #nodesToExplore.append(next)
        priorityqueue.put(next, manhattan_distance(next))

    #node = nodesToExplore.popleft()
    node = priorityqueue.get()

  # Once breaking, return the full path of the goal node
  return node.return_full_path()

    

def paint_point((x,y),data,color):
  for i in range(y-1, y+2):
    for k in range(x-1, x+2):
      data[i,k] = color
  return data


def make_tree(start_pixel):
  # Make star_pixel the root of the tree
  # start_pixels is a tuple (x, y)c
  root = Node(None, start_pixel)

  # Recursively expand the tree 
  return expand_tree(root)
  

if __name__ == '__main__':

  path = make_tree(start)
  print 'done with search'
  print 'goal',goal
  print 'start',start
  print path
  for i in path:
    map_info[i[1]][i[0]] = 2
    map_vis[i[1],i[0]] = [0,255,0]

  map_vis = paint_point(start, map_vis, [0,0,255])
  map_vis = paint_point(goal, map_vis, [255,0,0])

  img = smp.toimage( map_vis )
  img.show()
  flag = True
  while flag == True:
    continue
