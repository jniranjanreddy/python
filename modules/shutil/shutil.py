#!/usr/bin/env python3
import shutil
# f = open('data.txt', 'r')
# f1 = open('data1.txt', 'w')
# shutil.copyfileobj(f, f1)

# f.close()
# f1.close()
# shutil.copy('data.txt', 'data1.txt')
shutil.copyfile('data.txt', '/tmp/', follow_symlinks = True)  