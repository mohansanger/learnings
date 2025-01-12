# Original list
numbers = [1, 2, 3, 4, 5]

# Example 1: Creating a new list with each element squared
squared_numbers = [x**2 for x in numbers]
print("Squared numbers:", squared_numbers)
# Output: Squared numbers: [1, 4, 9, 16, 25]

# Example 2: Creating a new list with even numbers from the original list
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)
# Output: Even numbers: [2, 4]

# Example 3: Creating a new list by transforming elements with a function
def double(x):
    return x * 2

doubled_numbers = [double(x) for x in numbers]
print("Doubled numbers:", doubled_numbers)
# Output: Doubled numbers: [2, 4, 6, 8, 10]

# Example 4: Creating a list of tuples from two lists using zip
names = ["Alice", "Bob", "Charlie","abc"]
scores = [85, 92, 78]
student_info = [(name, score) for name, score in zip(names, scores)]
print("Student info:", student_info)
# Output: Student info: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Example 5: Creating a list of words with more than 3 characters
sentence = "This is a sample sentence with words of varying lengths."
words = sentence.split()
long_words = [word for word in words if len(word) > 3]
print("Long words:", long_words)
# Output: Long words: ['This', 'sample', 'sentence', 'with', 'words', 'varying', 'lengths.']
