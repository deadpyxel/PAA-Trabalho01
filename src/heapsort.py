import time


def heapsort(alist):
    start = time.clock()
    # converte alist para heap
    length = len(alist) - 1
    leastParent = length / 2
    for i in range(leastParent, -1, -1):
        movedown(alist, i, length)

    # converte o heap em um array ordenado
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
        # filho direito e maior que o filho esquerdo
        if (largest < last) and (alist[largest] < alist[largest + 1]):
            largest += 1

        # filho direito e maior que o pai
        if alist[largest] > alist[first]:
            swap(alist, largest, first)
            # move pra baixo o maior filho
            first = largest
            largest = 2 * first + 1
        else:
            return  # forca saida


def swap(A, x, y):
    A[x], A[y] = A[y], A[x]
