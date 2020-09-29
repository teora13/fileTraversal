# file traversal searching for specific name or extension in directory

import os

path = 'C:\\Users\\anmen\\Documents\\My Games'
name = 'config'

def travFile(path, name, level = 1):
    for file in os.listdir(path):
        # if there are some others dirs in folder
        if os.path.isdir(path+'\\'+file):
            travFile(path+'\\'+file, name, level+1)
        if file.find(name) != -1:
            print(path+'\\'+file)

travFile(path,name)
