
#coding:utf-8
def function(N):
    if N <= 0:
        return 0
    table = range(1, N + 1)
    while len(table) > 0:
        for i in range(2):
            table.append(table.pop(0))
        outNumber = table.pop(0)
    return outNumber

N = 5
print function(N)
N = 3
print function(N)
N = 6
print function(N)
N = -1
print function(N)
