#!/usr/bin/env python3
import boto3
import sys
firstParam = sys.argv[1]
def number_to_string():
    match firstParam:
        case iam:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
number_to_string()