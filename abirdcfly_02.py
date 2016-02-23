#!/usr/bin/env python
# -*- coding: utf8 -*-


def function(str, list, N):
    oldlist = range(len(list))
    for i in range(N):
        newstr = ""
        for i in list:
            newstr = newstr + str[oldlist.index(i)]
        str = newstr
    return newstr


str = "h?lunc"
list = [1,2,3,4,5,0]
N = 2
print function(str, list, N)

str = "ABC"
list = [2, 0, 1]
N = 2
print function(str, list, N)

str = "ABCD"
list = [3, 2, 1, 0]
N = 1
print function(str, list, N)

str = "12345"
list = [3, 1, 2, 4, 0]
N = 1
print function(str, list, N)
