def shellsort(items):
    inc = len(items) / 2
    while inc:
        for i in xrange(len(items)):
            j = i
            temp = items[i]
            while j >= inc and items[j - inc] > temp:
                items[j] = items[j - inc]
                j -= inc
            items[j] = temp
        inc = inc / 2 if inc / 2 else (0 if inc == 1 else 1)
