'''
Modulo responsavel por funcoes simples e comuns a todos os algoritmos
'''

import matplotlib.pyplot as plt
import os
from random import random

ROOT_DIR = 'plot_results'


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


'''
def calc_time():
    command = 'echo test'# + options
    process = os.popen(command)
    results = str(process.read())
    return results
'''


def plot_graph(dim, time, sortname):
    plt.figure()
    plt.plot(dim, time)
    plt.legend(['T(n)'], loc='best')
    plt.grid(True)
    plt.ylabel('Tempo Consumido')
    plt.xlabel('Tamanho da entrada')
    plt.title('Tempo de CPU para ' + sortname)
    plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9)
    plt.savefig(ROOT_DIR + '/' + sortname + '.png',
                bbox_inches='tight', pad_inches=.5)
    plt.show()
