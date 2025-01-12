import json

# Example Python dictionary
data = {"name": "Alice", "age": 30, "country": "USA"}

# Serializing (converting to JSON formatted string) using json.dumps()
json_str = json.dumps(data)
# print(type(data))
# Deserializing (parsing JSON formatted string) using json.loads()
loaded_data = json.loads(json_str)

print("Using json.dumps() and json.loads():")
print("Original data:", data)
print("JSON Formatted String:",json_str)
print("Loaded data:", loaded_data)
