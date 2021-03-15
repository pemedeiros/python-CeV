from random import randint
from time import sleep


def sorteia():
    print('SORTEANDO VALORES')
    for c in range(0, 5):
        numeros.append(randint(1, 10))
        print(numeros[c], end = ' ')
        sleep(0.5)


def somapar(numeros):
    s = 0
    for n in numeros:
        if n % 2 == 0:
            s += n
    print(f'\nSomando os valores pares de  {numeros} temos {s}')


numeros = []
sorteia()
somapar(numeros)