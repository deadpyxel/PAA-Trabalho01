# main.py
from general import *
from bubblesort import *
from quicksort import *
from insertionsort import *
from shellsort import *
from selectionsort import *
from heapsort import *
from mergesort import *

# cria o diretorio para armazenagem dos plots, por padrao o diretorio
# '../plot_results'
create_dir(ROOT_DIR)

n = 5000  # Quantos elementos no Array
num_it = 6  # Numero de iteracoes no teste
# list = fill_array(n)

# bubblesort(list)
# quicksort(list)
# insertionsort(list)
# shellsort(list)
# selectionsort(list)
# heapsort(list)
# mergesort(list)

cputime = [0.] * num_it  # inicializa o vetor vazio de dimensao num_it
dimvet = [0.] * num_it  # inicializa o vetor vazio de dimensao num_it

# Ira realizar num_it iteracoes de um mesmo algoritmo com diferentes dimensoes
for i in range(num_it):
    list = fill_array(n * (i + 1))
    dimvet[i] = len(list)
    cputime[i] = mergesort(list)  # Armazena o cputime para aquela execucao

# print dimvet, cputime
plot_graph(dimvet, cputime, 'Mergesort')
