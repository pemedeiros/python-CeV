n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O primeiro número é maior')
elif n2 > n1 and n2 > n3:
    print('O segundo número é maior')
elif n1 == n2 == n3:
    print('Todos são iguais')
else:
    print('O terceiro número é o maior')