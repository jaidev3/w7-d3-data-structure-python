students = [("101", "Alice", 85, 20), ("102", "Bob", 90, 22), ("103", "Charlie", 78, 21), ("104", "David", 88, 23)]

# Find the Student with the Highest Grade

highest_grade = max(students, key=lambda x: x[2])
print(highest_grade)

# Create a Name-Grade List

name_grade_list = [(student[1], student[2]) for student in students]

print(name_grade_list)


students[0] = ("101", "Alice", 86, 20)
print(students)
