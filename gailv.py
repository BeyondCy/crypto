# coding:utf-8
"""
author:xnianq
date:2017/03/01
"""

dict = {'A':0.082,'B':0.015,'C':0.028,'D':0.043,'E':0.127,'F':0.022,'G':0.02,'H':0.061,'I':0.07,'J':0.002,'K':0.008,'L':0.04,'M':0.024,'N':0.067,'O':0.075,'P':0.019,'Q':0.001,'R':0.060,'S':0.063,'T':0.091,'U':0.028,'V':0.010,'W':0.023,'X':0.001,'Y':0.020,'Z':0.001}

def GetStr(s,n):   # 将密文进行分组
    list =[]
    for i in range(0,n):
        list.append('')
    for i in range(0,len(s)):
        list[i%n] = list[i%n]+s[i]
    return list

def GetIc(s):
    p = 0
    for x in range(65,91):
        p = p + float(s.count(chr(x))*(s.count(chr(x))-1)/ float(len(s)*(len(s)-1)))
    return p



def Getkey(n,m):
    key =""
    n1 =len(n)/int(m)
    m =int(m)
    list = GetStr(n,m)
    for z in range(0,list.__len__()):
        list3 = []
        list4 = []
        for y in range(0,26):
            p = 0.0
            for x in range(65, 91):
                p = p + float(list[z].count(chr((x-65+y)%26+65))*dict[chr(x)])/ float(n1)
            list3.append(p)
        for n in range(0,list3.__len__()):
            abslist = abs(list3[n]-0.065)
            list4.append(abslist)
        key = key+chr(list4.index(min(list4))+65)
    return key



def Decrypt(s,key):
    final = ""
    for i in range(0,len(s)):
        if (ord(s[i])-ord(key[i%len(key)]))>=0 :
            final = final + chr(ord(s[i])-ord(key[i%len(key)])+ord("A"))
        else:
            final = final + chr(ord(s[i])-ord(key[i%len(key)])+26+ord("A"))
    return final


if __name__=='__main__':
    s = raw_input("亲，请输入你需要猜解密的字符串：")
    s = s.replace(" ","")
    s = s.upper()
    list3 = []
    for i in range(1,10):
        list2 = []
        ave = 0.0
        list = GetStr(s,i)
        for x in range(0,list.__len__()):
            #print list[x]
            list2.append(GetIc(list[x]))
        for x in range(0,list2.__len__()):
            ave = ave + float(list2[x])
        #print "当m="+str(i)+"时，重合指数(平均)为："+str(float(ave)/list2.__len__())
        list3.append(abs(float(ave)/list2.__len__()-0.065))
    m = list3.index(min(list3))+1
    key = Getkey(s,m)
    print "亲，你的密钥为："+key
    plaintext = Decrypt(s,key)
    print "亲，明文为：\n"+plaintext