def getNum(x, goods):
    if x <= 0 or len(goods) == 0:return 'params error'
    num = 0
    cost = 0
    goods.sort()
    while cost <= x and num <= (len(goods)-1):
        cost += goods[num]
        num += 1

    return num - 1
