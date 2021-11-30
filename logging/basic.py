#!/usr/bin/env python3
import logging
#logging.basicConfig(filename='log.txt',level=logging.WARNING) # by default file appended
#logging.basicConfig(filename='log.txt',level=logging.WARNING, filemode='w') # w=overwrite
#logging.basicConfig() # Print logs to console
#logging.basicConfig(format='%(levelname)s') # It prints only level name
#logging.basicConfig(format='%(levelname)s:%(message)s') # It prints levelname and message
logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s') # It prints levelname, name and Message
#print("loging Demo")
logging.critical("This is critical message")
logging.error("This is error message")
logging.warning("This is warning")
#logging.info("This is info")
#logging.debug("This is  debug")
#print("Hello")