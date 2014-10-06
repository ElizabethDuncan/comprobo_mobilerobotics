#!/usr/bin/python
from collections import deque

visited = set()
nodesToExplore = deque([])
# Farthest possible goal without recursion failure
goal = (500, 500)
allie = 0

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

2nd implementation without using objects or recursion
Trying to fix maximum recursion depth error

"""
def astar(start, finish):
  queue = deque([])
  queue.append((start, []))
  visited.add(start)
  while queue:

    node, path = queue.pop()

    if node == finish:
      return path

    child_right = (node[0] + 1, node[1])
    child_left = (node[0] - 1, node[1])
    child_up = (node[0], node[1] + 1)
    child_down = (node[0], node[1] - 1)
    child_right_down = (node[0] + 1, node[1] - 1)
    child_right_up = (node[0] + 1, node[1] + 1)
    child_left_down = (node[0] - 1, node[1] - 1)
    child_left_up = (node[0] - 1, node[1] + 1)

    neighbors = [child_right, child_left, child_up, child_down, child_right_down, child_right_up, child_left_up, child_left_down]


    for neighbor in neighbors:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, path + [node]))

  return None

def manhattan_distance():
  pass


"""

BFS implementation using the Node object
Flattened - tested with goal 500 away x and y

"""

def expand_tree(node):

  while True:
  
    # Check if current node is the goal node
    if node.pixels == goal:
      print node.return_full_path()
      exit()

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
      if current_pixel not in visited:
        # Create new node
        next = Node(node, current_pixel)
        visited.add(next.pixels)
        nodesToExplore.append(next)

    node = nodesToExplore.popleft()

    

def make_tree(start_pixel):
  # Make star_pixel the root of the tree
  # start_pixels is a tuple (x, y)
  root = Node(None, start_pixel)

  # Recursively expand the tree 
  expand_tree(root)
      



print make_tree((0, 0))

# Call to alternate BFS implementation
# root = Node((20, 20))
#print astar((20, 20), (11, 20))