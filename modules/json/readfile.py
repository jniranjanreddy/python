import json

# Open and read data from a JSON file
with open('simple.json', 'r') as file:
    data = json.load(file)

# Accessing data
# print(data['key'])
print([i for i in data.keys()])
print([i for i in data.values() if i == "Niranjann" ] )