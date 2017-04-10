"""
author:xnianq
date:2017/03/05
"""
#coding:utf-8
#MYAMRARUYIQTENCTORAHROYWDSOYEOUARRGDERNOGW
# Str = "MYAMRARUYIQTENCTORAHROYWDSOYEOUARRGDERNOGW"
# Str = "MYAMRARUYIQTENCTORAHROYWDSOYEOUARRGDERNOGW"
def Getmn(Str):
    for i in range(2,len(Str)):
        if len(Str)%i ==0:
            print i,len(Str)/i
            Decrypt(Str,i,len(Str)/i)

def Decrypt(s,m,n):
    cipher = ""
    for x in range(0,m):
        for y in range(0,n):
            cipher = cipher + s[x+y*m]
    print cipher.lower()

def Encrypt(s,m,n):
    mw = ""
    for i in range(0,n):
        for j in range(0,m):
            mw = mw + s[i+j*n]
    print mw
if __name__=='__main__':
    Sr = "mreadueyunhsaraycrornmitoyrorqoyeggatrwodw"
    #Getmn("MYAMRARUYIQTENCTORAHROYWDSOYEOUARRGDERNOGW")
    for x in range(0,7):
        l = ""
        for y in range(0,len(Sr)):
            if((y-x)%7==0):
              l = l + Sr[y]
        Getmn(l)   # Encrypt("marryqecoarydoeurgengymauitntrhowsyoardrow".upper(),2,21)
