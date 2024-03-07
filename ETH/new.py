import os
import hashlib
def Md5(data):
    mmd5 = hashlib.md5()
    mmd5.update(data.encode('utf-8'))
    return mmd5.hexdigest()
Rollup = open('Rollup.txt','r')
line = Rollup.readline()
Users = {}
count = 0
while line:
    start = line.find("from")
    end = line.rfind("\"gas\"")
    From_address = line[start+7:end-2]
    start = line.find("to")
    end = line.rfind("transactionIndex")
    To_address = line[start+5:end-3]
#初始化：
    if From_address not in Users.keys():
        Users[From_address] = 10000000000000000000
    if To_address not in Users.keys():
        Users[To_address] = 10000000000000000000
###############
    start = line.find("value")
    end = line.rfind("type")
    Value = line[start+8:end-3]
    Users[From_address] = Users[From_address]-int(Value,16)
    Users[To_address] = Users[To_address] + int(Value,16)
############### Mapfinished 
    line = Rollup.readline()

User_list = []



for i in Users:
    S = str(i)
    S = S +':'+str(Users[i])
    User_list.append(S)

#A = open('User.txt','w')
#for i in User_list:
#    A.write(i)
#A.close()
############## List
if len(User_list)%2 != 0:
    User_list.append(User_list[len(User_list)-1])
for i in range(len(User_list)):
    User_list[i] = Md5(User_list[i])+' '
print(len(User_list))
#D = open('User_hash.txt','w')
#for i in User_list:
#    D.write(i)
#D.close()
#Merkle_root = ""
#while Merkle_root == "":
#    temp_list = []
#    temp_str = ""
#    if len(User_list)%2 != 0:
#        User_list.append(User_list[len(User_list)-1])
#    i = 0
#    while i  < len(User_list):
#        temp_str = User_list[i]+User_list[i+1]
#        temp_list.append(sha256(temp_str))
#        i = i+2
#    User_list = temp_list
#    if (len(User_list)==1):
#        Merkle_root = User_list[0]
#    else:
#        continue
#print(Merkle_root)