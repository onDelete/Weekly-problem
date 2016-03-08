def getCiphertext(str1, arrs, status):
    length = 0
    length = int(len(str1))
    if len(str1)!= len(arrs):
        return "error"
    else:
        if status == 0:
            return str1
        str2 = []
        for i in str1:
            str2.append(i)
        str1 = ''
        for i in arrs:
            str1 = str1 + str2[i]
        
        return getCiphertext(str1, arrs, status-1)
        
str1 = 'abc'
arrs = [2, 0, 1]
status = 2
print 'the anser is: ' + getCiphertext(str1, arrs, status)
