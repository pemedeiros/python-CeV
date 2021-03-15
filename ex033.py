n1 = int(input('Insira o primeiro número:'))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))
if n1 > n2 and n2 < n3 and n1 > n3:
    print('O maior número é o {} e o menor é o {}.'.format(n1, n2))
if n1 > n2 and n2 > n3 and n1 > n3:
    print('O maior número é o {} e o menor é o {}.'.format(n1, n3))
if n2 > n1 and n1 > n3 and n2 > n3:
    print('O maior número é o {} e o menor é o {}.'.format(n2, n3))
if n2 > n3 and n1 < n3 and n2 > n1:
    print('O maior número é o {} e o menor é o {}.'.format(n2, n1))
if n3 > n1 and n2 < n1 and n3 > n2:
    print('O maior número é o {} e o menor é o {}.'.format(n3, n2))
if n3 > n1 and n2 > n1 and n3 > n1:
    print('O maior número é o {} e o menor é o {}.'.format(n3, n1))
