'''for c in range(0,4):
    n = int(input('Digite um valor:'))
    c += 1
nmrs = (n)
print(nmrs)'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o último número: '))
numeros = (n1,n2, n3, n4)
print(numeros)
vzs = numeros.count(9)
print(f'O número 9 apareceu {(vzs)} vezes')
print(f'O número 3 apareceu na {(numeros.index(3) + 1)}° posição')
c= 0
if n1 % 2 == 0:
    c +=1
if n2 % 2 == 0:
    c += 1
if n3 % 2 == 0:
    c+= 1
if n4 % 2 == 0:
    c += 1
print(f'Existem {c} números pares')