# crontab

Assignment 6 HHA 507

# Setting up VM (azure)

## 1 Set up VM with basic settings

2 Connect to VM via terminal 
3 Update VM $ sudo apt-get update
4 Select nano editor $ select-editor
5 $ git clone https://github.com/example
6 Change into file directory

# Crontab
1 $ crontab -e
2 Schedule cron jobs: 
Everday at 9 am $ 0 9 * * * /usr/bin/python3 /users/documents/pythonfile.py > log.txt 2>&1 &
Every Sunday night at 10:00 PM $ 0 2 2 * * SUN /usr/bin/python3 /users/documents/pythonfile.py > log.txt 2>&1 &
Every Quarter $ 0 0 1 * /3 * /usr/bin/python3 /users/documents/pythonfile.py > log.txt 2>&1 &
