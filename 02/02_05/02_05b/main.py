seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

# print(seating_chart[2][1])

for index, row in enumerate(seating_chart):
    print(f'row {index + 1}')
    for column, studentName in enumerate(row):
        print(f'seat {column + 1}: {studentName}')