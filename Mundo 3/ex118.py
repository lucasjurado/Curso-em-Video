from random import randint
from time import sleep
def sorteio ():
    print(f'Sorteando 5 valores da lista:', end=' ')
    for c in range(0,5):
        n = randint(1,10)
        numeros.append(n)
        sleep(0.5)
        print(n, end=' ')
    print('Pronto!')

def somapar():
    """
    :param c: todos numeros
    :param x: blabla
    :return:
    """
    for c in numeros:
        if c % 2 == 0:
            num_par.append(c)
    print(f'Somando os valores pares de {numeros}, temos {sum(num_par)}')


numeros = []
num_par = []

sorteio()
somapar()

help(somapar)

