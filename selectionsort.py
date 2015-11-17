#=======================================================================
#  Author: Isai Damier
#  Title: Selection Sort
#  Project: geekviewpoint
#  Package: algorithm.sorting
#
#  Statement:
#  Given a disordered list of integers (or any other items),
#  rearrange the integers in natural order.
#
#  Sample Input: [18,5,3,1,19,6,0,7,4,2,5]
#  Sample Output: [0,1,2,3,4,5,5,6,7,18,19]
#
#  Time Complexity of Solution:
#  Best O(n^2); Average O(n^2); Worst O(n^2).
#
#  Approach:
#  Selection sort is a step up from insertion sort from a memory
#  viewpoint. It only swaps elements that need to be swapped. In terms
#  of time complexity, however, insertion sort is better.
#=======================================================================


def selectionsort(aList):
    for i in range(len(aList)):
        least = i
        for k in range(i + 1, len(aList)):
            if aList[k] < aList[least]:
                least = k

        swap(aList, least, i)


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
