#!/usr/bin/python

class Node(parent, x, y):
  def __init__(self):
    self.x = x
    self.y = y
    self.parent = parent
    if self.parent != None:
      self.parent.assign_child(child)
    self.children = []

  def return_parent(self):
    return self.parent

  def assign_child(self, child):
    self.children.append(child)

class Queue():
  def __init__(self):
    self.array = []

  def push(self, element):
    self.array.append(element)

  def pop(self):
    return self.array.pop(0)

  def peek(self):
    if self.array:
      return self.array[0]
    else:
      return None


def bfs(graph, start, path = []):
  queue = Queue()
  queue.push(start)
  while queue.peek():
    v = queue.pop()
    if v not in path:
      path.append(v)
      expand_node(v, graph, queue)
  return path

def expand_node(node, graph, queue):
  for each in graph[node]:
    queue.push(each)


# root = Node(None, -51, -51)
# next_right = Node(root, -54, -55)
# next_left = Node(root, -38, -55)
# next_next_right = Node(next_right, -60, -60)

# parent = next_next_right.return_parent()
# print parent.x