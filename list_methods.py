# Creating a sample list
my_list = [1, 2, 3, 4, 5]

# Append method: Adds an element to the end of the list
my_list.append(6)
print("After append(6):", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Extend method: Appends elements from an iterable to the end of the list
my_list.extend([7, 8])
print("After extend([7, 8]):", my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Insert method: Inserts an element at a specific index
my_list.insert(0, 0)
print("After insert(0, 0):", my_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Remove method: Removes the first occurrence of a value
my_list.remove(3)
print("After remove(3):", my_list)  # Output: [0, 1, 2, 4, 5, 6, 7, 8]

# Pop method: Removes and returns the element at a specific index
popped_value = my_list.pop(4)
print(f"Popped value at index 4: {popped_value}, List after pop(4):", my_list)
# Output: Popped value at index 4: 5, List after pop(4): [0, 1, 2, 4, 6, 7, 8]

# Index method: Returns the first index of a value
index_of_6 = my_list.index(6)
print(f"Index of 6:", index_of_6)  # Output: Index of 6: 4

# Count method: Counts the number of occurrences of a value
count_of_4 = my_list.count(4)
print(f"Count of 4:", count_of_4)  # Output: Count of 4: 1

# Sort method: Sorts the list in-place
my_list.sort()
print("After sort():", my_list)  # Output: [0, 1, 2, 4, 6, 7, 8]

# Reverse method: Reverses the list in-place
my_list.reverse()
print("After reverse():", my_list)  # Output: [8, 7, 6, 4, 2, 1, 0]

# Copy method: Creates a shallow copy of the list
copy_of_list = my_list.copy()
print("Copy of list:", copy_of_list)  # Output: [8, 7, 6, 4, 2, 1, 0]

# Clear method: Removes all elements from the list
my_list.clear()
print("After clear():", my_list)  # Output: []

# min method: Returns the minimum element in the list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value = min(my_list)
print(f"Minimum value:", min_value)  # Output: Minimum value: 1

# max method: Returns the maximum element in the list
max_value = max(my_list)
print(f"Maximum value:", max_value)  # Output: Maximum value: 9

# sum method: Returns the sum of all elements in the list
sum_of_values = sum(my_list)
print(f"Sum of values:", sum_of_values)  # Output: Sum of values: 48

# count method: Counts the number of occurrences of a value in the list
count_of_5 = my_list.count(5)
print(f"Count of 5:", count_of_5)  # Output: Count of 5: 3

# Del statement: Removes an element by index
del my_list[2]
print("After del my_list[2]:", my_list)  # Output: [3, 1, 1, 5, 9, 2, 6, 5, 3, 5]

# Calculate the average of the elements in the list
average = sum(my_list) / len(my_list)
print(f"Average:", average)  # Output: Average: 4.0
