# main.py
'''
Modulo principal, onde ocorrem as execucoes
'''

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
    cputime1[i] = bubblesort(list[0])		# Tempo do bubblesort
    cputime2[i] = quicksort(list[1])		# Tempo do quicksort
    cputime3[i] = insertionsort(list[2])  # Tempo do insertionsort
    cputime4[i] = shellsort(list[3])		# Tempo do shellsort
    cputime5[i] = selectionsort(list[4])  # Tempo do selectionsort
    cputime6[i] = heapsort(list[5])		# Tempo do heapsort
    cputime7[i] = mergesort(list[6])		# Tempo do merge
    print "Tamanho de lista: {0}".format(len(list[0]))

# cria o diretorio para armazenagem dos plots, por padrao o diretorio
# '../plot_results'
create_dir(ROOT_DIR)

n = 5000  # Quantos elementos no Array
num_it = 6  # Numero de iteracoes no teste

# Inicializa os vetores para armazenamento do tempo de execucao
cputime1, cputime2, cputime3, cputime4, cputime5, cputime6, cputime7 = (
    ([0.] * num_it) for i in range(7))
dimvet = [0.] * num_it  # inicializa o vetor vazio de dimensao num_it

# Ira realizar num_it iteracoes de um mesmo algoritmo com diferentes dimensoes
for i in range(num_it):
    list1, list2, list3, list4, list5, list6, list7 = (
        (fill_array(n * (i + 1))) for i in range(7))
    list_list = [list1, list2, list3, list4, list5, list5, list6, list7]
    dimvet[i] = len(list_list[0])
    save_time(i, list_list)


plot_graph(dimvet, cputime1, dimvet, cputime2, dimvet, cputime3, dimvet,
           cputime4, dimvet, cputime5, dimvet, cputime6,  dimvet, cputime7)
