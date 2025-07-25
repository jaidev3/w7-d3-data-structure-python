employees = [("John", 50000, "Sales"), ("Jane", 60000, "Marketing"), ("Jim", 55000, "Sales"), ("Jill", 70000, "Marketing")]

def sort_by_salary(employees):
    return sorted(employees, key=lambda x: x[1])

print(sort_by_salary(employees))

def sort_by_department(employees):
    return sorted(employees, key=lambda x: x[2])

print(sort_by_department(employees))

def create_reversed_list(employees):
    return employees[::-1]

print(create_reversed_list(employees))

def sort_by_name_length(employees):
    return sorted(employees, key=lambda x: len(x[0]))

print(sort_by_name_length(employees))