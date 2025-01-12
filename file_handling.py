# Creating a new text file and writing data to it
with open('example.txt', 'w') as file:
    file.write("This is line 1.\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

# Reading the entire file

with open('example.txt', 'r') as file:
    content = file.read()
    print("Reading the entire file:")
    print(content)

# Reading one line at a time

with open('example.txt', 'r') as file:
    line = file.readline()
    print("\nReading one line at a time:")
    while line:
        print(line.strip())  # Strip removes the newline character
        line = file.readline()

# Reading all lines into a list

with open('example.txt', 'r') as file:
    lines = file.readlines()
    print("\nReading all lines into a list:")
    print(lines)
    for line in lines:
        print(line.strip())

# Appending data to the file

with open('example.txt', 'a') as file:
    file.write("This is a new line added through append.\n")

# Reading the file after appending

with open('example.txt', 'r') as file:
    content = file.read()
    print("\nReading the file after appending:")
    print(content)

# File navigation (moving to the beginning of the file)

with open('example.txt', 'r') as file:
    file.seek(20)
    content = file.read()
    print("\nFile navigation - moving to the beginning of the file:")
    print(content)

# Handling exceptions (trying to open a non-existent file)


try:
    with open('example.txt', 'r') as file:
        data = file.red()
except Exception  as e:
    print("\nHandling exceptions:")
    print(f"Error: {e}")


# Deleting the file

import os

if os.path.exists('example.txt'):
    os.remove('example.txt')
    print("\nDeleting the file: 'example.txt'")
else:
    print("\nThe file 'example.txt' does not exist.")

# Check if the file was deleted

if os.path.exists('example.txt'):
    print("The file 'example.txt' still exists.")
else:
    print("The file 'example.txt' has been deleted.")
