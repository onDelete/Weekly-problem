def iscontain(s1, s2):
    str1 = ''
    str2 = ''
    for i in s1:
        str1 = str1 + str(i)
    for j in s2:
        str2 = str2 + str(j)
    if str2 in str1:
        return 1
    else :
        return 0
