# -*- coding: utf-8 -*-

import functools


# problem two
"""
2.小孩会不会控制鳄鱼？（此题是有答案的，会或不会）

没有不会法术又可以控制鳄鱼的人。
(改：会法术的都可以控制鳄鱼）
有逻辑的人都不讨厌。
没逻辑的会法术。
小孩都是讨厌的。
"""


class Person(object):
    def __init__(self, is_hated):
        self.being_hated = is_hated

    @property
    def has_logic(self):
        return not self.being_hated

    @property
    def has_magic(self):
        return not self.has_logic

    @property
    def can_control_crocodile(self):
        return self.has_magic


class ProblemTwo(object):
    testdata = [
        (True, True),
        (False, False)
    ]

    @staticmethod
    def function1(is_hated):
        child = Person(is_hated)
        return child.can_control_crocodile

    def solve(self, *args):
        return self.function1(*args)


# problem three
"""
3.递归斐波那契数列（易）
请用递归写出斐波那契数列中第n个数。
菲波那切数列：1,1,2,3,5,8,13....

例子：
输入:[0] 输出:1
输入:[1] 输出:1
输入:[2] 输出:2

:type lst1: list(int)
:type lst2: list(int)
:rtype: int
"""


class ProblemThree(object):
    testdata = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13)
    ]

    # 斐波那契数列定义
    # 可以使用 LRU Cache 来缓存计算结果，提高计算速度
    @functools.lru_cache()
    def fibonacci1(self, num):
        if num < 0:
            return 0
        if num <= 1:
            return 1
        return self.fibonacci1(num-1) + self.fibonacci1(num-2)

    # 传入两个参数可以减少一次递归调用
    # Python 没有尾递归优化，默认递归调用深度1000
    def fibonacci2(self, num, a=1, b=1):
        if num < 0:
            return 0
        if num <= 1:
            return a
        return self.fibonacci2(num-1, a+b, a)

    # 使用 Y 组合子的尾递归优化，可以把递归调用转换成迭代，不受递归深度限制
    @staticmethod
    def fibonacci3(num):
        def tco(func):
            # y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))
            #   = lambda f: (lambda x: x(x))(lambda x: f(x(x)))
            # z = lambda f: (lambda x: x(x))(lambda x: f(lambda v: x(x)(v)))
            tco = lambda f: (lambda x: x(x))(lambda x: f(lambda *args, **kwargs: lambda: x(x)(*args, **kwargs)))

            def wrapper(*args, **kwargs):
                out = tco(func)(*args, **kwargs)
                while callable(out):
                    out = out()
                return out
            return wrapper

        fib = tco(lambda f: lambda n, a=1, b=1: a if n <= 1 else f(n-1, a+b, a))
        return fib(num)

    def solve(self, *args):
        return self.fibonacci1(*args)


# problem four
"""
4.最长的和为零（难）

给一串数组，问最长连续几个数相加的和为零。

例子：
输入:[2,-2] 输出:2
输入:[0,1,2,3,-1,-3,-1,5] 输出:5
输入:[0,1,2,3] 输出:0
输入:[1,1,1,1,1,1,-3,1,1,1,1,-4] 输出:9
输入:[1,-1,2,3,-2,-1] 输出:3
"""


class ProblemFour(object):
    testdata = [
        ([2,-2], 2),
        ([0,1,2,3,-1,-3,-1,5], 5),
        ([0,1,2,3], 0),
        ([1,1,1,1,1,1,-3,1,1,1,1,-4], 9),
        ([1,-1,2,3,-2,-1], 3)
    ]

    @staticmethod
    def function1(lst):
        length = len(lst)
        sum_max_length = 0
        for i in range(0, length):
            # 如果数组剩余长度比已找到的短，没有更长的了，返回找到的长度
            if length - i < sum_max_length:
                return sum_max_length
            # 迭代寻找求和为 0 的子数组
            # 从 i + sum_max_length + 1 开始迭代，减少搜索数量
            for j in range(i+sum_max_length+1, length+1):
                mysum = sum(lst[i:j])
                if mysum == 0 and j-i > sum_max_length:
                    sum_max_length = j - i
        return sum_max_length

    def solve(self, *args):
        return self.function1(*args)


if __name__ == '__main__':
    problems = filter(lambda x: x.startswith('Problem'), dir())
    for prob in problems:
        print('\nTest for %s:' % prob)
        prob = eval(prob)()
        for input, answer in prob.testdata:
            output = prob.solve(input)
            print('%s: input: %s (answer: %s), output: %s' % (
                'passed' if output == answer else 'failed',
                input, answer, output))
