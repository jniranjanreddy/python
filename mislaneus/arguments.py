#!/usr/bin/python
import sys
# if len(sys.argv) > 1:
#    if sys.argv[1] == "apply":  
#           print("apply")
#    elif sys.argv[1] == "destroy":
#        print("destroy")
#    else:
#        print("This Script usage", sys.argv[0], "apply/Destroy")
    



#if sys.argv[1] == "apply":
#   print("apply")
#elif sys.argv[1] == "destroy":
#   print("destyor")
#else: 
#   print("Usage of This script")
for i in range(1, 11): 
    
    # If i is equals to 6,   
    # continue to next iteration   
    # without printing  
    if i == 6: 
        continue
    else: 
        # otherwise print the value 
        # of i 
        print(i, end = " ")