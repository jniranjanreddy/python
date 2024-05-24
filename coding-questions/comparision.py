sts ="HEllo Students how are yOu dOing"
sts2 ="i am so blessed students how about you"
chgCase = sts.lower()
chgCase2 = sts2.lower()

splitSTS = chgCase.split()
splitSTS2 = chgCase2.split()

count = 0
for i in splitSTS:
    for j in splitSTS2:
        if i == j:
            count += 1
print(count)
