# main.py
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
    cputime1[i] = bubblesort(list)
    cputime2[i] = quicksort(list)
    cputime3[i] = insertionsort(list)
    cputime4[i] = shellsort(list)
    cputime5[i] = selectionsort(list)
    cputime6[i] = heapsort(list)
    cputime7[i] = mergesort(list)
    print "tamanho de lista: {0}".format(len(list))

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
    list = fill_array(n * (i + 1))
    dimvet[i] = len(list)
    save_time(i, list)


plot_graph(dimvet, cputime1, dimvet, cputime2, dimvet, cputime3, dimvet,
           cputime4, dimvet, cputime5, dimvet, cputime6,  dimvet, cputime7)
