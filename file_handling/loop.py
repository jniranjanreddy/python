#!/usr/bin/env python3
# myContent = ['first line','second line','third line']
# # fo = open("with_loop.txt", "w")
# fo = open("with_loop.txt", "a")
# for each_line in myContent:
#    fo.write(each_line+"\n")
# fo.cloce()

# Reading file
fo = open("with_loop.txt","r")
data = fo.readlines()
fo.close()
for each in data:
   print(each)
