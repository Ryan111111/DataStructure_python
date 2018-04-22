#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/12 下午1:10

#寻找最长一个光滑数列，元素大小差距不能大于1

import collections
class Solution:
    def findHS(self,nums):
        dic = dict(collections.Counter(nums))
        print(dic)


ss = Solution()
ss.findHS([1,3,2,2,5,2,3,7])



