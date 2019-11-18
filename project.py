from zipfile import ZipFile
filename ='namelists.zip'
with ZipFile(filename, 'r') as zip:
    zip.printdir()
    data = zip.namelist()
    print('Extracting all files')
    zip.extractall()
    print('done.. now reading each file....')
con = []
for fil in data:
    with open(fil,'r') as f:
            ele = f.read().strip('\n')
            con.append(ele)
con = list(set(con))
with open('final.txt', 'w') as f:
    for i in con: 
        f.write(i+' ')
        print(i)
print('done')
