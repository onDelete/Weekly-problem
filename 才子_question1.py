def getCount(s):
    count = 0
    start = 1
    if (not 'X' in s) or (not 'O' in s):
        return 0
    for i in range(len(s)):
        if s[i] == 'X':
            temp = 0
            for j in range(i+1, len(s)):
                if s[j] == 'X':
                    temp = len(s[start:i]) + len(s[i+1:j])
                    count = max(temp, count)
                    start = i+1
                    break
                    
                elif j == len(s) - 1:
                    temp = len(s[start:i]) + len(s[i+1:j+1])
                    count = max(temp, count)
                    break
                    
    return count
