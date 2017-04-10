#coding:utf-8
import  math
import struct
import hashlib

A=0x67452301
B=0xefcdab89
C=0x98badcfe
D=0x10325476
T =  tuple(int(4294967296*abs(math.sin(x))) for x in range(65))

def F(x,y,z):
    return (x&y)|((~x)&z)

def G(x,y,z):
    return (x&z)|(y&(~z))

def H(x,y,z):
    return x^y^z

def I(x,y,z):
    return y^(x|(~z))

def FF(a,b,c,d,Mj,s,ti):
    a = b+XHYW(s,(a+(F(b,c,d)+Mj+ti))&0xffffffff)
    return a&0xffffffff

def GG(a,b,c,d,Mj,s,ti):
    a = b+XHYW(s,(a+G(b,c,d)+Mj+ti))
    return a&0xffffffff

def HH(a,b,c,d,Mj,s,ti):
    a = b+XHYW(s,(a+H(b,c,d)+Mj+ti))
    return a&0xffffffff

def II(a,b,c,d,Mj,s,ti):
    a = b+XHYW(s,(a+I(b,c,d)+Mj+ti))
    return a&0xffffffff


def XHYW(n,m):#循环移位
    #print bin(m)
    #print ((m<<n)&0xffffffff)|((m&0xffffffff)>>(32-n))
    return ((m<<n)&0xffffffff)|((m&0xffffffff)>>(32-n))

def extend(s):##小端拓展
    bitlen = len(s)*8
    # 将字符串长度以64位二进制保存
    hexlen1 = hex(bitlen)[2:].zfill(16)
    hexlen = hexlen1.decode('hex')[::-1].encode('hex')##将字符串反转,hex编码
    extlen = [chr(int(hexlen[i:i+2],16)) for i in range(0, 16, 2)]
    mod = bitlen%512
    if(mod>=448):#如果余数大于448,重新添加一组0。
        padding = chr(0x80)+chr(0)*(55-mod/8+64)
    else:
        padding = chr(0x80)+chr(0)*(55-mod/8)
    # for i in range(0,len(s+padding+''.join(extlen))):
    #     print ord((s+padding+''.join(extlen))[i])
    #print ''.join(extlen)
    return s+padding+''.join(extlen)

def Froud(i,s,M):#i=0
    global A,B,C,D,T
    for t in range(0,4):
        #print s[i+1]
        A = FF(A,B,C,D,M[i],s[i%4],T[i+1])
        D = FF(D,A,B,C,M[(i+1)%16],s[(i+1)%4],T[i+2])
        C = FF(C,D,A,B,M[(i+2)%16],s[(i+2)%4],T[i+3])
        B = FF(B,C,D,A,M[(i+3)%16],s[(i+3)%4],T[i+4])
        i = i+4

def Groud(i,j,s,M):#i=16
    global A,B,C,D, T
    for t in range(0,4):
        #print j%16
        A = GG(A,B,C,D,M[(j)%16],s[0],T[i+1])
        D = GG(D,A,B,C,M[(j+5)%16],s[1],T[i+2])
        C = GG(C,D,A,B,M[(j+10)%16],s[2],T[i+3])
        B = GG(B,C,D,A,M[(j+15)%16],s[3],T[i+4])
        i = i+4
        j = j + 20

def Hroud(i,j,s,M):#i=32,j=5
    global A,B,C,D, T
    for t in range(0,4):
        #print (j)%16
        A = HH(A,B,C,D,M[(j)%16],s[0],T[i+1])
        D = HH(D,A,B,C,M[(j+3)%16],s[1],T[i+2])
        C = HH(C,D,A,B,M[(j+6)%16],s[2],T[i+3])
        B = HH(B,C,D,A,M[(j+9)%16],s[3],T[i+4])
        i = i+4
        j = j+12

def Iroud(i,j,s,M):#i=48,j=0
    global A,B,C,D,T
    for t in range(0,4):
        #print (j)%16
        A = II(A,B,C,D,M[(j)%16],s[0],T[i+1])
        D = II(D,A,B,C,M[(j+7)%16],s[1],T[i+2])
        C = II(C,D,A,B,M[(j+14)%16],s[2],T[i+3])
        B = II(B,C,D,A,M[(j+21)%16],s[3],T[i+4])
        i = i+4
        j = j+28

def encrypt(s):
    s = extend(s)
    global A,B,C,D
    #print s.__len__()
    for i in range(0,len(s),64):#每64个字节分一组
        M = []
        AA, BB, CC, DD = A, B, C, D
        for j in range(0,64,4):#再将一组分为16个小组,每一小组4个字节
            #print s[i + j:i + j + 4]
            M.append(struct.unpack("i",s[i+j:i+j+4])[0])
        #print M
        Froud(0,[7,12,17,22],M)
       # print A, B, C, D
        Groud(16,1,[5,9,14,20],M)
        #print A, B, C, D
        Hroud(32,5,[4,11,16,23],M)
        #print A, B, C, D
        Iroud(48,0,[6,10,15,21],M)
        #print A, B, C, D
        A,B,C,D = (A+AA)&0xffffffff,(B+BB)&0xffffffff,(C+CC)&0xffffffff,(D+DD)&0xffffffff
        #print A, B, C, D
        #
    #print hex(A)
    result = ""
    for i  in (A,B,C,D):
        result = result+ hex(i)[2:].zfill(8).decode('hex')[::-1].encode('hex')

    return result
if __name__ == '__main__':
    test1 = raw_input("请输入您要加密的md5值")
    mtest1 = encrypt(test1)
    mtest2 = hashlib.md5(test1).hexdigest()
    print "使用本函数进行加密的值为:"+ mtest1
    print "使用hashlib系统自带的函数加密的值为:"+mtest2
    if(mtest1 == mtest2):
        print test1+"MD5值是:"+mtest1+",验证成功";