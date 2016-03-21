# coding = utf-8

"""
1.著名七桥问题（别看答案，好好想想）

有这么一个地方，每个桥只能走一遍，请问你能不能一次把全部桥走完呢？写出你的证明，别上网搜答案哦。
看图： http://a2.att.hudong.com/68/93/01300000089793120693931525342.jpg
"""

"""
1.不能。每个桥只走一遍，要么全部都是偶数的节点，要么是只有起始于结束节点是奇数节点，图中有四个基数节点所以能不一次性走过。
"""


"""
2.小孩会不会控制鳄鱼？（此题是有答案的，会或不会）

没有不会法术又可以控制鳄鱼的人。
有逻辑的人都不讨厌。
没逻辑的会法术。
小孩都是讨厌的。
"""
# coding = utf-8

""" 控制鳄鱼需要会法术"""
skunk = True #小孩都是讨厌的
logic = not skunk # 有逻辑的人都不讨厌
magic = not logic # 没逻辑的会法术

# 没有不会法术又可以控制鳄鱼的人
if magic == True:  
    print '小孩会控制鳄鱼'
else: print '小孩不会控制鳄鱼'

# 小孩会控制鳄鱼


"""
3.递归斐波那契数列（易）

请用递归写出斐波那契数列中第n个数。

菲波那切数列：1,1,2,3,5,8,13....
例子：
输入:[0] 输出:1
输入:[1] 输出:1
输入:[2] 输出:2
"""

def function(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return function(n-1) + function(n-2)
    
if __name__ == '__main__':
    print function(0)
    print function(1)
    print function(2)
    print function(3)
    print function(4)
    print function(5)
    print function(6)
    print function(7)
    
    


 """
 4.最长的和为零（难）
给一串数组，问最长连续几个数相加的和为零。
例子：
输入:[2,-2] 输出:2
输入:[0,1,2,3,-1,-3,-1,5] 输出:5
输入:[0,1,2,3] 输出:1
输入:[1,1,1,1,1,1,-3,1,1,1,1,-4] 输出:9
输入:[1,-1,2,3,-2,-1] 输出:3
"""
    
def function(List):
    count = 0
    for i in xrange(len(List)):
        for j in xrange(i+1, len(List)):
            if sum(List[i:j+1]) == 0:
                #print j, i ,"_______"
                if j-i>count:
                    count = j-i+1
    return count
    
if __name__ == "__main__":
    print function([2,-2])
    print function([0,1,2,3,-1,-3,-1,5])
    print function([0,1,2,3])
    print function([1,1,1,1,1,1,-3,1,1,1,1,-4])
    print function([1,-1,2,3,-2,-1])
                
