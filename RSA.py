#coding:utf-8
"""
author:xnianq
date:2017/04/05
"""
from math import sqrt
from Miller_Rabin import *


def GetChr(num):
    last = num%pow(26,2)%26
    medium = (num-last)%pow(26,2)/26
    first = (num-last-medium*26)/pow(26,2)
    return chr(ord('A')+first)+chr(ord('A')+medium)+chr(ord('A')+last)

def GetNum(cipher):
    #print cipher
    num = 0
    num = num+(ord(cipher[0])-ord('A'))*pow(26,2)
    num = num + (ord(cipher[1])-ord('A'))*26
    num = num+ord(cipher[2])-ord('A')
    return num


def gcd(a,b):#欧几里徳求最大公约数
    if b ==0:
        return a
    else:
        return gcd(b,a%b)

def ex_gcd(a,b,x,y):#欧几里徳拓展算法求逆元
    if b==0:
        return a,1,0
    r,t,y = ex_gcd(b,a%b,x,y)
    x,y = y,t-a/b*y
    return r,x,y



def Getpq(n):#破解n时需要调用
    for i in range(2,int(sqrt(n))):
        if n%i ==0:
            return i,n/i

def Getfy(n):#求fy,破解时调用.
    p,q = Getpq(n);
    fy = (p-1)*(q-1)
    return fy

def Geta(b,fy):#取逆元
    return  (ex_gcd(b,fy,1,0)[1]+fy)%fy


def Encrypt(plaintext,b,n):
    cipher = quickPowMod(plaintext,b,n)
    return cipher
def Decrypt(m,a,n):
    plaintext = quickPowMod(m,a,n)
    return plaintext


def Getcipher():
    f = open('cipher.txt','r')
    cipher = []
    text = f.read()
    text = text.replace("\n","").split(" ")
    for i in range(0,len(text)):
        cipher.append(int(text[i]))
    return cipher


if __name__ == '__main__':
    # cipher = Getcipher()
    # plaintext = ""
    # fy = Getfy(18923)
    # a = Geta(1261,fy)
    # for i in range(0,len(cipher)):
    #     plaintext = plaintext + GetChr(Decrypt(cipher[i],a,18923))
    # print plaintext
    p = getBigPrime(random.randrange(10,30,2)**random.randint(150,160) + 1)#生成大素数
    q = getBigPrime(random.randrange(10,30,2)**random.randint(150,160) + 1)
    n = p*q
    fy = (p-1)*(q-1)
    b = random.randrange(100,1000,2)+1#一定是奇数
    while 1:
        if gcd(fy,b)==1:
            break
        b = b+2
    a = Geta(b,fy)
    print "欢迎使用xnianq'RSA加密解密，您的公钥是:b ="+str(b)+",\nn="+str(n)+"，\n私钥是：a ="+str(a)+",\np:"+str(p)+",\nq:"+str(q)+".\n"
    cipher = raw_input("请输入要加密的密文")
    shengyu = 3-len(cipher)%3
    if len(cipher)%3!=0:
        cipher = cipher+"A"*(3-len(cipher)%3)
    plaintext = []
    Ci  = []
    for i in range(0,len(cipher),3):
        plaintext.append(GetNum(cipher[i:i+3]))
    print plaintext
    mingwen = ""
    for i in range(0,len(plaintext)):
        mingwen = mingwen+str(plaintext[i])
    print "您输入的字符串转换成数字为："+mingwen

    miwen = ""
    for i in range(0,len(plaintext)):
        Ci.append(Encrypt(plaintext[i],b,n))
        miwen = miwen + str(Encrypt(plaintext[i],b,n))
    for i in range(0,len(Ci)):
        print Ci[i]
    print "您加密的密文为："+miwen


    Pl = []

    for i in range(0,len(Ci)):
        Pl.append(Decrypt(Ci[i],a,n))



    mingwen = ""
    for i in range(0,len(Pl)):
        mingwen = mingwen+ GetChr(Pl[i])
        #mingwen = mingwen+str(Pl[i])
    ##print en
    print "您解密出的密文为:" +mingwen[:-1*shengyu]
    #print de