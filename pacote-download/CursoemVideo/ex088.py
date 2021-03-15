from random import randint
from time import sleep
jogo = []
lista = []

tot = 1
qtd = int(input('Quantos jogos você quer fazer? '))
while tot <= qtd:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.append(sorted(jogo[:]))
    jogo.clear()
    tot += 1
for i, l in enumerate(lista):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
