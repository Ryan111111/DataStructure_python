#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/17 下午2:25

#通过快慢指针，fast每次移动两个节点，slow每次移动一个节点
#如果存在环结构，那么fast指针在不断环绕的过程中，肯定会追上slow指针

class Solution:
    def hasCycle(self,head):
        if head is None:
            return False
        elif head.next is None:
            return False
        slow = head.next
        fast = head.next
        if fast.next is not None:
            fast = fast.next

        while (slow.next is not None) and (fast.next is not None):
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
            if fast.next != None:
                fast = fast.next
        return False