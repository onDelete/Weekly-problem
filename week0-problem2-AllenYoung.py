#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-17 16:33:16
# @Author  : Allen Young (allenyoung717@gmail.com)
# @Version : $Id$

'''
问题2：圆桌问题

过年了，N个小伙伴绕着一个圆桌做游戏，他们每个人都有独自的编号，而他们是根据自己的编号（1,2,3...N) 按顺序坐的。

游戏的规则是，从1号开始数，依次请第“三”个人离开座位，请问最后留下的人编号是多少？
'''
def function(N):
    if N<1:
        return 0
    num_list = range(1,N+1)
    rst = N
    num_leave = 1
    while rst>1:
        num_leave += 2
        num_leave %= rst
        if num_leave == 0:
            num_leave=rst
        num_list.pop(num_leave-1)

        rst -= 1
    return num_list[0]

N=5
print 'if N = 5, the Output should be 4. The function return:', function(N)

N=3
print 'if N = 3, the Output should be 2. The function return:', function(N)

N=6
print 'if N = 6, the Output should be 1. The function return:', function(N)

N=0
print 'if N < 1, the Output should be 0. The function return:', function(N)
