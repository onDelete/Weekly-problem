# coding = utf-8

def function(List):
    if 1 == len(List): return List
    for i in xrange(len(List)):
        for j in xrange(len(List)-i-1):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
    return List

if __name__ == '__main__':
    print function([3,2,1])
    print function([1,5,4,6,7]) 
    print function([0,2,4,5,7]) 
    print function([1])
