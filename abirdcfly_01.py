def solution(Y,M):
    i, j = 0, 0
    mark = 0
    result = 0
    while i != len(Y) and j != len(M):
        if Y[i] == M[j]:
            mark = i
            result = 1
            j += 1
            i += 1
        else:
            j = 0
            if result == 0:
                i += 1
            else:
                i = mark + 1
            result = 0
    if j != len(M):
        result = 0
    return result


Y = [0,1,0,1,2,3,4]
M = [1,2]
print solution(Y,M)
Y = [0,1,2,3,1,2,3]
M = [3,1,2]
print solution(Y,M)
Y = [1,0,2]
M = [1,2]
print solution(Y,M)
