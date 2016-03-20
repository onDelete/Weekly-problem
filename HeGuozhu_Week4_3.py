def fib(n):
    if(n < 2):
        return 1
    return fib(n - 1) + fib(n - 2)

def test():
    for n in range(0,20):
        print ("Fib %d is %d" % (n,fib(n)))

if __name__ == "__main__":
    test()
