matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = tercolu = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f'Digite um valor para {l + 1, c + 1}: '))
        if matriz[l] [c] % 2 == 0:
            somapar += matriz[l] [c]
        if c == 2:
            tercolu += matriz[l] [2]
        if  l == 1:
            if matriz[1] [c] > maior:
                maior = matriz[1] [c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end = '')
    print()
print(f'A soma dos pares é {somapar}'
      f'\nA soma dos valores da terceira coluna é {tercolu}'
      f'\nO maior valor da segunda linha é {maior}')