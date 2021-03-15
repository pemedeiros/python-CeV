prim_ele = int(input('Digite o primeiro elemento da P.A: '))
razao = int(input('Digite a razão da P.A: '))
print('\n10 Primeiros Termos da PA com Razão {} (Iniciando em {}):'.format(razao, prim_ele))
print(prim_ele, end = '')
for c in range(0, 10):
    prim_ele += razao
    print(prim_ele, end = ' ')