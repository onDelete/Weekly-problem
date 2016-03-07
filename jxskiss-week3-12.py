# problem one
"""
问题1： 俺的数组里有你的数组吗？
你我各有一串数组，现在我想知道我的数组里有没有你的数组，怎么办呢？
比如我的数组是[0,1,2,3,4,5],你的是[2,3]。那么我的数组里就包含了你的数组。

例子:
输入: [0,1,2,3,4],[1,2]               输出:1
输入: [0,1,2,3,1,2,3],[3,1,2]         输出:1
输入: [1,0,2],[1,2]                   输出:0

:type lst1: list(int)
:type lst2: list(int)
:rtype: int
"""


class ProblemOne(object):
    testdata = [[[[0,1,2,3,4], [1,2]], 1],
                [[[0,1,2,3,1,2,3], [3,1,2]], 1],
                [[[1,0,2], [1,2]], 0]]

    def function1(self, lsts):
        lst1, lst2 = lsts
        length = len(lst2)
        for i in range(len(lst1)):
            if lst1[i:i+length] == lst2:
                return 1
        return 0

    def solve(self, *args):
        return self.function1(*args)


# problem two
"""
问题2:那俺的数组里得数能组成你的数组吗？
跟问题1很相似，但是这时候我的数组里的数并不需要“连续”跟你一样，
才能称之为“有你的数组”，但是顺序依旧重要。 举个栗子:
[0,7,1,7,2,7,3] 包含 [0,1,2,3] 因为我们可以无视掉7。
但是[3,2,1,7]不包含[1,2,3]因为他们的排列顺序不一样。

例子：
输入:[1,3,2,4,3,5,6],[1,2,3,6]                输出:1
输入:[1,2,1,1],[1,1,1]                        输出:1
输入:[1,2,1,2,0,1,2],[2,1,2,1]                输出:1
输入:[3,2,1,0,7],[7,1,2,3]                    输出:0
输入:[1,3,5],[2]                              输出:0

:type lst1: list(int)
:type lst2: list(int)
:rtype: int
"""


class ProblemTwo(object):
    testdata = [[[[1,3,2,4,3,5,6], [1,2,3,6]], 1],
                [[[1,2,1,1], [1,1,1]], 1],
                [[[1,2,1,2,0,1,2], [2,1,2,1]], 1],
                [[[3,2,1,0,7], [7,1,2,3]], 0],
                [[[1,3,5], [2]], 0]]

    def function1(self, lsts):
        lst1, lst2 = lsts
        i = j = 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] == lst2[j]:
                i, j = i + 1, j + 1
            else:
                i += 1
        return 1 if j == len(lst2) else 0

    def solve(self, *args):
        return self.function1(*args)


if __name__ == '__main__':
    problems = filter(lambda x: x.startswith('Problem'), dir())
    for prob in problems:
        prob = eval(prob)
        print('\nTest for %s:' % prob)
        for input, answer in prob.testdata:
            output = prob().solve(input)
            print('%s: input: %s (answer: %s), output: %s' % (
                'passed' if output == answer else 'failed',
                input, answer, output))
