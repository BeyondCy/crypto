#coding:utf-8
import os,random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
modes = {'1':2,'2':3,'3':6,'4':1,'5':5,'6':4}

def encrypt(key,filename,mode):
    chunksize = 64*1024
    outFile = "AESEn"+filename
    filesize = str(os.path.getsize(filename)).zfill(16) #返回16
    IV = ''

    for i in range(16):
        IV = IV + chr(random.randint(0,0xff))

    encryptor = AES.new(key,AES.MODE_CBC,IV)

    with open(filename,'rb') as infile:
        with open(outFile,'wb') as outfile:
            outfile.write(filesize)
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) ==0:
                    break
                elif len(chunk)%16 !=0:
                    chunk = chunk + (16-len(chunk)%16)*' '
                print "DOne"
                outfile.write(encryptor.encrypt(chunk))


def decrypt(key,filename,mode):
    chunksize = 64*1024
    outfile = "De"+filename
    with open(filename) as infile:
        with open(outfile,"wb") as outfile:
            filesize = long(infile.read(16))
            IV  = infile.read(16)

            decryptor = AES.new(key,mode,IV)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

def getkey(password):
    key = SHA256.new(password)
    return key.digest()



def main():
    choice = raw_input("加密请输入：1,解密请输入：2")
    password = raw_input("请输入您的密钥：")
    mode = raw_input("加密模式：[1]CBC,[2]CFB,[3]CTR,[4]ECB,[5]OFB,[6]PGP")
    mode = modes[mode]
    key = getkey(password)
    if choice == '1':
        file = raw_input("请输入要加密文件的绝对路径:")
        encrypt(key,file,mode)
    if choice =='2':
        file = raw_input("请输入要解密文件的绝对路径：")
        decrypt(key,file,mode)

if __name__ == '__main__':
    main()
