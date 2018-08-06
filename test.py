import os
boringFileNames = []
listOfFiles = os.listdir('.')
newList = []

for names in listOfFiles:
    if names.endswith(".txt"):
       newList.append(names)
    if names.endswith(".TXT"):
       newList.append(names)   
for boringName in newList:
    print('\n\n\nThis is the boring name, ', boringName, '\n\n\n')
    open_file = open(boringName, 'r')
    file = open_file.readlines()
    print(file)
#junk remove this comment.
open_file.close()
