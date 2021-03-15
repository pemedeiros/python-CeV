n = 1
while n != 0:
    sexo = str(input('Digite seu sexo(M/F): ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Entrada inválida, digite novamente')
