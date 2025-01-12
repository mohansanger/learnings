# Creating a sample tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements in a tuple by index
element_at_index_2 = my_tuple[2]
print("Element at index 2:", element_at_index_2)
# Output: Element at index 2: 3

# Slicing a tuple to create a new tuple
slice_of_tuple = my_tuple[1:4]
print("Slice of tuple:", slice_of_tuple)
# Output: Slice of tuple: (2, 3, 4)

# Concatenating tuples to create a new tuple
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)
# Output: Concatenated tuple: (1, 2, 3, 4, 5, 6)

# Multiplying a tuple to repeat its elements
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)
# Output: Repeated tuple: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Checking for the existence of an element in a tuple
element_to_check = 3
if element_to_check in my_tuple:
    print(f"{element_to_check} exists in the tuple.")
else:
    print(f"{element_to_check} does not exist in the tuple.")
# Output: 3 exists in the tuple.

# Finding the index of an element in a tuple
index_of_4 = my_tuple.index(4)
print("Index of 4:", index_of_4)
# Output: Index of 4: 3

# Counting the occurrences of an element in a tuple
count_of_5 = my_tuple.count(5)
print("Count of 5:", count_of_5)
# Output: Count of 5: 1

# Trying to update a tuple (This will result in a TypeError)
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"Error: {e}")
# Output: Error: 'tuple' object does not support item assignment
