from collections import deque

def first_binary_numbers(num):
  if num <= 0:
    return
  
  queue = deque()
  queue.append(1)
  
  for number in range(num):
    binary = queue.popleft()
    print(binary)
    queue.append(binary * 10)
    queue.append(binary * 10 + 1)
  
first_binary_numbers(6)