# -*- coding: utf-8 -*-

from itertools import groupby
from collections import defaultdict, namedtuple


# problem one
"""
问题1：字符串之和
我们有任意一字符串包括字母（不分大小写），每个字母个代表一个唯一的数字:

A,a = 1
B,b = 2
C,c = 3
.
.
.
Z,z = 26

我们用一种特殊的算数方法来求得这个字符串的和，那就是：每个字母代表的数字乘以比他大的字母的个数的积，然后所有的积相加。

比如: "abca"
为 1 * 2 + 2 * 1 + 3 * 0 + 1 * 2 = 6
第一个 1 * 2 中：1是a所代表的数字，2是因为bc 比a大，所以有两个数字比他大

例子:
输入: "abc"       输出：4
输入: "zxy"       输出: 73
输入: "cccdca"    输出：17
"""


class ProblemOne(object):
    ZERO = ord('a') - 1
    testdata = [
        ('abc', 4),
        ('zxy', 73),
        ('cccdca', 17)
    ]

    @classmethod
    def function1(cls, string):
        grps = groupby(sorted(string.lower()))
        grps = [(g[0], len(list(g[1]))) for g in grps]
        mysum = 0
        for i, x in enumerate(grps):
            # 字母数字 * 字母个数 * 比它大的字母个数
            mysum += (ord(x[0])-cls.ZERO) * x[1] * sum(g[1] for g in grps[i+1:])
        return mysum

    @classmethod
    def function2(cls, string):
        """Learn to use defaultdict as a convenience data type."""
        cnts = defaultdict(lambda: [0, 0])
        for c in reversed(sorted(string.lower())):
            cnts[c][0] += sum(cnts[x][1] for x in cnts if x != c)
            cnts[c][1] += 1
        return sum((ord(k)-cls.ZERO) * v[0] for k, v in cnts.items())

    @classmethod
    def function3(cls, string):
        """Learn to use namedtuple to help verifying tuple member."""
        Count = namedtuple('Count', ['count', 'larger'])
        cnts = defaultdict(lambda: Count(0, 0))
        for c in reversed(sorted(string.lower())):
            cnts[c] = cnts[c]._replace(
                larger=cnts[c].larger + sum(cnts[x].count for x in cnts if x != c),
                count=cnts[c].count + 1
            )
        return sum((ord(k)-cls.ZERO) * v.larger for k, v in cnts.items())

    def solve(self, *args):
        return self.function1(*args)


# problem two
"""
问题2：草原模拟题 （我觉得这道题比较有趣） 这道题并不是什么算法题，
是为了鼓励大家写出模块化的程序，写出逻辑性强，易修改的程序。

有一片草原上生活着兔子和狼，当然还有草。草，兔子和狼的个数分别是x,y,z。
他们的生物链规则是这样的，每两只兔子可以生一只兔子，每两条狼可以生一只狼。
但是他们繁育的条件是必须吃掉相同个数的食物，比如两只兔子要想生一只小兔子，那他们就要吃两根草。
草的个数每天都是以二的倍数生长着。比如第一天有3根草，第二天就有6根。我们还要设个规定，
草是每天都生长的，但是兔子是每两天吃一次草，狼是每三天吃一次兔子（第一天他们都想吃，如果可能的话）。

在这个问题里，我们假设生物都不会自然死亡。而如果食物的个数小于等于2，他们就得等。

举个栗子：
假如一开始有4根草，2只兔子，2条狼。那么第一天兔子可以吃草，狼不能吃兔子，
而草可以生长。他们行动的顺序是狼->兔子->草。

那么第一天（初始值）:     x = 4 y = 2 z = 2 (草兔子狼都想繁育，但是狼不能吃，兔子可以，草剩2再乘2）
第二天:      x = 4 y = 3 z = 2 （只有草想繁育，草翻倍）
第三天:      x = 8 y = 3 z = 2  （草兔子想繁育，兔子能生一只小兔子，草剩6再乘二）
第四天：    x = 12 y = 4 z = 2 （草狼想繁育，兔子剩2，狼能生一只小狼，草乘2）
第五天：    x = 20 y = 2 z = 3  （草，兔子想繁育，兔子成为3，草剩18乘2）

问题是，假如草原上一开始有5根草，33只兔子，3条狼，那么多少天后狼的数量能达到 50 呢？
"""


class Grassland(object):
    _count = 0

    @classmethod
    def initialize(cls, initial):
        cls._count = initial

    @classmethod
    def eaten(cls, count):
        cls._count -= count

    @classmethod
    def count(cls):
        return cls._count


