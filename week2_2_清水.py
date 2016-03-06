# coding = utf-8

def function(xo, n):
    Max, count = 0, 0
    List = []
    for i in xrange(len(xo) / n):
        List.append(xo[:n])
        xo = xo[n:]
        print List[i]

    for i in xrange(len(List)):
        for j in xrange(len(List[i])):
            if 'X' == List[i][j]:
                if i - 1 >= 0 and 'O' == List[i - 1][j]:
                    count += 1
                if j - 1 >= 0 and 'O' == List[i][j - 1]:
                    count += 1  
                if i + 1 <= len(List) - 1 and 'O' == List[i + 1][j]:
                    count += 1  
                if j + 1 <= n - 1 and 'O' == List[i][j + 1]:
                    count += 1 
                if Max < count:
                    Max = count 
                count = 0
    return Max

if __name__ == '__main__':
    print function('OXOOOXOXOXOXXOX', 5)
    print function('OXXOXOOXOXOXOOXOOXOX', 10)
    print function('XOOXOOOOOOXOOXOXXXOX', 5)
