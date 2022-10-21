#!/usr/bin/env python3
import os
import re
#Print the current working 
# cwd = os.getcwd()
# print(f"Current working directory: ${cwd}") 
#----------
#Create Dir
# newDir = "dir-01"
# parentDir = "/tmp/"
# otherDir = "dir-02"
# target = os.path.join(parentDir,newDir,otherDir)
# print(target)
# path = os.path.join(parentDir,newDir)
# print(path)
# os.mkdir(target)

#---Regular Expression to find a folder ---------
# path = "/"
# dirList = os.listdir(path)
# print(dirList)

# #---Regular Expression to find a folder ---------
# path = "/"
# dirList = os.listdir(path)
# newlist = list(filter(r.match, dirList)) # Read Note below
# print(newlist)

# #------removing files-----
# targetPath = "/tmp/"
# file = 'file1.txt'
# path = os.path.join(targetPath,file)
# # os.removedirs(path) # For removing Dirs
# # os.remove(path)

# #---Rename File--------
# fd = "a.txt"
# os.rename(fd,'New.txt')

result = os.path.exists("file_name") #giving the name of the file as a parameter.
print(result)