#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/6 下午5:37

def isDeformation(str1,str2):
    if str1 == None or str2 == None or len(str1) != len(str2):
        return False
    map = [0]*256                         #创建一个长度为256的三个数组
    str1_toArray = list(str1)
    str2_toArray = list(str2)
    for i in range(len(str1_toArray)):
        char1_ord = ord(str1_toArray[i])  #获取当前字符的对应编码
        map[char1_ord] += 1

    for j in range(len(str2_toArray)):
        char2_ord = ord(str2_toArray[j])
        map[char2_ord] -= 1


    for k in range(len(map)):
        if map[k] != 0:
            return False

    return True

print(isDeformation('1234','321'))
