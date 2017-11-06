#!/bin/bash/python
## Opening a file in python for reading is easy
file = open('/home/ec2-user/python/loops.py', 'r')
## to get everything in the file just use read()

text = file.read()
# print the file content
print (text)
#close hte statement
file.close()



import os
os.system('echo "this will help to runn linux commands"')
