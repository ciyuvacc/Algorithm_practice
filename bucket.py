#!/bin/python 
#encoding:utf8
#桶算法
#python bucket.py  1 2 9 2  4  2 3 3 8 10

from sys import argv

list1 = argv[1:] #获取输出的值
lens = len(list1)#计算输入值的个数

#init 
#初始化定义字典初始值为0
list2 = {}
for i in range(11):
    list2[i] = 0

#记录输入值对应key的个数(value值)
for i in range(lens):
    nub = int(list1[i])
    list2[nub] += 1

#遍历value值大于1的输出到屏幕排序完成 
for i,j in list2.items():
    if j>=1:
        for y in range(j):
            print i
 
