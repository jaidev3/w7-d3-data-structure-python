grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

# Slice grades from index 2 to 7
print(grades[2:7])

# Use list comprehension to find grades above 85
print([grade for grade in grades if grade > 85])

# Replace the grade at index 3 with 95
grades[3] = 95
print(grades)

# Append three new grades
grades.append(93)
grades.append(94)
grades.append(95)
print(grades)

# Sort in descending order and display the top 5 grades
grades.sort(reverse=True)
print(grades[:5])