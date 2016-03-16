def solution(Y,M):
    i, j = 0, 0
    mark = 0
    result = 0
    while i!=len(Y) and j!=len(M):
        if Y[i] == M[j]:
            mark = i
            result = 1
            j += 1
            i += 1
        else:
            if result == 0:
                i += 1
            else:
                i = mark + 1
            result = 0
    if j != len(M):
        result = 0
    return result


Y = [1,3,2,4,3,5,6]
M = [1,2,3,6]
print solution(Y,M)
Y = [1,2,1,1]
M = [1,1,1]
print solution(Y,M)
Y = [1,2,1,2,0,1,2]
M = [2,1,2,1]
print solution(Y,M)
Y = [3,2,1,0,7]
M = [7,1,2,3]
print solution(Y,M)
Y = [1,3,5]
M = [2]
print solution(Y,M)
