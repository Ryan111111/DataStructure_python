#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/18 下午2:10

def sortedDictValue3(dict1):
    keys = dict1.keys()
    keys.sort()
    return map(dict1.get,keys)

