#=======================================================================
#  Author: Isai Damier
#  Title: Insertionsort
#  Project: geekviewpoint
#  Package: algorithms
#
#  Statement:
#  Given a disordered list of integers (or any other items),
#  rearrange the integers in natural order.
#
#  Sample Input: [8,5,3,1,9,6,0,7,4,2,5]
#  Sample Output: [0,1,2,3,4,5,5,6,7,8,9]
#
#  Time Complexity of Solution:
#  Best O(n); Average O(n^2); Worst O(n^2).
#
#  Approach:
#  Insertion sort is good for collections that are very small
#  or nearly sorted. Otherwise it's not a good sorting algorithm:
#  it moves data around too much. Each time an insertion is made,
#  all elements in a greater position are shifted.
#=======================================================================


def insertionsort(alist):
    for i in range(1, len(alist)):
        tmp = alist[i]
        k = i
        while k > 0 and tmp < alist[k - 1]:
            alist[k] = alist[k - 1]
            k -= 1
        alist[k] = tmp
