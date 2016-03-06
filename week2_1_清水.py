# coding = utf-8

def function(xo):
    Sum, Max = 0, 0    
    string = xo.lower()  #字符串小写字母
    List = string.split('x') #以‘x’把字符串分成序列
    n = len(List)
    if n < 2 or 'o' not in string:
        return 0    # ‘oooo’或‘xxxxx’输出0
    for i in xrange(n - 1):
        Sum = len(List[i]) + len(List[i + 1]) 
        if Max < Sum: Max = Sum
    return Max

if __name__ == '__main__':
    string = raw_input('输入只有‘o’与‘x’组成的字符串：')
    print function(string)
