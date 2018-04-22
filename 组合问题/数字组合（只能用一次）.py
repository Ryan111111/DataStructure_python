#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/9 下午1:01

class Solution:
    def combinationSum2(self, candidates, target):
        path = []
        result = []
        begin = 0
        # 先排序，为了后面的去重做准备
        candidates.sort()
        self.helper(candidates, target, begin, path, result)
        return result

    def helper(self, candidates, target, begin, path, result):
        # 符合条件，加入结果列表
        if sum(path) == target:
            result.append(path[:])
            return
        # 剪枝
        if sum(path) > target:
            return

        # 注意此时用while循环，而应避免使用for循环
        n = len(candidates)
        while begin < n:
            path.append(candidates[begin])
            self.helper(candidates, target, begin + 1, path, result)
            path.pop()
            # 因为已经排序，所以可以通过如下的while循环找到下一个不同的元素作为新一轮的开始，防止重复
            while begin < n - 1 and candidates[begin] == candidates[begin + 1]:
                begin += 1
            begin += 1
        # write your code here

ss = Solution()
print(ss.combinationSum2([10,1,6,7,2,1,5],8))