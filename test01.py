#!/usr/bin/env python
import platform
import sys
#release = platform.linux_distribution()
#print release

"""
#THis is one Method
if "CentOS Linux" in platform.linux_distribution():
    print "This is CentOS"
else:
    print "This is Redhat"
"""

#THis is another method

release = ''.join(platform.linux_distribution())
print release
print release[0]
