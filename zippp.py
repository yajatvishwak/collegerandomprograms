# Python script to Open a zipfile and read its content
# and then make another file with all its content in one file
# Prerequisities : 1. make a zip file named as zipp.zip or change the filename 
# in code manually
# 2. the zip file can contain whatever files, the scropt will extract and read its content
# 3. the final content of zip file will b written in a txt file called 'final.txt'
# 4. A cup of coffee for making me do this will be appretiated eshan... 
# Written on : 15th Nov, 2019
# Modified: 18th Nov, 2019 - added Showing only redundant data
from zipfile import ZipFile
filename ='zipp.zip'
with ZipFile(filename, 'r') as zip:
    zip.printdir()
    data = zip.namelist()
    print('Extracting all files')
    zip.extractall()
    print('done.. now reading each file....')
con = []
for fil in data:
    with open(fil,'r') as f:
        ele = f.read()
        con.append(ele)
con2 = [] # for cleaning and data processing 
for ele in con:
    for element in ele.split('\n'):
        con2.append(element)
d = {x:con2.count(x) for x in con2} # take the frequency of all the names
final =[]
for key, value in d.items():
    if(value == len(data)): # print those names whose frequency is whatever the number of files present in zip
        final.append(key)

with open('final.txt', 'w') as f:
    for i in final: 
        print(i)
        f.write(i+' ')  
print('done')
