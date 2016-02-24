# coding = utf-8

def decode(strs, lists, n):
    if strs == '' or lists == [] or n < 1 or len(strs) != len(lists):
        return -1
    destr = ''
    for i in lists:
        destr += strs[i]
    strs = destr
    if n == 1:
        return destr
    return decode(strs, lists, n-1)    #递归

if __name__ == '__main__':
    print decode('ABC', [2,0,1], 2)
    print decode('ABCD', [3,2,1,0], 1)
    print decode('12345', [3,1,2,4,0], 1)
    


