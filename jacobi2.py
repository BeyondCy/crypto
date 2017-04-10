#coding:utf-8
"""
author:xnianq
date:2017/04/05
"""

def pro1(a,b):
    a = a%b
    return a,b

def pro2(a,b):
    if b%8==1 or b%8 == 7:
        return 1
    if b%8==3 or b%8 == 5:
        return -1

def pro3(a,b):
    i = 0
    while 1:
        if a%2 ==0:
            a = a/2
            i = i+1
        else:
            break
    return a,i

def pro4(a,b):
    if a%4==3 and b%4==3:
        return False
    else:
        return True

def Jacobi(a,b):
    f = 1
    while 1 :
        if a==1:
            break
        elif(a>b):
            a,b = pro1(a,b)
            a,i = pro3(a,b)
            f = f*pow(pro2(2,b),i)
        elif (a<b):
            if pro4(a,b):
                a,b = b,a
                a,b = pro1(a,b)
                a,i = pro3(a,b)
                f = f*pow(pro2(2,b),i)
            else:
                a,b = b,a
                f = f*-1
                a,b = pro1(a,b)
                a,i =pro3(a,b)
                f = f*pow(pro2(2,b),i)
    return f
if __name__ == '__main__':
    print Jacobi(20964,1987)

