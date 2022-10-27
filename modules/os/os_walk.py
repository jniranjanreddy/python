import os
path = "/jnr/python/modules/subprocess"
# print(list(os.walk(path)))
print("-----------------------------")
# for each in os.walk(path):
#     print(each)
# un packing tuple
# for r,d,f in os.walk(path):
#      if len(f) != 0:
#         print(r)
for r,d,f in os.walk(path):
     if len(f) != 0:
        for each_file in f:
            print(os.path.join(r,each_file))