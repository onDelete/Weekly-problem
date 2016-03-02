# -*- coding: utf-8 -*-

def function(OX):
    b = OX.split('X')   #将字符串按照X分解成list
    c = []              #存储每一个紧挨着X的O个数
    for i in range(len(b)-1):
        d = len(b[i]) + len(b[i+1])     #计算每个相邻的X的O的个数
        c.append(d)                     #将数字存储到c中
    if not c:
        return 0                        #若c是空，返回0
    else:
        print(max(c))                   #返回c里的最大值
