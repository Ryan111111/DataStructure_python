#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/22 下午3:56

#输入两个字符，从第一个字符中删除第二字符中所有的字符
#思路：匹配第二个字符然后替换称空即可


#注意牛客网的输入输出，保证程序代码对的前提下，正确CV
#python3.5中，没有raw_input()函数，只有input()

input_1 = input()
input_2 = input()
input_2 = set(input_2)
for en_char in input_2:
    input_1 = input_1.replace(en_char,"")
print(input_1)