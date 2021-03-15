from random import randint
n = 1
while n != 0:
    usu = int(input('Digite um número: '))
    poi = input('Escolha par ou ímpar[P/I]: ').upper()
    escolha = randint(1, 11)

    print('O número escolhido pelo computador foi {}'.format(escolha))
    if poi == 'P':
        if (usu + escolha) % 2 == 0:
            result = usu + escolha
            print(f'Você escolheu {usu}, o computador escolheu {escolha}, portanto a soma é {result} então\n VOCÊ GANHOU')
            n += 1
        else:
            result = usu + escolha
            print(f'Você escolheu {usu}, o computador escolheu {escolha}, portanto a soma é {result} então\n VOCÊ PERDEU')
            print(f'Você ganhou {n - 1} vezes!')
    if poi == 'I':
        if (usu + escolha) % 2 != 0:
            result = usu + escolha
            print(f'Você escolheu {usu}, o computador escolheu {escolha}, portanto a soma é {result} então\n VOCÊ GANHOU')
            n += 1
        else:
            result = usu + escolha
            print(f'Você escolheu {usu}, o computador escolheu {escolha}, portanto a soma é {result} então\n VOCÊ PERDEU')
            print(f'Você ganhou {n - 1} vezes!')
