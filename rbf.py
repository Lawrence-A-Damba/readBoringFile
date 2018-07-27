import os, fnmatch
boringFileNames = []
listOfFiles = os.listdir('.')
pattern = "*.TXT"
for entry in listOfFiles:
	if fnmatch.fnmatch(entry, pattern):
		boringFileNames.append(entry)
print('#',boringFileNames)
for boringName in boringFileNames:
	open_file=open(boringName,'r')
	file=open_file.readlines()
	print(file)
open_file.close()
