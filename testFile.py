import os 
import sys
import time

# get current working directory
cwd = os.getcwd()

# print cwd
print(cwd)

# create new dictionary
covidData = pd.read_json('https://healthdata.gov/resource/8uup-3f6m.json')
covidData

# save to csv file
covidData.to_csv('data/covidData.csv, index=None')

# get the current time
now = time.time()

# save current time as a string
start_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/home/saira/crontab/testFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(covidData))
