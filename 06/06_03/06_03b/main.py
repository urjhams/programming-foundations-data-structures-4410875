from collections import deque

history_stack = deque()
history_stack.append("google")
history_stack.append("facebook")
history_stack.append("stackoverflow")

print(history_stack[-1])
print(history_stack.pop())
print(history_stack)