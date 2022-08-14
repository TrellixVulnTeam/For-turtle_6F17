def do1(x):
    '''
    действие первое
    '''
    return x + 1


def do2(x):
    '''
    действие второе
    '''
    return x * 2


def ans(begin, end):
    if begin == end:
        return 1
    elif begin > end:
        return 0
    else:
        return ans(do1(begin), end) + ans(do2(begin), end)


def fool_ans(begin, process, end):
    return ans(begin, process) * ans(process, end)


start = 1
middle = 10
stop = 20
print(fool_ans(start, middle, stop))
