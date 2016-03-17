# -*- coding: utf-8 -*-
def fib(n):
    """
    :param n: 接受正整数n为参数
    :return: 返回斐波那契数列中第n个数
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def test():
    for n in range(1, 10):
        print u"斐波那契第%s个数是%s" % (n, fib(n))


if __name__ == "__main__":
    test()

