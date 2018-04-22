#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/8 下午12:55

class Solution:
    def removeElements(self,head,val):
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        pre = dummy

        while cur:
            if cur.data == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next