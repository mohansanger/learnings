import json

# Example JSON data to write to a file
data_to_write = {
    "name": "Alice",
    "age": 30,
    "country": "USA",
    "languages": ["English", "Spanish"]
}
print(type(data_to_write))
# Writing data to a JSON file
with open('example.json', 'w') as jsonfile:
    json.dump(data_to_write, jsonfile, indent=4)

print("Data has been written to 'example.json'.")
print("\nReading data from 'example.json'...")

# Reading data from a JSON file
with open('example.json', 'r') as jsonfile:
    data = json.load(jsonfile)

print("\nData read from 'example.json':")
print(data)

# Modifying data and writing it back to the JSON file
data["age"] = 31
data["languages"].append("French")

with open('example.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)

print("\nData has been modified and written back to 'example.json'.")
print("\nReading updated data from 'example.json'...")

# Reading updated data from the JSON file
with open('example.json', 'r') as jsonfile:
    updated_data = json.load(jsonfile)

print("\nUpdated data read from 'example.json':")
print(updated_data)

# Deleting the JSON file
import os

if os.path.exists('example.json'):
    os.remove('example.json')
    print("\nDeleting the file: 'example.json'")
else:
    print("\nThe file 'example.json' does not exist.")

# Check if the file was deleted
if os.path.exists('example.json'):
    print("The file 'example.json' still exists.")
else:
    print("The file 'example.json' has been deleted.")
