import csv

# Example data to write to a CSV file
data_to_write = [
    ["Name", "Age", "Country"],
    ["Alice", 30, "USA"],
    ["Bob", 25, "Canada"],
    ["Charlie", 35, "UK"],
]

# Writing data to a CSV file
with open('example.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write each row of data
    for row in data_to_write:
        writer.writerow(row)

print("Data has been written to 'example.csv'.")
print("\nReading data from 'example.csv'...")

# Reading data from a CSV file

with open('example.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    print(type(reader))
    # Reading and printing each row of data
    for row in reader:
        print("Row:", row)

import pandas as pd
data = pd.read_csv('example.csv')
print(data)

# Appending data to an existing CSV file

new_data = ["David", 40, "Australia"]
with open('example.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Append the new data
    writer.writerow(new_data)

print("\nData has been appended to 'example.csv'.")
print("\nReading updated data from 'example.csv'...")

# Reading updated data from the CSV file
with open('example.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Reading and printing the updated data
    for row in reader:
        print("Row:", row)

# Deleting the CSV file
import os

if os.path.exists('example.csv'):
    os.remove('example.csv')
    print("\nDeleting the file: 'example.csv'")
else:
    print("\nThe file 'example.csv' does not exist.")

# # Check if the file was deleted
if os.path.exists('example.csv'):
    print("The file 'example.csv' still exists.")
else:
    print("The file 'example.csv' has been deleted.")
