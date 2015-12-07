'''
Modulo responsavel por funcoes simples e comuns a todos os algoritmos
'''

import matplotlib.pyplot as plt
import os
import math
from random import random

ROOT_DIR = '../plot_results'


def fill_array(n):  # Preenche o array com 'n' elementos aleatorio
    temp = [0.] * n  # Cria um vetor dimensao 'n' com zeros
    for i in range(n):
        # Assume um valor aleatorio, multiplica-o por 100 e define o sinal
        temp[i] = random() * 100 * (1 if random() < .5 else -1)
    return temp


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


def plot_graph(dim, time_bubble, dim2, time_quick, dim3, time_insert, dim4, time_shell,
               dim5, time_select, dim6, time_heap, dim7, time_merge):
    plt.figure()
    plt.plot(dim, time_bubble, dim2, time_quick, dim3, time_insert, dim4, time_shell,
             dim5, time_select, dim6, time_heap, dim7, time_merge)
    plt.legend(['BubbleSort', 'QuickSort', 'InsertionSort', 'ShellSort',
                'SelectionSort', 'HeapSort', 'MergeSort'], loc='best')
    plt.grid(True)
    plt.ylabel('Tempo Consumido(s)')
    plt.xlabel('Tamanho da entrada')
    plt.title('Tempo de CPU para todos algoritmos')
    plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9)
    plt.savefig(ROOT_DIR + '/all_algs.png',
                bbox_inches='tight', pad_inches=.5)
    plt.show()
