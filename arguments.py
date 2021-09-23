#!/usr/bin/python
import sys
if len(sys.argv) > 1:
   if sys.argv[1] == "apply":  
          print("apply")
   elif sys.argv[1] == "destroy":
       print("destroy")
   else:
       print("This Script usage", sys.argv[0], "apply/Destroy")
    



#if sys.argv[1] == "apply":
#   print("apply")
#elif sys.argv[1] == "destroy":
#   print("destyor")
#else: 
#   print("Usage of This script")
