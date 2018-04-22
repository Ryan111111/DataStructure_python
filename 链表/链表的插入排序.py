#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/29 下午3:44

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertSortList(self,head):
        if head is None:return None
        if head.next is None:return head

        new = ListNode(0)
        while head is not None:
            node = new
            fol = head.next
            while node.next is not None and node.next.val < head.val:
                node = node.next
            head.next = node.next
            node.next = head
            head = fol
        return new.next