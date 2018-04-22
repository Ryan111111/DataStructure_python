#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/9 下午12:49
class Solution:
    def combinationSum(self,candidates,target):
        candidates.sort()
        path,result = [],[]
        begin = 0
        self.helper(begin,candidates,target,path,result)
        return result

    def helper(self,begin,candidatas,target,path,result):
        #剪枝
        if sum(path) > target:
            return

        #满足条件：先复制，再将复制的结果加入结果列表
        if sum(path) == target:
            temp  = path[:]
            result.append(temp)
            return

        for i in candidatas[begin:]:
            path.append(i)
            #带着半成品path继续探索，往这个半成品中添加元素，看能否成功
            self.helper(begin,candidatas,target,path,result)
            #返回上一层，自然要把这一层添加的值删除
            path.pop(-1)

            begin += 1

ss = Solution()
print(ss.combinationSum([2,3,6,7],7))
