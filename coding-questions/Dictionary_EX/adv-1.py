student = {
    "Sno": [1,2,3,4,5],
    "name": ["Ranjith", "Niranjan", "sagar", "alfa", "beta"],
    "physics": [80,70,60,50,45],
    "chemistry": [75,40,80,50,67],
    "maths": [70,75,60,83]
}

student["TotalMarks"] = []
student["TotalAverage"] = []
student["Grade"] = []



for i,j,k,l,m in zip(student["Sno"],student["name"],student["physics"],student["chemistry"],student["maths"]):
    totalmarks = k+l+m
    totalAverage = totalmarks / 4
    student["TotalMarks"].append(totalmarks)
    student["TotalAverage"].append(totalAverage)
    if totalAverage >= 60 and totalAverage < 100:
        student["Grade"].append("A")
    elif totalAverage >= 50 and totalAverage < 60:
        student["Grade"].append("B")
    else: 
        student["Grade"].append("c")

print(student)


