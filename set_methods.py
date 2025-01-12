# Creating two sample sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Adding an element to a set using add()
set1.add(6)
print("After add(6) to set1:", set1)
# Output: After add(6) to set1: {1, 2, 3, 4, 5, 6}

# Removing an element from a set using remove() - Raises an error if the element is not present
set1.remove(3)
print("After remove(3) from set1:", set1)
# Output: After remove(3) from set1: {1, 2, 4, 5, 6}

# Removing an element from a set using discard() - No error if the element is not present
set1.discard(3)
print("After discard(3) from set1:", set1)
# Output: After discard(3) from set1: {1, 2, 4, 5, 6}

# Copying a set using copy()
set1_copy = set1.copy()
print("Copy of set1:", set1_copy)
# Output: Copy of set1: {1, 2, 4, 5, 6}

# Clearing all elements from a set using clear()
set1.clear()
print("After clear() on set1:", set1)
# Output: After clear() on set1: set()

# Checking if a set is a subset of another using issubset()
is_subset = set1_copy.issubset(set2)
print("Is set1_copy a subset of set2:", is_subset)
# Output: Is set1_copy a subset of set2: False

# Checking if a set is a superset of another using issuperset()
is_superset = set1_copy.issuperset(set2)
print("Is set1_copy a superset of set2:", is_superset)
# Output: Is set1_copy a superset of set2: False

# Union of two sets using union() or |
union_set = set1_copy.union(set2)
print("Union of set1_copy and set2:", union_set)
# Output: Union of set1_copy and set2: {1, 2, 4, 5, 6, 3, 7}

# Intersection of two sets using intersection() or &
intersection_set = set1_copy.intersection(set2)
print("Intersection of set1_copy and set2:", intersection_set)
# Output: Intersection of set1_copy and set2: {4, 5}

# Difference of two sets using difference() or -
difference_set = set1_copy.difference(set2)
print("Difference between set1_copy and set2:", difference_set)
# Output: Difference between set1_copy and set2: {1, 2, 6}

# Symmetric difference of two sets using symmetric_difference() or ^
symmetric_difference_set = set1_copy.symmetric_difference(set2)
print("Symmetric difference between set1_copy and set2:", symmetric_difference_set)
# Output: Symmetric difference between set1_copy and set2: {1, 2, 3, 6, 7}

# Adding elements from one set to another using update()
set1_copy.update(set2)
print("After update() with set2 on set1_copy:", set1_copy)
# Output: After update() with set2 on set1_copy: {1, 2, 3, 4, 5, 6, 7}

# Removing elements that are common between two sets using difference_update()
set1_copy.difference_update(set2)
print("After difference_update() with set2 on set1_copy:", set1_copy)
# Output: After difference_update() with set2 on set1_copy: {1, 2}