class Grass(Grassland):
    _count = 0

    @classmethod
    def populate(cls):
        cls._count *= 2

    @classmethod
    def can_be_eaten(cls):
        return cls._count - 2


class Rabbit(Grassland):
    _count = 0

    @classmethod
    def can_be_eaten(cls):
        return cls._count - 2

    @classmethod
    def populate(cls, eating=Grass):
        x = eating.can_be_eaten()
        # 只能吃偶数个，不能吃奇数个
        # 如果草多兔子少，按照兔子最多能吃掉的数量吃，其他草继续繁殖
        # 如果草少兔子多，按照最多能被吃掉的草数量吃，其他兔子等着
        y = min(2 * (cls._count // 2), 2 * (x // 2))
        z = y // 2
        eating.eaten(y)
        cls._count += z

    @classmethod
    def populate_cleverly(cls, eating=None):
        x = eating.can_be_eaten()
        # 只能吃偶数个，不能吃奇数个，于狼类似，但是草每天繁殖一次
        # (x - y) * 2 * 2 = y * 2 + y => x = 7 * y / 4
        if x < cls._count * 7 / 4:
            return
        else:
            y = cls._count
        # 取偶数，确保不会生出半只狼出来
        y = 2 * (y // 2)
        z = y // 2
        eating.eaten(y)
        cls._count += z


class Wolf(Grassland):
    _count = 0

    @classmethod
    def populate(cls, eating=Rabbit):
        x = eating.can_be_eaten()
        # 只能吃偶数个，不能吃奇数个
        # 如果兔子多狼少，按照狼最多能吃掉的数量吃，其他兔子继续繁殖
        # 如果兔子少狼多，按照最多能被吃掉的兔子数量吃，其他狼等着
        y = min(2 * (cls._count // 2), 2 * (x // 2))
        z = y // 2
        eating.eaten(y)
        cls._count += z

    @classmethod
    def populate_cleverly(cls, eating=None):
        x = eating.can_be_eaten()
        # 只能吃偶数个，不能吃奇数个
        # 假设狼王是聪明的并且是公平的，每一次繁殖时都可以让所有的狼进行，
        # 在每次决定吃多少兔子时，令兔子，狼，和要吃掉兔子的数量分别为 x, y, z
        # 在一次繁殖周期内，兔子会增加二分之一的数量，狼会增加二分之一的数量
        # 那么狼王希望 下一次 吃兔子时能令所有狼都有兔子吃，
        # 需要保持 (x - z) * 1.5 = y * 2 + z
        # 狼王当然也希望这一次吃兔子时，所有的狼也都有兔子吃，那么令 z = y
        # 即是 (x - y) * 1.5 = y * 2 + z => x = 3y
        if x < cls._count * 3:
            return
        else:
            y = cls._count
        # 取偶数，确保不会生出半只狼出来
        y = 2 * (y // 2)
        z = y // 2
        eating.eaten(y)
        cls._count += z


class ProblemTwo(object):
    testdata = [
        ((5, 33, 3), 22),
    ]

    @classmethod
    def function1(cls, g, r, w):
        """假设狼是贪婪的，只要有兔子吃就吃，不考虑可持续发展"""
        Grass.initialize(g)
        Rabbit.initialize(r)
        Wolf.initialize(w)
        day = 0
        print('day: 0, grass: %s, rabbits: %s, wolfs: %s' % (g, r, w))
        while Wolf.count() < 50:
            day += 1
            Grass.populate()
            if day % 2 == 1:
                Rabbit.populate()
            if day % 3 == 1:
                Wolf.populate()
            print('day: %s, grass: %s, rabbits: %s, wolfs: %s' % (
                day, Grass.count(), Rabbit.count(), Wolf.count()))
        return day

    @classmethod
    def function2(cls, g, r, w):
        """假设狼王很聪明，知道可持续发展，不会一次把草吃光，以每次繁殖最多狼为目标"""
        Grass.initialize(g)
        Rabbit.initialize(r)
        Wolf.initialize(w)
        day = 0
        print('day: 0, grass: %s, rabbits: %s, wolfs: %s' % (g, r, w))
        while Wolf.count() < 50:
            day += 1
            Grass.populate()
            if day % 2 == 1:
                # 兔子很聪明
                Rabbit.populate_cleverly(Grass)
            if day % 3 == 1:
                # 狼也很聪明
                Wolf.populate_cleverly(Rabbit)
            print('day: %s, grass: %s, rabbits: %s, wolfs: %s' % (
                day, Grass.count(), Rabbit.count(), Wolf.count()))
        return day

    def solve(self, args):
        return self.function2(*args)


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
