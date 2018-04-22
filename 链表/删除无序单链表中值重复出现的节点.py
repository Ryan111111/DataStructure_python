#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/8 下午12:23

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def deleteDuplicates(self,head):
        if head is None:
            return head

        record = set([head.data])
        cur,pre = head.next,head

        while cur:
            if cur.data in record:
                pre.next = cur.next
                cur = cur.next
            else:
                record.add(cur.data)
                pre = pre.next
                cur = cur.next
        return head


