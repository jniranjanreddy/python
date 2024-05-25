str1 = "hello how are you"
str1split = str1.split()

str2 = "A great feeling"
str2Split = str2.split()



for i in str1split:
     for j in str2Split:
          print(i +" "+ j)

combinedString = []
combinedString.append(i + " "+ j)