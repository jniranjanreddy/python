# student = [
#    [1,2,3,4,5],
#    ["ranjit","pavani","kumar","kusuma","abhi"],
#    [200,300,400,500,600],
#    ["m","f","m","f","m"]
# ]
# male =[]
# female = []

# myMax = max(student[2])
# # print(myMax)
# for i,j,k,l in zip(student[0],student[1],student[2],student[3]):
#     if k == max(student[2]):
#         male.append(i)
#         male.append(j)
#         male.append(k)
#         male.append(l)
#     else:
#         female.append(i)
#         female.append(j)
#         female.append(k)
#         female.append(l)
# print(male)

a =[1,2,3,4,5,1,2,3,4]


b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)


