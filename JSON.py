import json

x={
    "name":"Ram",
    "age":"Infinite",
    "City": "Vaikunt"
}

x1=x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y=json.dumps(x)
y1=json.dumps(x1)
print(y)
print(y1)