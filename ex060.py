'''from math import factorial
n = int(input('Digite um número para saber seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''
n = int(input('Digite um número para saber seu fatorial: '))
c = n
f = 1
while c > 0:
    print(f'{c}', end = '')
    print('x' if c > 1 else '=', end = '')
    f *= c
    c -= 1
print(f)

