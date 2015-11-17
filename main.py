from general import *
from bubblesort import *
from quicksort import *
from insertionsort import *
from shellsort import *
from selectionsort import *
from heapsort import *
from mergesort import *

create_dir(ROOT_DIR)

n = 1000  # Quantos elementos no Array
list = fill_array(n)
# bubblesort(list)
# quicksort(list)
# insertionsort(list)
# shellsort(list)
# selectionsort(list)
heapsort(list)
# mergesort(list)
# print list

#plot_graph(list, list, 'test2')
