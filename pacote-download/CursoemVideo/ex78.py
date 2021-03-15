lista = []
maior = 0
menor = 999999
posmaior = 0
posmenor = 0
for c in range(0, 5):
    lista.append(int(input('Digite o valor: ')))
    if lista[c] > maior:
        maior = lista[c]
        posmaior = c + 1
    if lista[c] < menor:
        menor = lista[c]
        posmenor = c + 1
print(lista)
print(f'O menor valor ({menor}) está na posição {posmenor} e o maior ({maior}) está an posição {posmaior}')
