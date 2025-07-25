
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
scores = [95, 85, 92, 88, 90]

# Create a Numbered List of Students
for i, student in enumerate(students, start=1):
    print(f"{i}. {student}")

# Pair Students with Their Scores Using enumerate()
for i, student in enumerate(students):
    print(f"{student}: {scores[i]}")

# Find Positions of High Scorers
max_score = max(scores)
for i, score in enumerate(scores):
    if score == max_score:
        print(f"{students[i]} scored {score} at position {i}")

# Identify and print the positions (indices) of students who scored above 90.
for i, score in enumerate(scores):
    if score > 90:
        print(f"{students[i]} scored {score} at position {i}")

# Map Positions to Student Names
position_to_student = {i: student for i, student in enumerate(students)}
print(position_to_student)
