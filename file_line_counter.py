'''
File line counter
Write a function that takes a file path, opens it, and returns the number of lines in it. If the file doesn't exist, return -1 instead of crashing.
'''

import os

def countingLines(file_path):
    if os.path.exists(file_path):
        with open(file_path) as f1:
            lines = f1.readlines()
            return(len(lines))
    else:
        return(-1)

file_path = input("Enter a file path: ")
print(countingLines(file_path))