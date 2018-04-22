
#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/9 上午11:24

class Solution:
    def strStr(self,source,target):
        if source is None or target is None:
            return -1

        cur,index =0,0
        s_len=len(source)
        t_len=len(target)

        while cur <= s_len-t_len:
            temp = cur

            #匹配目标字符的每一位
            while index != t_len:
                if target[index] != source[cur]:
                    break
                else:
                    index += 1
                    cur += 1
            #匹配成功
            if index == t_len:
                return cur-t_len

            #如果没有匹配成功
            cur = temp + 1

            index = 0

        return -1
