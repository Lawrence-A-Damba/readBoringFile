import os
import fnmatch
boringFileNames = []
outPut=open('OutPut','w')

listOfFiles = os.listdir('.')
pattern = "*.TXT"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        boringFileNames.append(entry)
#print('#', boringFileNames)
for boringName in boringFileNames:
    open_file = open(boringName, 'r')
    file = open_file.readlines()
    for item in range(8,((len(file))-8)):
        print(file[item])

#        print(file[14])


        item1=file[item][0:5]
        print('Top ', item1, file = outPut)


        item2=file[item][5:10]
        print('Bottom ', item2, file = outPut)


        item3=file[item][10:13]
        print('Water ', item3, file = outPut)


        item4=file[item][13:18]
        print('Strata ', item4, file = outPut)


        item5=file[item][18:25]
        print('Log ',item5, file = outPut)


        item6=file[item][25:28]
        print('Cons. ', item6, file = outPut)


        item7=file[item][28:37]
        print('Color ', item7, file = outPut)


        item8=file[item][37:51]
        print('Syb ', item8, file = outPut)


        item9=file[item][51:55]
        print('Res. ', item9, file = outPut)


        item10=file[item][55:59]
        print('UCT ', item10, file = outPut)


        item11=file[item][59:62]
        print('Density ', item11, file = outPut)


        item12=file[item][62:65]
        print('LL ', item12, file = outPut)


        item13=file[item][65:68]
        print('PL ', item13, file = outPut)


        item14=file[item][68:73]
        print('D-10 ', item14, file = outPut)


        item15=file[item][73:76]
        print('Water ', item15, file = outPut)


        item16=file[item][76:80]
        print('UCT ', item16, file = outPut)


        item17=file[item][80:85]
        print('ORG% ', item17, file = outPut)


        item18=file[item][85:90]
        print('Materiall ', item18, file = outPut)

open_file.close()
'''
outPut.close()

text=str(file[14])
text=text.split()
print(text)
for item in text:
    if item == '':
        text.remove('')
    else:
        pass
print(text)
'''

