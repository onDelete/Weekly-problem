def Function(Str,List,Num):
    while Num > 0:
        Num -= 1
        new_str = ''
        for i in List:
            new_str = new_str + Str[i]
        Str = new_str

    return new_str


if __name__ == '__main__':
    print Function("ABC",[2,0,1],2)
    print Function("ABCD",[3,2,1,0],1)
    print Function("12345",[3,1,2,4,0],1)
