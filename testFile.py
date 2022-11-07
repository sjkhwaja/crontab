import os 
import sys
import time

# get current working directory
cwd = os.getcwd()

# print cwd
print(cwd)

# get the current time
now = time.time()

# save current time as a string
start_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/testFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(data))
