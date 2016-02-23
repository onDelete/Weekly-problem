#coding=utf-8

def function(x,list):
    asum = 0
    number = 0
    if list != None and x > 0:
        list.sort()
        for i in list:
            asum = asum + i
            if asum > x:
                break
            number += 1
    return number

x=5
list=[3,8,1,2,3]
print function(x,list)
x = 3
list = [2,1,5]
print function(x,list)
x = 10
list = [1,1,1,1,2,5]
print function(x,list)
x = 10
list = [5,10,3,2]
print function(x,list)
x = 2
list = [3,8,10]
print function(x,list)
