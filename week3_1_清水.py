# coding = utf-8
"""
你我各有一串数组，现在我想知道我的数组里有没有你的数组，怎么办呢？

比如我的数组是[0,1,2,3,4,5],你的是[2,3]。那么我的数组里就包含了你的数组。

例子: 
输入: [0,1,2,3,4],[1,2]               输出:1
输入: [0,1,2,3,1,2,3],[3,1,2]         输出:1
输入: [1,0,2],[1,2]                   输出:0
"""

def function(list1, list2):
    s1 = ''
    s2 = ''
    for i in list1:
        s1 += str(i)
    for i in list2:
        s2 += str(i)
        
    if s2 in s1: return 1
    return 0

if __name__ == '__main__':
    print function([0,1,2,3,4],[1,2] )
    print function([0,1,2,3,1,2,3],[3,1,2])
    print function( [1,0,2],[1,2] )
