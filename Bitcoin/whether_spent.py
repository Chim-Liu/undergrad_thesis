import os
L = open ("Hash_library.txt", 'r')
S = open ("spent_output_hash.txt", 'r')
dict = {}
line = L.readline()
while line :
    dict[line[0:64]] = line[65:].strip()
    line=L.readline()

line =S.readline()
while line :
    line = line.strip()
    if line.strip() in dict.keys():
        dict[line] = int(dict[line]) - 1
    line=S.readline()

T = open("test3.txt",'w')
for key in dict.keys():
    if int(dict[key]) > 0:
        T.write(key+'\n')
T.close()
L.close()
S.close()