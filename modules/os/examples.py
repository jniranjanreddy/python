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

# result = os.path.exists("file_name") #giving the name of the file as a parameter.
# print(result)
# print(os.name)
# print(os.curdir)
# print(os.confstr_names)            
# print(os.defpath)                   
# print(os.devnull)                  
# print(os.environ)                  
# print(os.environb)                  
# print(os.errno)                 
# print(os.extsep)                    
# print(os.linesep)                 
# print(os.name)                
# print(os.pardir)                  
# print(os.path)                 
# print(os.pathconf_names)         
# print(os.pathsep)   

# print(os.sep)                
# print(os.st)
# print(os.supports_bytes_environ)
# print(os.supports_dir_fd)
# print(os.supports_effective_ids)
# print(os.supports_fd)
# print(os.supports_follow_symlinks)

# print(os.path.getatime('/jnr/python/modules/os'))
# print(os.path.getctime('/jnr/python/modules/os'))

# print(fileType)
# print(os.sysconf_names)

#--------split------------
myPATH = "/jnr/python/modules/os"
afSplit = os.path.split(myPATH)
print(afSplit)
# for i in afSplit:
#
# print(i)

##-----Environment-------------
# print(os.environ["USER"])
# print(os.getenv("USER", "HOME"))
# Check if environemnt variable exist
# if 'USER' in os.environ:
#     print("User exist")
# else: 
#     print("User not exist:")
API_KEY = '123abc'
a = "rame"
