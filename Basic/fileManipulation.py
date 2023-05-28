#!/usr/bin/python

def storeFile(file):
    f = open(file, 'r')
    contents = f.read()
    f.close()
    return contents

# Variable to store the filename
fileVar = "notes.txt"

contents = storeFile(fileVar)
print(contents)