fruits_list = ["apple", "banana", "cherry", "orange", "pineapple", "mango"]
fruits_set = {"apple", "banana", "cherry", "orange", "pineapple", "mango"}
fruits_tuple = ("apple", "banana", "cherry", "orange", "pineapple", "mango")
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3, "orange": 4, "pineapple": 5, "mango": 6}

# Check for Membership
print("apple" in fruits_list)
print("apple" in fruits_set)
print("apple" in fruits_tuple)
print("apple" in fruits_dict)

# Find Length
print(len(fruits_list))
print(len(fruits_set))
print(len(fruits_tuple))
print(len(fruits_dict))

# Iterate and Print Elements
for fruit in fruits_list:
    print(fruit)
for fruit in fruits_set:
    print(fruit)
for fruit in fruits_tuple:
    print(fruit)
for fruit in fruits_dict:
    print(fruit)

# Compare Membership Testing Performance
import time
start_time = time.time()
for _ in range(100000):
    "apple" in fruits_list
end_time = time.time()
print(f"Time taken for list: {end_time - start_time} seconds")

start_time = time.time()
for _ in range(100000):
    "apple" in fruits_set
end_time = time.time()
print(f"Time taken for set: {end_time - start_time} seconds")

start_time = time.time()
for _ in range(100000):
    "apple" in fruits_tuple
end_time = time.time()
print(f"Time taken for tuple: {end_time - start_time} seconds")

start_time = time.time()
for _ in range(100000):
    "apple" in fruits_dict
end_time = time.time()
print(f"Time taken for dict: {end_time - start_time} seconds")

# Briefly explain which data structures are more efficient for membership checks and why.
# Set is more efficient for membership checks because it is implemented as a hash table, which allows for O(1) time complexity for membership checks.
# List is less efficient because it requires a linear search through the list, which has O(n) time complexity.
