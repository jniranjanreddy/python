import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "street": "Road 7",
  "a": ""
}

# # convert into JSON:
y = json.dumps(x)

# # the result is a JSON string:
# # print(y) 

# count = 0
# for i in x.keys():
#     count += 1
# print("Number of Keys:", count)
######################################
import json

y = {
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

print(json.dumps(x, indent=4, sort_keys=True))