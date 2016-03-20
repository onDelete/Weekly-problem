"""
小孩会不会控制鳄鱼？
小孩都是讨厌的 + 有逻辑的人都不讨厌 = 小孩都是没逻辑的
小孩都是没逻辑的 + 没逻辑的会法术  = 小孩都会法术
小孩都会法术 + 会法术的都会控制鳄鱼 = 小孩会控制鳄鱼

结论：小孩会控制鳄鱼
"""
def fib(n):
    if(n < 2):
        return 1
    return fib(n - 1) + fib(n - 2)

def test():
    for n in range(0,20):
        print ("Fib %d is %d" % (n,fib(n)))

if __name__ == "__main__":
    test()
