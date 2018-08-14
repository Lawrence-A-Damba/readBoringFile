import os
import fnmatch
boringFileNames = []
OutPut=open('OutPut','w')
listOfFiles = os.listdir('.')
pattern = "*.txt"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        boringFileNames.append(entry)
for boringName in boringFileNames:
    open_file = open(boringName, 'r')
    file = open_file.readlines()
    print(boringName, file=OutPut)
    print('Gnd Elev. = ', file[7][10:16], file=OutPut)
    for item in range(8,((len(file))-8)):
        if file[item][0:5]=='999.9':
            pass
        elif file[item][0:5]=='*****':
            pass
        elif file[item][0]=='S':
            pass
        elif file[item][0]=='T':
            pass
        elif file[item][0]=='D':
            pass
        elif file[item][0]=='L':
            pass
        elif file[item][0]=='C':
            pass
        else:
            item1=file[item][0:5]
            item2=file[item][5:10]
            item3=file[item][10:13]
            item4=file[item][13:18]
            item5=file[item][18:25]
            item6=file[item][25:28]
            item7=file[item][28:37]
            item8=file[item][37:51]
            item9=file[item][51:55]
            item10=file[item][55:59]
            item11=file[item][59:62]
            item12=file[item][62:65]
            item13=file[item][65:68]
            item14=file[item][68:73]
            item15=file[item][73:76]
            item16=file[item][76:80]
            item17=file[item][80:85]
            item18=file[item][85:90]
            if item14 == '':
                pass
            elif item14 == '     ':
                pass
            else:
                print((float(item1) + float(item2))/2, item14, file=OutPut)
open_file.close()
