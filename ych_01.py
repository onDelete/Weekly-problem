def solution(str_array):
    limit = len(str_array)
    all_possibility = []
    count = 0
    start = 0
    while True:
        switch = 0
        one_possible_num = 0
        while switch < 2 and count < limit:
            if str_array[count] == "X":
                switch += 1
                one_possible_num += 1
                count += 1
                if switch == 1:
                    start = count
            else:
                one_possible_num += 1
                count += 1
        if switch:
            all_possibility.append(one_possible_num - switch)
        else:
            all_possibility.append(0)
        if count == limit:
            break
        count = start
    max_num = max(all_possibility)
    return max_num


def text():
    print "OXO" + " " + "is" + " " + str(solution("OXO"))
    print "OXOOXOXXOOOXO" + " " "is" + " " + str(solution("OXOOXOXXOOOXO"))
    print "OOXOOOXOXO" + " " + "is" + " " + str(solution("OOXOOOXOXO"))
    print "OOOOOOOOOO" + " " + "is" + " " + str(solution("OOOOOOOOOO"))
    print "XXX" + " " + "is" + " " + str(solution("XXX"))


if __name__ == '__main__':
    text()
