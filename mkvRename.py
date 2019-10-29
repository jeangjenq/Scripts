'''
Created on 12 March 2019
Usage: Batch rename MKV title to filename with the help of mkvpropedit
'''

import os
from subprocess import call

#Create a list of all files in a folder of choice, change folder in os.walk('./')
allFiles = [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk('/mnt/Archive/Video/Movies/')] for val in sublist]

for file in allFiles:
    #Get file name without extension to use as title
    name = os.path.splitext(os.path.basename(file))
    #isolate out mkv files only
    if name[1] not in ['.mkv', '.MKV']:
        pass
    else:
        title = 'title=' + name[0]
        call(["mkvpropedit", file, "-e", "info", "-s", title])