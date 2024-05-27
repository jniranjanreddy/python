a = ["apple", "banana", "cherry" , "apple", "cherry", "apple", "banana", "cherry"]


# Count the number of times the value "apple" appears in the list:
x = a.count("apple")
y = a.count("banana")
z = a.count("cherry")

i_apple = []
j_banana = []
k_cherry = []

for i in a:
    if i == "apple":
        i_apple.append(i)
        # print("Apple: ", i)
    elif i == "banana":
        j_banana.append(i)
        # print("Banana: ", i)
    else:
        k_cherry.append(i)
        # print("Cherry: ", i)

print(i_apple)