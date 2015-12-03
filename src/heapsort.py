import time


def heapsort(alist):
    start = time.clock()
    # convert alist to heap
    length = len(alist) - 1
    leastParent = length / 2
    for i in range(leastParent, -1, -1):
        movedown(alist, i, length)

    # flatten heap into sorted array
    for i in range(length, 0, -1):
        if alist[0] > alist[i]:
            swap(alist, 0, i)
            movedown(alist, 0, i - 1)
    end = time.clock()
    cputime = end - start
    return cputime


def movedown(alist, first, last):
    largest = 2 * first + 1
    while largest <= last:
            # right child exists and is larger than left child
        if (largest < last) and (alist[largest] < alist[largest + 1]):
            largest += 1

        # right child is larger than parent
        if alist[largest] > alist[first]:
            swap(alist, largest, first)
            # move down to largest child
            first = largest
            largest = 2 * first + 1
        else:
            return  # force exit


def swap(A, x, y):
    A[x], A[y] = A[y], A[x]
