import json

# Sample data
data = {'key': 'value', 'number': 123, "name": "Niranjan"}

# Writing data to a JSON file
with open('simple.json', 'w') as file:
    json.dump(data, file)
