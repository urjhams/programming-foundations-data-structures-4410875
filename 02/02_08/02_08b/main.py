my_list = [1, 7, 3]
print(sorted(my_list, reverse=True))

student_grades = [('Alpha', 10),('Gama', 7), ('Beta', 22)]

print(sorted(student_grades))
print(sorted(student_grades, key=lambda x: x[1], reverse=True))