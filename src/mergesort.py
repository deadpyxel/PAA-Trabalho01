# mergesort.py
import time


def mergesort(aList):
    start = time.clock()
    _mergesort(aList, 0, len(aList) - 1)
    end = time.clock()
    cputime = end - start
    return cputime


def _mergesort(aList, first, last):
    # quebra o problema em partes menores
    mid = (first + last) / 2
    if first < last:
        _mergesort(aList, first, mid)
        _mergesort(aList, mid + 1, last)

    # junta as partes ordenadas para chegar a solucao do problema orginal
    a, f, l = 0, first, mid + 1
    tmp = [None] * (last - first + 1)

    while f <= mid and l <= last:
        if aList[f] < aList[l]:
            tmp[a] = aList[f]
            f += 1
        else:
            tmp[a] = aList[l]
            l += 1
        a += 1

    if f <= mid:
        tmp[a:] = aList[f:mid + 1]

    if l <= last:
        tmp[a:] = aList[l:last + 1]

    a = 0
    while first <= last:
        aList[first] = tmp[a]
        first += 1
        a += 1
