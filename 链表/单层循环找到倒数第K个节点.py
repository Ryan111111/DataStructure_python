#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/16 下午3:29

class Solution:
    def FindKthToTail(self,head,k):
        if head==None or k<=0:
            return None

        p1=head
        p2=head

        #先让p1移动k-1步
        while k>1:
            if p1.next!=None:
                p1=p1.next
                k-=1
            else:
                return None

        #两个指针同时移动
        while p2.next!=None:
            p1=p1.next
            p2=p2.next
            return p1
