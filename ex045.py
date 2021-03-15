import random
usu = input('Escolha pedra, papel ou tesoura: ')
lista = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(lista)

if pc == 'Pedra' and usu == 'Pedra':
    print('Empatou')
elif pc == 'Pedra' and usu == 'Tesoura':
    print('O computador ganhou, você escolheu {} e o computador escolheu {}'.format(usu, pc))
elif pc == 'Pedra' and usu == 'Papel':
    print('Você ganhou, você escolheu {} e o computador escolheu {}'.format(usu, pc))
elif pc == 'Papel' and usu == 'Papel':
    print('Empatou')
elif pc == 'Papel' and usu == 'Tesoura':
    print('Você ganhou, você escolheu {} e o computador escolheu {}'.format(usu, pc))
elif pc == 'Tesoura' and usu == 'Tesoura':
        print('Empatou')
elif pc == 'Tesoura' and usu == 'Papel':
    print('O computador ganhou, você escolheu {} e o computador escolheu {}'.format(usu, pc))

