# Python script to Open a zipfile and read its content
# and then make another file with all its content in one file
# Prerequisities : 1. make a zip file named as zipp.zip or change the filename 
# in code manually
# 2. the zip file can contain whatever files, the scropt will extract and read its content
# 3. the final content of zip file will b written in a txt file called 'final.txt'
# 4. A cup of coffee for making me do this will be appreciated eshan... 
# Written on : 15th Nov, 2019

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
            con.append(f.read())
with open('final.txt', 'w') as f:
    for i in con: 
        f.write(i+' ')
print('done')
