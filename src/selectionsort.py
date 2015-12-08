# selectionsort.py
import time


def selectionsort(aList):
    start = time.clock()
    for i in range(len(aList)):
        least = i
        for k in range(i + 1, len(aList)):
            if aList[k] < aList[least]:
                least = k
            swap(aList, least, i)
    end = time.clock()
    cputime = end - start
    return cputime


def swap(A, x, y):
    A[x], A[y] = A[y], A[x]
