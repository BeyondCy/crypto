#coding:utf-8
"""
author:xnianq
date:2017/03/04
"""

def Create():
    count =0
    for i in range(0,26):
        for j in range(0,26):
            for x in range(0,26):
                for z in range(0,26):
                    if((i*z-x*j)%26)==1:
                         if(z%26==i%26 and (26-j)%26==j%26 and (26-x)%26==x%26):
                            count = count + 1
                            print "第"+str(count)+"组key为："+str(i),str(j),str(x),str(z)
                    if ((i*z-x*j+26)%26) == 25:
                        if ((-z)%26 == (i)%26 ):
                            count = count + 1
                            print "第" + str(count) + "组key为：" + str(i), str(j), str(x), str(z)
if __name__ == '__main__':
    Create()
