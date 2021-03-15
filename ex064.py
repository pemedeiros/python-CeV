n = 1
soma = 0
while n != 0:
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
    else:
        print('Você digitou 999 e a soma de todos foi {}'.format(soma))