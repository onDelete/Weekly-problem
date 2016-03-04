# problem one
"""
问题1： 一维OX
给你一串包含'X'和'O'字符串，如"OXOOOXXXOXXOOOXXXOXO",问这个字符串中，
与其中一个X直接相连（中间没有X格着）的O最多有多少个？比如"OXOO",就有三个O与X相连。
但是"OXOOOXOO"最多就是五个而不是六个，因为左边的X挡住了最左边的O。

输入：字符串 输出：整数

例子：
输入:"OXO"            输出：2
输入:"OXOOXOXXOOOXO"  输出：4
输入:"OOXOOOXOXO"     输出：5
输入:"OOOOOOOOOO"     输出：0
输入:"XXX"            输出：0

:type string: str
:rtype: int
"""
class ProblemOne(object):
    def function1(self, string):
        o_max = 0
        ox_map = {'o1': 0, 'o2': 0, 'x': 0}
        for c in string:
            if c == 'X':
                if ox_map['x'] > 0:
                    o_max = max(o_max, ox_map['o1'] + ox_map['o2'])
                ox_map['x'] += 1
                ox_map['o1'], ox_map['o2'] = ox_map['o2'], 0
            else:
                ox_map['o2'] += 1
        if ox_map['x'] == 0:
            return 0
        o_max = max(o_max, ox_map['o1'] + ox_map['o2'])
        return o_max

    def function2(self, string):
        lst = string.split('X')
        if len(lst) < 2:
            return 0
        return max(len(lst[i]) + len(lst[i+1]) for i in range(len(lst)-1))

    def solve(self, *args):
        return self.function2(*args)


# problem two
"""
问题2: 二维OX
给你一串字符串，一个整数代表每行字符的个数，求与其中一个X直接相连（紧挨着）的O最多有多少个？

输入："OXOOOXOXOXOXXOX"， "5" 输出：3
    其图像为：
    OXOOO
    XOXOX
    OXXOX

输入："OXOOOXOXOXOXXOX"， "10" 输出：2
    其图像为：
    OXXOXOOXOX
    OXOOXOOXOX

输入："XOOXOOOOOOXOOXOXXXOX"， "5" 输出：4
    其图像为：
    XOOXO
    OOOOO
    XOOXO
    XXXOX

显而易见，输出最小是0，最大只可能是4.

:type string: str
:type width: int
:rtype: int
"""
class ProblemTwo(object):
    def function1(self, string, width):
        def partition(seq, n):
            args = [iter(seq)] * n
            return list(zip(*args))
        matrix = partition(string, width)

        def judge(i, j):
            try:
                return int(matrix[i][j] == 'O')
            except IndexError:
                return 0

        o_max = 0
        x_index = filter(lambda idx: matrix[idx[0]][idx[1]] == 'X',
                         ((i, j) for i in range(len(matrix)) for j in range(width)))
        for i, j in x_index:
            o_count = sum([judge(i, j-1), judge(i-1, j), judge(i, j+1), judge(i+1, j)])
            o_max = max(o_max, o_count)
        return o_max

    def solve(self, *args):
        return self.function1(*args)


# problem three
"""
问题3: 冒泡排序
用冒泡排序给一个数组排序。输入一个数组，输出排好的数组。

:type lst: List[int]
:rtype: List[int]
"""
class ProblemThree(object):
    def function1(self, lst):
        need_sort = True  # 优化：排序标记
        for i in range(len(lst)-1, 0, -1):
            if not need_sort:
                return lst
            need_sort = False
            for j in range(i):
                if lst[j] > lst[j+1]:
                    need_sort = True
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst

    def solve(self, *args):
        return self.function1(*args)


if __name__ == '__main__':
    from itertools import starmap
    print(list(map(ProblemOne().solve, [
        'OXO', 'OXOOXOXXOOOXO', 'OOXOOOXOXO', 'OOOOOOOOOO', 'XXX'])))
    print(list(starmap(ProblemTwo().solve, [
        ('OXOOOXOXOXOXXOX', 5), ('OXOOOXOXOXOXXOX', 10), ('XOOXOOOOOOXOOXOXXXOX', 5)])))
    print(ProblemThree().solve([6, 2, 4, 1, 5, 9]))

