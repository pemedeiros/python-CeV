import random
n = 1
while n != 0:
    usu = int(input('Digite um número entre 0 e 10:'))
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    escolha = random.choice(lista)
    n += 1
    print('O número escolhido pelo computador foi {}'.format(escolha))
    if usu == escolha:
        print('Você ganhou, parabéns!')
        print('Você precisou de {} chances para acertar'.format(n - 1))
    else:
        print('O computador ganhou')

