sts = "how are you doing my dear friend "



words = sts.split(" ")
c= 0
pos = 0

for i in words :
    c=c+1
    if i == "doing":
        pos =c

words[pos-1] ="sleeping"


sts2 ="" # empty String
for j in words:
    sts2=sts2+" "+j 
# sts = "how are you doing my dear friend "

print(sts2)



