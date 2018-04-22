#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/15 下午7:41

#用一个hash表，存储每一个数的下标，时间复杂度O(N),空间复杂度O(N)
#找到数组中和为定值的两个数，返回其对应的下标
def twoSum(A,s):
    l = len(A)
    mHash,res = {},[]
    for i in range(l):
        mHash[A[i]] = i
    for i in range(l):
        t = s - A[i]
        if t in mHash:
            res.append(i)
            res.append(mHash[t])
            break
    return res

#寻找和为定值的多个数
mlist = []
def find_factor(s,n):
    if n <= 0 or s <= 0:
        return
    if s == n:
        print(n)
    mlist.insert(0,n)
    find_factor(s-n,n-1)
    del mlist[0]
    find_factor(s,n-1)


#先排序，然后左右夹逼，排序O（N*logN），夹逼O（N），总O（N*logN）
#查找数组中两个数为指定值的两个数
def partition(s, m, n):
	#s is a list
	key = s[n-1]
	l,r = m,n-2
	while True:
		while l <= n-2 and s[l] <= key:
			l += 1
		while r>= m and  s[r] > key:
			r -= 1
		if l < r:
			s[l],s[r] = s[r],s[l]
		else:
			break
	s[l],s[n-1] = s[n-1],s[l]
	return l

def medin3(s, m, n):
	md = m + (n-m)/2
	if s[m] > s[md]:
		s[m],s[md] = s[md],s[m]
	if s[m] > s[n]:
		s[m],s[n] = s[n],s[m]
	if s[md] > s[n]:
		s[md],s[n] = s[n],s[md]
	s[md],s[n-1] = s[n-1],s[md]
	return s[n-1]

def quicksort(s, m, n):
	#s is a list
	if m < n:
		medin3(s, m, n)
		k = partition(s, m, n)
		quicksort(s, m, k)
		quicksort(s, k+1, n)

def twoSumd(A, s):
	'''快速排序，夹逼, 返回两个数'''
	lens = len(A)
	quicksort(A, 0, lens-1)
	l,r = 0,lens-1
	while l<r:
		if A[l] + A[r] < s:
			l += 1
		elif A[l] + A[r] > s:
			r -= 1
		else:
			return (A[l],A[r])
	return False



if __name__ == '__main__':
    A = [1,2,4,7,11,15]
    s = 15
    print(twoSum(A,s))