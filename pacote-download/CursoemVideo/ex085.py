total = []
par = []
impar = []
for c in range(0,7):
    total.append(int(input('Digite o valor: ')))
    if total[c] % 2 == 0:
        par.append(total[c])
    else:
        impar.append(total[c])
print(f'A lista dos 7 valores foi {total}'
      f'\nA dos pares foi {sorted(par)}'
      f'\nA dos impares foi {sorted(impar)}')