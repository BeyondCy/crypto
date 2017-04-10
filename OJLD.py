#coding:utf-8
from sympy import *
def Ojld(b,n):
    list = []
    while 1:
        if b%n ==0:
            list.append(b)
            break
        else:
            list.append(b/n)
            t = b
            b = n
            n = t%n
    return list

def Wiener(b,n):
    list = Ojld(b,n)
    c = []
    #print list
    c.append(1)
    c.append(list[0])
    d = []
    d.append(0)
    d.append(1)
    for j in range(1,len(list)):
        f = list[j]*c[j]+c[j-1]
        g = list[j]*d[j]+d[j-1]
        #print g,b,f
        c.append(f)
        d.append(g)
        if (g*b-1)%f ==0:
            n1 = (g*b-1)/f
            x = symbols("x")
            solves =  solve(Eq(x**2-(n-n1+1)*x+n,0),x)
            if int(solves[1])==solves[1]:
                return n1,solves[0],solves[1]
if __name__ == '__main__':
    print Wiener(77537081,317940011)