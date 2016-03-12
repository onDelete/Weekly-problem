# -*- coding: utf-8 -*-
def getCount(s, n):
    
    def getArrs(s, n):
        strs = []
        j = 0
        str_temp = ''
        for i in range(len(s)):
            if (i+1)%n!=0:
                str_temp = str_temp + s[i]
            else:
                str_temp = str_temp + s[i]
                strs.append(str_temp)
                str_temp = ''
        return strs
    s = getArrs(s, n)
    count = 0
    result = 0
    for i in range(len(s)):
        print 's[%d] = %s' % (i, s[i])
        for j in range(len(s[i])):
            print 's[%d][%d]] = %s' % (i, j, s[i][j])
            if s[i][j] == 'X':
                #中间
                if (i!=0) and (j!=0) and (i!=len(s)-1) and (j!=len(s[i])-1):
                    strs = s[i-1][j] + s[i+1][j] + s[i][j-1] + s[i][j+1]
                #四个角
                elif (i==0)and(j==0):
                    strs = s[i+1][j] + s[i][j+1]
                elif (i==0) and (j==len(s[i])-1):
                    strs = s[i+1][j] + s[i][j-1]
                elif (i==len(s)-1) and (j == 0):
                    strs = s[i-1][j] + s[i][j+1]
                elif (i==len(s)-1) and (j==len(s[i])-1):
                    strs = s[i-1][j] + s[i][j-1]
                #四个边
                elif (i==0)and(j!=0)and(j!=len(s[i])-1):
                    strs = s[i+1][j] + s[i][j+1] + s[i][j-1]
                elif (i!=0)and(i!=len(s)-1) and (j==len(s[i])-1):
                    strs = s[i+1][j] + s[i][j-1] + s[i+1][j]
                elif (i==len(s)-1) and (j != 0)and (j==len(s[i])-1):
                    strs = s[i-1][j] + s[i][j+1] + s[i][j-1]
                elif (i!=0)and(i!=len(s)-1) and (j==0):
                    strs = s[i-1][j] + s[i][j+1] + s[i+1][j]
                for str1 in strs:
                    if str1 == 'O':
                        count+=1
                result = max(count, result)
                count=0
    return result
