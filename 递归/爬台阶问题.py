#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/16 上午11:59

#递归方法,代码简单，效率比较底，会超出时间上限
def climbStairs(n):
    if n == 1:
        return 1
    elif n==2:
        return 2
    else:
        return climbStairs(n-1)+climbStairs(n-2)

#用循环代替递归，效果会高一点
def climbStairs_2(n):
    if n==1 or n==2:
        return n
    a=1;b=2;c=3
    for i in range(3,n+1):
        c=a+b;a=b;b=c
    return c

#设青蛙跳上这n级台阶一共跳了z次，其中有x次是一次跳了两级，
# y次是一次跳了一级，则有z=x+y ,2x+y=n,对一个固定的x，
# 利用组合可求出跳上这n级台阶的方法共有
#又因为 x在区间[0,n/2]内，所以我们只需要遍历这个区间内所有的整数，
# 求出每个x对应的组合数累加到最后的结果即可
def climbStairs_3(n):
    def fact(n):
        result = 1
        for i in range(1,n+1):
            result *= i
        return result
    total = 0
    for i in range(n/2+1):
        total += fact(i+n-2*i)/fact(i)/fact(n-2*i)
    return total