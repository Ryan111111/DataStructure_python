#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/1 上午9:55

class Stack(object):
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return self.stack == []
    def peek(self):
        return self.stack[len(self.stack)-1]
    def push(self,n):
        self.stack.append(n)
    def pop(self):            #把栈顶元素抛出去
        return self.stack.pop()
    def printstack(self):
        print(self.stack)

def sortStack(stack,help):
    while(stack.is_empty() != True):
        cur = stack.pop()
        while(help.is_empty() != True)and(help.peek()>cur):
            stack.push(help.pop())
        help.push(cur)

    while(help.is_empty() != True):
        stack.push(help.pop())


stack = Stack()
help = Stack()
stack.push(1)
stack.push(6)
stack.push(4)
stack.push(2)

stack.printstack()

sortStack(stack,help)
stack.printstack()
