import os
import fnmatch
boringFileNames = []
OutPut=open('OutPut','w')

listOfFiles = os.listdir('.')
pattern = "*.txt"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        boringFileNames.append(entry)
#print('#', boringFileNames)
for boringName in boringFileNames:
    open_file = open(boringName, 'r')
    file = open_file.readlines()
    for item in range(8,((len(file))-8)):
#        print(file[item])

#        print(file[14])


        item1=file[item][0:5]
#        print('Top ', item1, file = OutPut)


        item2=file[item][5:10]
#        print('Bottom ', item2, file = OutPut)


        item3=file[item][10:13]
#        print('Water ', item3, file = OutPut)


        item4=file[item][13:18]
#        print('Strata ', item4, file = OutPut)


        item5=file[item][18:25]
#        print('Log ',item5, file = OutPut)


        item6=file[item][25:28]
#        print('Cons. ', item6, file = OutPut)


        item7=file[item][28:37]
#        print('Color ', item7, file = OutPut)


        item8=file[item][37:51]
#        print('Syb ', item8, file = OutPut)


        item9=file[item][51:55]
#        print('Res. ', item9, file = OutPut)


        item10=file[item][55:59]
#        print('UCT ', item10, file = OutPut)


        item11=file[item][59:62]
#        print('Density ', item11, file = OutPut)


        item12=file[item][62:65]
#        print('LL ', item12, file = OutPut)


        item13=file[item][65:68]
#        print('PL ', item13, file = OutPut)


        item14=file[item][68:73]
#        print('D-10 ', item14, file = OutPut)


        item15=file[item][73:76]
#        print('Water ', item15, file = OutPut)


        item16=file[item][76:80]
#        print('UCT ', item16, file = OutPut)


        item17=file[item][80:85]
#        print('ORG% ', item17, file = OutPut)


        item18=file[item][85:90]
#        print('Materiall ', item18, file = OutPutl)
#        print(item1, item2, item3, item4, item5, item6,
#                item7, item8, item9, item10, item11,
#                 item12, item13, item14, item15, item16,
#                 item17, item18, file=OutPut)

        
        print(item1, item2, item14, file=OutPut)
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

