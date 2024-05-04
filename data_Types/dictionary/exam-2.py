# Creating an empty dictionary
my_dict = {}

# Creating a dictionary with some key-value pairs
my_dict = {'name':'John', 'age':30, 'city':'New York'}

# Accessing a value using its key
# print(my_dict['name'])  # Output: John

# Using the get() method to access a value
# print(my_dict.get('age'))  # Output: 30

# Accessing a value that doesn't exist
# print(my_dict.get('gender'))  # Output: None

# Adding a new key-value pair
my_dict["gender"] = "Male"

# Updating the value of an existing key
my_dict['age'] = 31

# Iterating through keys

# for key in my_dict:
#     print(key, my_dict[key])

# print("------")

# for key, val in my_dict.items():
#     print(key, val)

print("------------")

# # Using 'in' keyword
# if 'age' in my_dict:
#     print("Name exists in the dictionary.")

# Priny only Values
dict_values = my_dict.values()
dict_keys = my_dict.keys()
# for i in dict_values:
#     print("Its type is", type(i))

# print("------------")
# for i in dict_keys:
#     print("Its type is", type(i))

# print(list(my_dict.values()))


# # Removing a key-value pair
# del my_dict['city']
# print(my_dict)


# for i in myList.items():
#     print(i)

# for i in myList:
#     print(type(i))
# print("---")

# items_view = my_dict.items()
# for i in items_view:
#     print(type(i))


a = my_dict.pop("gender")
print(a)
print(my_dict)