import random
usu = int(input('Digite um número entre 0 e 5:'))
lista = [0, 1, 2, 3, 4, 5]
escolha = random.choice(lista)
print('O número escolhido pelo computador foi {}'.format(escolha))
if usu == escolha:
    print('Você ganhou, parabéns!')
else:
    print('O computador ganhou')

