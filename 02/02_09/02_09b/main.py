def find_second_smallest(my_list):
    if len(my_list) > 1: return sorted(my_list)[1]
    else: return None

# better solution with time complexity O(n)
def find_second_smallest_v2(my_list):
    smallest = float('inf')
    second_smallest = ('inf')
    for item in my_list:
        if item < smallest:
            second_smallest = smallest
            smallest = item
    return second_smallest
    
print(find_second_smallest([5, 8, 3, 2, 6]))
print(find_second_smallest_v2([5, 8, 3, 2, 6]))
