#coding:utf-8
sushu  = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
def Gettwo(a,p):
    t = pow(a,(p-1)/2)
    if t%p ==0:
        return 0
    elif t%p ==1:
        return 1
    else :
        return -1
def Getsim(a):
    s = []
    for i in sushu:
        while(1):
            if a%i==0:
                s.append(i)
                a = a/i
            else:
                break
    return s

def Jacbi(a,b):
    list = Getsim(b)
    final = 1
    for i in list:
        final = final*Gettwo(a,i)
    return final


if __name__ == '__main__':
        print Jacbi(20964,1987)