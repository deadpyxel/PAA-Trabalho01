import time


def insertionsort(alist):
    start = time.clock()
    for i in range(1, len(alist)):
        tmp = alist[i]
        k = i
        while k > 0 and tmp < alist[k - 1]:
            alist[k] = alist[k - 1]
            k -= 1
        alist[k] = tmp
    end = time.clock()
    cputime = end - start
    return cputime
