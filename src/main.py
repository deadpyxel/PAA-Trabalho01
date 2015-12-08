# main.py
'''
Modulo principal, onde ocorrem as execucoes
'''

import time
from general import *
from bubblesort import *
from quicksort import *
from insertionsort import *
from shellsort import *
from selectionsort import *
from heapsort import *
from mergesort import *


# Funcao para executar as chamadas
def save_time(i, list):
    start = time.clock()
    time_bubble[i] = bubblesort(list[0])		# Tempo do bubblesort
    time_quick[i] = quicksort(list[1])		# Tempo do quicksort
    time_insert[i] = insertionsort(list[2])  # Tempo do insertionsort
    time_shell[i] = shellsort(list[3])		# Tempo do shellsort
    time_select[i] = selectionsort(list[4])  # Tempo do selectionsort
    time_heap[i] = heapsort(list[5])		# Tempo do heapsort
    time_merge[i] = mergesort(list[6])		# Tempo do merge
    end = time.clock()
    actualtime = end - start
    print "Tamanho de lista: {0} | Tempo para a execucao de todos algoritmos: {1}s".format(len(list[0]), actualtime)
    return  # forca a saida


# Funcao para salvar o tempo de execucao em arquivos legiveis
def save_all_times():
    write_file(DATA_DIR + '/cputime_bubble.txt', time_bubble)
    write_file(DATA_DIR + '/cputime_quick.txt', time_quick)
    write_file(DATA_DIR + '/cputime_insertion.txt', time_insert)
    write_file(DATA_DIR + '/cputime_shell.txt', time_shell)
    write_file(DATA_DIR + '/cputime_selection.txt', time_select)
    write_file(DATA_DIR + '/cputime_heap.txt', time_heap)
    write_file(DATA_DIR + '/cputime_merge.txt', time_merge)
    return  # forca a saida

# cria o diretorio para armazenagem dos plots, por padrao o diretorio
# '../plot_results'
create_dir(PLOT_DIR)
create_dir(DATA_DIR)

n = 5000  # Quantos elementos no Array
num_it = 6  # Numero de iteracoes no teste

# Inicializa os vetores para armazenamento do tempo de execucao
time_bubble, time_quick, time_insert, time_shell, time_select, time_heap, time_merge = (
    ([0.] * num_it) for i in range(7))
dimvet = ([0.] * num_it)  # inicializa o vetor vazio de dimensao num_it

# Ira realizar num_it iteracoes de um mesmo algoritmo com diferentes dimensoes
for i in range(num_it):
        # Array de listas para ordenacao
    list1, list2, list3, list4, list5, list6, list7 = (
        (fill_array(n * (i + 1))) for k in range(7))
    list_list = [list1, list2, list3, list4, list5, list5, list6, list7]
    dimvet[i] = len(list1)
    save_time(i, list_list)

save_all_times()  # Salva o tempo de execucao dos algoritmos

plot_graph(dimvet, time_bubble, dimvet, time_quick, dimvet, time_insert, dimvet,
           time_shell, dimvet, time_select, dimvet, time_heap,  dimvet, time_merge)
