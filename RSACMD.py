#coding:utf-8
"""
author:xnianq
date:2017/04/05
"""

def Decrypt(n,b1,b2,y1,y2):
    c1 = Getre(b1,b2)
    c2 = (c1*b1-1)/b2
    x1 = (pow(y1,c1)*Getre(pow(y2,c2),n))%n
    return x1


def Getre(b,n):
    for i in range(2,n):
        if (b*i)%n==1:
            return i

if __name__ == '__main__':
    print Decrypt(18721,43,7717,12677,14702)