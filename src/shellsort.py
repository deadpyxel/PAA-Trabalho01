import time


def shellsort(alist):
    inc = len(alist) / 2
    start = time.clock()
    while inc:
        for i in xrange(len(alist)):
            j = i
            temp = alist[i]
            while j >= inc and alist[j - inc] > temp:
                alist[j] = alist[j - inc]
                j -= inc
            alist[j] = temp
        inc = inc / 2 if inc / 2 else (0 if inc == 1 else 1)
    end = time.clock()
    cputime = end - start
    return cputime
