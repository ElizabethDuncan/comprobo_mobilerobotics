#!/usr/bin/python
from collections import deque
import math
from Queue import PriorityQueue
import numpy as np
import scipy.misc.pilutil as smp
import pickle
import rospy

map_vis = pickle.load( open( "starMapCut.p", "rb" ) )
map_info = pickle.load( open( "data2d.p", "rb" ) )

visited = set()
nodesToExplore = deque([])
# Farthest possible goal without recursion failure
goal = (2000, 2000)

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

BFS implementation using the Node object
Flattened - tested with goal 500 away x and y

"""

def expand_tree(node):

  priorityqueue = MyPriorityQueue()

  while True:
  
    # Check if current node is the goal node
    if node.pixels == goal:
      break

    # Find the pixels of all the neighbors
    child_right = (node.pixels[0] + 1, node.pixels[1])
    child_left = (node.pixels[0] - 1, node.pixels[1])
    child_up = (node.pixels[0], node.pixels[1] + 1)
    child_down = (node.pixels[0], node.pixels[1] - 1)
    child_right_down = (node.pixels[0] + 1, node.pixels[1] - 1)
    child_right_up = (node.pixels[0] + 1, node.pixels[1] + 1)
    child_left_down = (node.pixels[0] - 1, node.pixels[1] - 1)
    child_left_up = (node.pixels[0] - 1, node.pixels[1] + 1)

    surrounding_area = [child_right, child_left, child_up, child_down, child_right_down, child_right_up, child_left_up, child_left_down]

    # Iterate through the neighbors
    for current_pixel in surrounding_area:
      
      # Only add pixel is a child if it isn't visisted already
      if current_pixel not in visited and not hitObstacle(current_pixel):
        # Create new node
        next = Node(node, current_pixel)
        visited.add(next.pixels)
        #nodesToExplore.append(next)
        priorityqueue.put(next, manhattan_distance(next))

    #node = nodesToExplore.popleft()
    node = priorityqueue.get()

  # Once breaking, return the full path of the goal node
  return node.return_full_path()

    

def make_tree(start_pixel):
  # Make star_pixel the root of the tree
  # start_pixels is a tuple (x, y)
  root = Node(None, start_pixel)

  # Recursively expand the tree 
  return expand_tree(root)
      




print make_tree((0, 0))

def hitObstacle(pixel):
  if map_info[pixel[0]][pixel[1]] != 0:
    return False
  return True

# Example text to run priority queue
# root = Node(None, (0,0))
# right = Node(root, (10, 1

# queue = MyPriorityQueue()
# queue.put(root, 3)
# queue.put(right, 1)

# print queue.get().pixels
# print queue.get().pixels
