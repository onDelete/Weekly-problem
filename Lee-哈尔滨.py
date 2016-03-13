#!/usr/bin/env python
# -*- coding=utf-8 -*-


def question1(a, b):

    ''' 俺的数组里有你的数组吗？ '''
    have = False
    for i,ch in enumerate(a):
        if ch == b[0] and len(a)-i >= len(b):
            have = True
            for j in range(1, len(b)):
                if a[i+j] != b[j]:
                    have = False
                    break
    return have




def question2(a, b):

    '''那俺的数组里得数能组成你的数组吗？'''

    k,have = 0,False
    for i in range(len(a)):        
        for j in range(k,len(b)):
            print a[i],b[j]
            if a[i] != b[j]:
                break
            if a[i] == b[j]:
                if j == len(b) - 1:
                    have = True                    
                k += 1
                break
        if have == True:
            break
    return have


if __name__ == "__main__":
    print "第一题结果------"
    print question1([0,1,2,3,4],[1,2]) 
    print question1([0,1,2,3,1,2,3],[3,1,2])
    print question1([1,0,2],[1,2]) 

    print "第二题结果------"
    print question2([1,3,2,4,3,5,6],[1,2,3,6])
    print question2([1,2,1,1],[1,1,1])
    print question2([1,2,1,2,0,1,2],[2,1,2,1])
    print question2([3,2,1,0,7],[7,1,2,3])
    print question2([1,3,5],[2])