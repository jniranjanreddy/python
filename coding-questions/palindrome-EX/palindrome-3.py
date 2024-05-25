myString = "Hello madam I am your Student madam"

convert_to_dictionary = myString.split() # it concerts to List
# convert_to_String = ' '.join(convert_to_dictionary) # Convert to back to string

# j = 0
# for i in convert_to_dictionary:
#     if i == i[::-1]:
#         j=j+1

# print("hey its palindrome: ", j)

# print(convert_to_dictionary)

# print(convert_to_String)

for i in convert_to_dictionary:
    if i == i[::-1]:
        print("hey its palindrome: ", i)
        