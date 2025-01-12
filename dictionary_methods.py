# Creating a sample dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing a value by key using get()
name = my_dict.get('name')
print("Value for 'name':", name)
# Output: Value for 'name': Alice

# Accessing a value by key using bracket notation
age = my_dict['age']
print("Value for 'age':", age)
# Output: Value for 'age': 30

# Checking if a key exists in the dictionary using in
if 'city' in my_dict:
    print("'city' key exists in the dictionary.")
else:
    print("'city' key does not exist in the dictionary.")

# Removing a key-value pair using pop()
city = my_dict.pop('city')
print("Removed 'city' key with value:", city)
# Output: Removed 'city' key with value: New York

# Getting a list of all keys using keys()
keys_list = list(my_dict.keys())
print("Keys in the dictionary:", keys_list)
# Output: Keys in the dictionary: ['name', 'age']

# Getting a list of all values using values()
values_list = list(my_dict.values())
print("Values in the dictionary:", values_list)
# Output: Values in the dictionary: ['Alice', 30]

# Getting a list of key-value pairs as tuples using items()
items_list = list(my_dict.items())
print("Key-value pairs in the dictionary:", items_list)
# Output: Key-value pairs in the dictionary: [('name', 'Alice'), ('age', 30)]

# Copying a dictionary using copy()
dict_copy = my_dict.copy()
print("Copy of the dictionary:", dict_copy)

# Clearing all key-value pairs from a dictionary using clear()
my_dict.clear()
print("After clear() on my_dict:", my_dict)
# Output: After clear() on my_dict: {}

# Merging two dictionaries using update()
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print("After update() with dict2 on dict1:", dict1)
# Output: After update() with dict2 on dict1: {'a': 1, 'b': 3, 'c': 4}

# Iterating through keys and values in a dictionary
for key, value in dict1.items():
    print(f"Key: {key}, Value: {value}")
# Output:
# Key: a, Value: 1
# Key: b, Value: 3
# Key: c, Value: 4
