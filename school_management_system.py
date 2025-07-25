
school = {
    "Math":{
        "teacher": "Mr. Smith",
        "students": {
            "Alice": 95,
            "Bob": 85,
            "Charlie": 90
        }
    },
    "Science":{
        "teacher": "Mrs. Johnson",
        "students": {
            "David": 88,
            "Eve": 92,
            "Frank": 87
        }
    }
}

for class_name, class_info in school.items():
    print(f"Teacher: {class_info['teacher']}")

# Calculate Class Average Grades

for class_name, class_info in school.items():
    print(f"Class: {class_name}")
    print(f"Average Grade: {sum(class_info['students'].values()) / len(class_info['students'])}")


# Find Top Student Across All Classes

for class_name, class_info in school.items():
    max_grade = 0
    max_student = None
    for student_name, grade in class_info['students'].items():
        if grade > max_grade:
            max_grade = grade
            max_student = student_name
    print(f"Top Student in {class_name}: {max_student} with grade {max_grade}")

# Use Unpacking

for class_name, class_info in school.items():
    for student_name, grade in class_info['students'].items():
        print(f"{student_name}: {grade}")



