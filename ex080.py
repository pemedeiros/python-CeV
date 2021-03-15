lista = []
for c in range(0, 5):
    val = int(input('Digite o valor: '))
    if c == 0 or val > lista[-1]:
        lista.append(val)
        print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if val <= lista[pos]:
                lista.insert(pos, val)
                print(f'Valor adicionado na posição {pos}° da lista')
                break
            pos +=1
print(lista)