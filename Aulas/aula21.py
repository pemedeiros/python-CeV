'''def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return  f


n = int(input('Digite um número:'))
print(f'O fatoria de {n} é {fatorial(n)}')
f1 = fatorial(4)
f2 = fatorial(5)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')'''


def parOuImpar(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número'))
if parOuImpar(num):
    print('É par')
else:
    print('Não é par')