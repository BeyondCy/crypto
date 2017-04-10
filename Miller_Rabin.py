#coding:utf-8
import random

def Miller_Rabin(n):
    r, d = 0, n - 1
    while d & 1 == 0:
        r += 1
        d >>= 1

    for k in range(5):
        a = random.randint(2, n - 2)
        x = quickPowMod(a, d, n)
        if x == 1 or x + 1 == n:
            continue
        for i in range(r - 1):
            x = x * x % n
            if x == 1:
                return False
            if x + 1 == n:
                break

        if x + 1 != n:
            return False

    return True

##快速幂取模 pow(a,b) mod c = pow((a mod c),b) moc c
def quickPowMod(a, n, m):
  ans = 1
  while n:
    if n & 1:
      ans = ans * a % m
    a = a * a % m
    n >>= 1
  return ans # a^n %
# 米勒-罗宾算法求大质数

def getBigPrime(n):
    while 1:
        if Miller_Rabin(n):
            return n
        n = n+2

