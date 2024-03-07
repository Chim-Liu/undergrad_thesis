import os

dir = './result/'

fList = os.listdir(dir)
fList.sort()
H = open("spent_output_hash.txt", 'w')
for i in fList:
    f = open(dir + i, 'r')
    line = f.readline()
    while line :
#       if (line.startswith('Outputs count')):
#            count = line.lstrip("Outputs count =")
#            temp_line = temp_line + count
        if (line.startswith('TX from hash')):
            line = line.lstrip("TX from hash = ")
            H.write(line)
        line = f.readline()
f.close()
H.close()