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