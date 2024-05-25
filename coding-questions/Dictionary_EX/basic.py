# #Create a dictionary with three key-value pairs and print it.
# my_dict = {'b': 2, 'c': 3, 'a': 1}
# print(my_dict)

# # Add a new key-value pair to an existing dictionary.
# my_dict = {'a': 1, 'b': 2}
# my_dict['c'] = 3
# print(my_dict)

# # Access the value associated with a specific key in a dictionary.
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# value = my_dict['b']
# print(value)

# # Remove a key-value pair from a dictionary.
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# del my_dict['b']
# print(my_dict)

# Check if a key exists in a dictionary.
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# key = 'b'
# exists = key in my_dict
# print(exists)

#Intermediate Level
# Iterate over the keys and values of a dictionary and print them.
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key, value in my_dict.items():
#     print(f'Key: {key}, Value: {value}')

# Merge two dictionaries.
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# merged_dict = {**dict1, **dict2}
# print(merged_dict)



# Get the keys of a dictionary as a list.

student = [
   [1,2,3,4,5],
   ["ranjit","pavani","kumar","kusuma","abhi"],
   [200,300,400,500,600],
   ["m","f","m","f","m"]
]
male =[]
female = []

for i,j,k,l in zip(student[0],student[1],student[2],student[3]):
    if l=="m":
        male.append(i)
        male.append(j)
        male.append(k)
        male.append(l)
    else:
        female.append(i)
        female.append(j)
        female.append(k)
        female.append(l)


    

