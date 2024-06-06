from collections import deque

queue = deque()
queue.append("a")
queue.append("e")
queue.append("c")
queue.append("d")

while len(queue) > 0:
  print(queue.popleft())
