# Linear Search
list = [0,1,2,3,4,5,6,7,8,9,8]

item = 7

def search(item, list):
  for element in list:
    if element == item:
      return True
  return False

print(search(item, list))

# this index function also a linear search behind the scene
item_index = list.index(item)
print(item_index)