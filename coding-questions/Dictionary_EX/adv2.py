student = [
   [1,2,3,4,5],
   ["ranjit","pavani","kumar","kusuma","abhi"],
   [200,300,400,500,600],
   ["m","f","m","f","m"]
]


for i,j,k,l in zip(student[0],student[1],student[2],student[3]):
    print(i,"   ",j,"   ",k,"   ",l)
