def check_match(str):
  stack = []
  for char in str:
    if char == '(': stack.append(char)
    elif char == ')':
      if not stack: return False  # empty list
      stack.pop()
  return len(stack) == 0

print(check_match('(linked)in'))
print(check_match('(linke'))
print(check_match('linked)in'))
