import os
import hashlib

def read_bytes(file,n,byte_order = 'L'):
    data = file.read(n)
    if byte_order == 'L':
        data = data[::-1]
    data = data.hex().upper()
    return data

def read_varint(file):
    b = file.read(1)
    bInt = int(b.hex(),16)
    c = 0
    data = ''
    if bInt < 253:
        c = 1
        data = b.hex().upper()
    if bInt == 253: c = 3
    if bInt == 254: c = 5
    if bInt == 255: c = 9
    for j in range(1,c):
        b = file.read(1)
        b = b.hex().upper()
        data = b + data
    return data

def reverse(input):
    L = len(input)
    if (L % 2) != 0:
        return None
    else:
        Res = ''
        L = L // 2
        for i in range(L):
            T = input[i*2] + input[i*2+1]
            Res = T + Res
            T = ''
        return (Res);

File_path = "blk00003.dat"
L = open("test3.txt", 'r')
line = L.readlines()
m = 0
for i in line:
    line[m] = i.rstrip()
    m = m+1
F = open(File_path, 'rb')
tmpHex = ''
resList = []
fSize = os.path.getsize(File_path)
while F.tell() != fSize:
    tmpHex = read_bytes(F,4)
    resList.append(str(tmpHex))
    tmpHex = read_bytes(F,4)
    resList.append(str(tmpHex))
    tmpPos3 = F.tell()
    tmpHex = read_bytes(F,80)
    resList.append(str(tmpHex))
    tmpHex = read_varint(F)
    txCount = int(tmpHex,16)
    resList.append(str(tmpHex))
    tmpHex = ''; RawTX = ''; tx_hashes = [];Tx_info=''
    for k in range(txCount):
        tmpHex = read_bytes(F,4)
        Tx_info = Tx_info + tmpHex
        RawTX = reverse(tmpHex)
        tmpHex = ''
        Witness = False
        b = F.read(1)
        Tx_info = Tx_info + b.hex().upper()
        tmpB = b.hex().upper()
        bInt = int(b.hex(),16)
        if bInt == 0:
            tmpB = ''
            F.seek(1,1)
            c = 0
            c = F.read(1)
            Tx_info = Tx_info + c.hex().upper()
            bInt = int(c.hex(),16)
            tmpB = c.hex().upper()
            Witness = True
        c = 0
        if bInt < 253:
            c = 1
            tmpHex = hex(bInt)[2:].upper().zfill(2)
            tmpB = ''
        if bInt == 253: c = 3
        if bInt == 254: c = 5
        if bInt == 255: c = 9
        for j in range(1,c):
            b = F.read(1)
            Tx_info = Tx_info + b.hex().upper()
            b = b.hex().upper()
            tmpHex = b + tmpHex
        inCount = int(tmpHex,16)
        
        tmpHex = tmpHex + tmpB
        RawTX = RawTX + reverse(tmpHex)
        for m in range(inCount):
            tmpHex = read_bytes(F,32)
            Tx_info = Tx_info + tmpHex
            RawTX = RawTX + reverse(tmpHex)
            tmpHex = read_bytes(F,4)                
            Tx_info = Tx_info + tmpHex
            RawTX = RawTX + reverse(tmpHex)
            tmpHex = ''
            b = F.read(1)
            Tx_info = Tx_info + b.hex().upper()
            tmpB = b.hex().upper()
            bInt = int(b.hex(),16)
            c = 0
            if bInt < 253:
                c = 1
                tmpHex = b.hex().upper()
                tmpB = ''
            if bInt == 253: c = 3
            if bInt == 254: c = 5
            if bInt == 255: c = 9
            for j in range(1,c):
                b = F.read(1)
                Tx_info = Tx_info + b.hex().upper()
                b = b.hex().upper()
                tmpHex = b + tmpHex
            scriptLength = int(tmpHex,16)
            tmpHex = tmpHex + tmpB
            RawTX = RawTX + reverse(tmpHex)
            tmpHex = read_bytes(F,scriptLength,'B')
            Tx_info = Tx_info + tmpHex
            RawTX = RawTX + tmpHex
            tmpHex = read_bytes(F,4,'B')
            Tx_info = Tx_info + tmpHex
            RawTX = RawTX + tmpHex
            tmpHex = ''
        b = F.read(1)
        Tx_info = Tx_info + b.hex().upper()
        tmpB = b.hex().upper()
        bInt = int(b.hex(),16)
        c = 0
        if bInt < 253:
            c = 1
            tmpHex = b.hex().upper()
            tmpB = ''
        if bInt == 253: c = 3
        if bInt == 254: c = 5
        if bInt == 255: c = 9
        for j in range(1,c):
            b = F.read(1)
            Tx_info = Tx_info + b.hex().upper()
            b = b.hex().upper()
            tmpHex = b + tmpHex
        outputCount = int(tmpHex,16)
        tmpHex = tmpHex + tmpB
        RawTX = RawTX + reverse(tmpHex)
        for m in range(outputCount):
            tmpHex = read_bytes(F,8)
            Tx_info = Tx_info + tmpHex
            Value = tmpHex
            RawTX = RawTX + reverse(tmpHex)
            tmpHex = ''
            b = F.read(1)
            Tx_info = Tx_info + b.hex().upper()
            tmpB = b.hex().upper()
            bInt = int(b.hex(),16)
            c = 0
            if bInt < 253:
                c = 1
                tmpHex = b.hex().upper()
                tmpB = ''
            if bInt == 253: c = 3
            if bInt == 254: c = 5
            if bInt == 255: c = 9
            for j in range(1,c):
                b = F.read(1)
                Tx_info = Tx_info + b.hex().upper()
                b = b.hex().upper()
                tmpHex = b + tmpHex
            scriptLength = int(tmpHex,16)
            tmpHex = tmpHex + tmpB
            RawTX = RawTX + reverse(tmpHex)
            tmpHex = read_bytes(F,scriptLength,'B')
            Tx_info = Tx_info + tmpHex
            RawTX = RawTX + tmpHex
            tmpHex = ''
        if Witness == True:
            for m in range(inCount):
                tmpHex = read_varint(F)
                Tx_info = Tx_info + tmpHex
                WitnessLength = int(tmpHex,16)
                for j in range(WitnessLength):
                    tmpHex = read_varint(F)
                    Tx_info = Tx_info + tmpHex
                    WitnessItemLength = int(tmpHex,16)
                    tmpHex = read_bytes(F,WitnessItemLength)
                    Tx_info = Tx_info + tmpHex
                    tmpHex = ''
        Witness = False
        tmpHex = read_bytes(F,4)
        Tx_info = Tx_info + tmpHex
        RawTX = RawTX + reverse(tmpHex)
        tmpHex = RawTX
        tmpHex = bytes.fromhex(tmpHex)
        tmpHex = hashlib.new('sha256', tmpHex).digest()
        tmpHex = hashlib.new('sha256', tmpHex).digest()
        tmpHex = tmpHex[::-1]
        tmpHex = tmpHex.hex().upper()
        if tmpHex in line:
            resList.append(Tx_info)
        else:
            Tx_info = ''
        resList.append(''); tmpHex = ''; RawTX = '';Tx_info = '';
C = open("compressd_tx.txt",'w')
for j in resList:
    C.write(j+'\n')
C.close()
F.close()