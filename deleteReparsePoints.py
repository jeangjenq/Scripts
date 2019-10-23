'''
Created by Jeang Jenq Loh

Delete reparse points on every files/directories/subdirectories in the selected folder
Created for Windows 10 Onedrive reparse points issue
'''

import os
from subprocess import call

#gather a list of files/directories/subdirectories
list = []
for root, directories, filenames in os.environ['OneDrive']:
    for directory in directories:
        list.append(os.path.join(root, directory))
    for filename in filenames:
        list.append(os.path.join(root, filename))

#run 'fsutil reparsepoint delete #filename' for every thing in the list
for file in list:
    call(["fsutil", "reparsepoint", "delete", file])