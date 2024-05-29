# Merge
# list_1 = [2,3,5,4,1]
# list_2 = [10,9,7,8,6,12,11]

# sort_list_1 = sorted(list_1)
# sort_list_2 = sorted(list_2)



# print(sort_list_1 + sort_list_2)

list_1 = [10,3,5,1,2,7]
list_2 = [9,8,6,12,2,4]

sort_list_1 = sorted(list_1)
sort_list_2 = sorted(list_2)

SortedAll = sort_list_1 + sort_list_2

print(sorted(SortedAll))
print(set(SortedAll))

# def remove_duplicates(lst):
#     # return list(set(lst))
#     myList = []
#     myList.append(lst)
#     # mySet = set(a)
#     # print(type([myList]))
#     print(myList)

# # Example usage
# # print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
# remove_duplicates([1,2,3,3,45])
a = [1,2,2,3,4,5,5]
print(type(a))
print(set(a))
print(type(set(a)))