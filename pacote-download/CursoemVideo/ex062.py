prim_ele = int(input('Digite o primeiro elemento da P.A: '))
razao = int(input('Digite a razão da P.A: '))
termo = prim_ele
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}->'.format(termo), end ='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quer ver mais quantos termos?'))
print('FIM')