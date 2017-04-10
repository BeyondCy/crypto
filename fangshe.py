#coding:utf-8

str = "KQEREJEBCPPCJCRKIEACUZBKRVPKRBCIBQCARBJCVFCUPKRIOFKPACUZQEPBKRXPEIIEABDKPBCPFCDCCAFIEABDKP BCPFEQPKAZBKRHAIBKAPCCIBURCCDKDCCJCIDFUIXPAFF ERBICZDFKABICBBENEFCUPJCVKABPCYDCCDPKBCOCPERKIVKSCPICBRKIJPKABI"

list = []
for i in range(ord('A'),ord('Z')+1):
    list.append(str.count(chr(i)))
print list
print list.index(max(list))
print list
print list.index(max(list))
#list.pop(1)
print list.indx(max(list))