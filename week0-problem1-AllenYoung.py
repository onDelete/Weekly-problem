#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-16 15:30:27
# @Author  : Allen Young (allenyoung717@gmail.com)
# @Version : $Id$

def function(x,l):    
    l.sort() # 将list从小到大排序    
    s = 0       # 初始化和   
    n = 0       # 初始化个数
    for item in l:
        s += item   # 以金额从小到大累加
        if s > x:   # 判断是否超出所有的钱
            break
        n += 1
    return n


# 测试
x = 5 
l = [3,8,1,2,3]
print 'moeny in total is', x,'items prices are:',l
print 'The output should be 2, the function return:', function(x, l)
print 

x = 3
l = [2,1,5]
print 'moeny in total is', x,'items prices are:',l
print 'The output should be 2, the function return:', function(x, l)
print 

x = 10
l = [1,1,1,1,2,5]
print 'moeny in total is', x,'items prices are:',l
print 'The output should be 5, the function return:', function(x, l)
print 

x = 10 
l = [5,10,3,2]
print 'moeny in total is', x,'items prices are:',l
print 'The output should be 3, the function return:', function(x, l)
print 

x = 2
l = [3,8,10]
print 'moeny in total is', x,'items prices are:',l
print 'The output should be 0, the function return:', function(x, l)
print 

x = input('Total money you have: ')
l = raw_input('the price of items you want to buy(use space between items, use Enter to end):\n')
l = l.split()
l = map(int, l)
print 'You can buy', function(x, l), 'at most.'
