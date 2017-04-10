#coding:utf-8
"""
author:xnianq
date:2017/03/03
"""
from numpy import *

#def Encrypt(plaintext,key):


#def Decrypt(ciphertext,key):


if __name__ == '__main__':
    plaintext = raw_input("亲，请输入要加密的字符串:")
    key = raw_input("亲，请输入你的密钥(以矩阵形式)：\n“例如：[[1,2][3,4]]”\n")
    key = mat(array(eval(key)))
    print key.I*key