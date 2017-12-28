#!/bin/python
#encoding:utf8
#冒泡排序 
list1=[1,23,423,11111,123,523,123,1234,]
lens = len(list1)

for j in range(lens-1):
    for i in range(lens-1-j):
        if list1[i]<list1[i+1]:
            list1[i],list1[i+1] = list1[i+1],list1[i]
print list1


#双重嵌套循环   
#时间复杂度O(N*N)  高
