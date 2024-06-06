set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}

union_set = set_A.union(set_B)
print(union_set)

intersection_set = set_A.intersection(set_B)
print(intersection_set)

difference_set_A = set_A.difference(set_B)
print(difference_set_A)

difference_set_B = set_B.difference(set_A)
print(difference_set_B)

symetric_difference_set = set_A.symmetric_difference(set_B)
print(symetric_difference_set)