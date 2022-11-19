#!/usr/bin/env python3
import logging
import os
import socket
import pytest

try:
    a = "Rama"
    myHost = socket.gethostname()
    assert myHost == "minikube01.nirulabs.com"
    print(a)
except NameError as msg:
    logging.critical("This is critical message")
    print("Entering to exception!")
    print(msg)
finally: 
    print("Finally")