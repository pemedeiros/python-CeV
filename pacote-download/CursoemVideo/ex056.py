total = 0
maior = 0
for c in range(1, 5):
    print('========== {}° PESSOA ============'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo(M ou F): ')
    total += idade
    media = total / 4
    if sexo == 'M':
        if c == 1:
            maior = idade
        if c != 1 and idade > maior:
            maior = idade
print('A média de idade desse grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos'.format( maior))
