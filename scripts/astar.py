#!/usr/bin/python
visited = set([])

class Node():
  def __init__(self, parent, pixels):
    self.pixels = pixels
    self.coords = convert_to_m(pixels)
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

def make_tree(start_pixels):
  #Get all pixels next to root
  #root = Node(None, )
  pass


root = Node(None, (-51, -51))
next_right = Node(root,(-54, -55))
next_left = Node(root, (-38, -55))
next_next_right = Node(next_right, (-60, -60))

parent = next_next_right.return_parent()
print parent.pixels
print next_next_right.return_full_path()