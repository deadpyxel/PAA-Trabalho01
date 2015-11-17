def bubblesort(alist):
    length = len(alist) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if alist[i] > alist[i + 1]:
                sorted = False
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
