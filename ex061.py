prim_ele = int(input('Digite o primeiro elemento da P.A: '))
razao = int(input('Digite a razão da P.A: '))
termo = prim_ele
cont = 1
while cont <= 10:
    print('{}->'.format(termo), end ='')
    termo += razao
    cont += 1
print('FIM')