#coding:utf-8
"""
author:xnianq
"""

def initsbox(key):
    sbox = range(256)
    j = 0
    for i in range(0,256):
        j = (j+sbox[i]+ord(key[i%len(key)]))%256
        sbox[i],sbox[j] = sbox[j],sbox[i]
    return sbox

def initkey(key,data):
    i = 0
    j = 0
    k = []
    for x in range(0,len(data)):
        i = (i+1)%256
        j = (j+key[i])%256
        key[i],key[j] = key[j],key[i]
        k.append(key[(key[i]+key[j])%256])
    return k

def encrypt(text,key):
    c = []
    for i in range(0,len(text)):
        c.append(chr(ord(text[i])^key[i]))
    return ''.join(c)


def readfile(file):
    a = open(file, 'r')
    try:
        content = a.read()
    finally:
        a.close()
    return content
def writefile(file,text):
    f = open(file,'w')
    try:
        f.write(text)
    finally:
        f.close()

def main():
    key  = raw_input("请输入密钥：")
    ty = raw_input("请输入要加密的类型,文字：[1],文件:[2]")
    if ty == '1':
        data = raw_input("请输入要加密的文字")
    elif ty =='2' :
        filename = raw_input("请输入要加密的文件(绝对路径)")
        data = readfile(filename)
    sbox = initsbox(key)
    pay = initkey(sbox,data=data)
    cipher = encrypt(data,pay)
    if ty == '1':
        print "密文为："+cipher
    if ty == '2':
         writefile(file="RC4en"+filename,text=cipher)
         print "文件已经加密，请查看:"+"RC4en"+filename
if __name__ == '__main__':
    main()