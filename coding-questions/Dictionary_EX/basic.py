# # Create a dictionary

# mydict = {}

# mydict["a"] = 1
# mydict["b"] = 2
# mydict["c"] = 3

# print(mydict)

# # Check if a key exists in a dictionary.
# key = "d"
# valExist = "2"
# exists = key in mydict
# print(exists)

# # Update the value of an existing key in a dictionary.
# mydict["c"] = 4
# print(mydict)


#Remove a key-value pair from a dictionary using pop().
# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)

# rm = d.pop("c")
# print(d)


# Get the value associated with a key using get(), with a default value if the key is not found.
# d = {'a': 1, 'b': 2, 'c': 3}
# value = d.get("d", "key Not found")

# print(value)

# Merge Two dictionaries
# a = {'a': 8, 'b': 2, 'c': 3}
# b = {'a': 4, 'e': 5, 'f': 6}

# a_b = dict(**a),dict(**b)
# a_c = {**a,**b}

# print(a_b)
# print(a_c)

# Iterate over a dictionary and print each key-value pair.
# a = {'a': 8, 'b': 2, 'c': 3}

# for key, value in a.items():
#     # print("key is :", key, "Value is: ", value )
#     print(f"key is: {key}, Value is {value}")
# ##############

# Create a dictionary from two lists: one for keys and one for values.
# keys = ["a","b","c"]
# values = [1,2,3]

# updated_dict = dict(zip(keys,values))   # {'a': 1, 'b': 2, 'c': 3}
# # updated_dict = list(zip(keys,values)) # [('a', 1), ('b', 2), ('c', 3)]
# print(updated_dict)

# # Get a list of all keys and a list of all values in a dictionary.
# a = {'a': 8, 'b': 2, 'c': 3}

# myKeys = list(a.keys())     # ['a', 'b', 'c']
# myValues = list(a.values()) # [8, 2, 3]
# print(myKeys)

# Sort a dictionary by its keys.
##########################
# a = { 'b': 2, 'c': 3, 'a': 8,}
# sorted_dict = dict(sorted(a.items()))
# print(sorted_dict)
#######################

#Find the key with the maximum value in a dictionary.

# a = { 'b': 2, 'c': 3, 'a': 8,}

# my_values = [x for x in a.values()]
# my_keys = [x for x in a.keys()]

# min_value = min(my_values)
# max_value = max(my_values)

# print("max value :", max_value)
# print("min value", min_value)

# ####################################
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# # inverted_values = {value: key for key, value in my_dict.items()}

# sim = {x: y for x, y in my_dict.items()}
# print(sim)
# # print(inverted_values)
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
# key_to_remove = 2

# my_dict.pop("b")
# print(my_dict)

# my_dict["c"] = 4
# remove_a_key = { k: v  for k, v in  my_dict.items() if v != key_to_remove}
# print(remove_a_key)


##########
# words = ["apple", "anar", "banana", "cherry", "apricot", "blueberry"]
# grouped_words = {}
# for word in words:
#     first_letter = word[0]
#     if first_letter not in grouped_words:
#         grouped_words[first_letter] = [word]
#     else:
#         grouped_words[first_letter].append(word)
# print(grouped_words) 

# Combine two dictionaries by adding values for common keys.
# from collections import Counter
# dict1 = {'a': 1, 'c': 3, 'b': 15}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# combined_dict = dict(Counter(dict1) + Counter(dict2))
# # print(combined_dict)  # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}

# one_conter =  sorted(set(dict1))

# print(one_conter)

####################
# Count the frequency of each character in a string using a dictionary.
# s = "Hello world"

# freq_words = {}
# for i in s:
#     if i in freq_words:
#         freq_words[i] += 1
#     else:
#         freq_words[i] = 1
# print(freq_words)

###########
# Create a default dictionary that returns a default value for missing keys.
# from collections import defaultdict
# default_dict = defaultdict(lambda: 'Not Present')
# default_dict['a'] = 1
# print(default_dict['a'])  # Output: 1
# print(default_dict['b'])  # Output: Not Present

###################
# Find the average of values in a dictionary.

# d = {'a': 1, 'c': 3, 'd': 2}

# sum_of_keys =  sum(d.values()) / len(d)

# print(sum_of_keys)

# print(len(d))
#########################################
# Convert a list of tuples into a dictionary.
# tuples_list = [(1,2)]

# # tuples_list = [('a', 1), ('b', 2), ('c', 3)]
# my_dict = dict(tuples_list)
# print(my_dict)  











                   
