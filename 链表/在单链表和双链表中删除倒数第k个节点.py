#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/1 下午1:33

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def RemoveLastKthNode(self,head,k):
         if head != True and k<1:
             return head
         cur = head

         while(cur):
             k -= 1
             cur = cur.next

         if k == 0 :
             head = head.next

         elif k < 0:
             cur = head
             if k != 0:
                 cur = cur.next
                 k += 1
             elif k == 0:
                 cur.next = cur.next.next
         return head

