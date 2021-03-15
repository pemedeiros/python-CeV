from datetime import date

anos = int(input('Que ano você nasceu?'))

data_atual = date.today()
ano_atual = '{}'.format(data_atual.year)
ano_int = int(ano_atual)

if ano_int - anos == 18:
    print('É a hora de se alistar')
elif ano_int - anos >= 18:
    diferenca = (ano_int - anos) - 18
    print('Você já passou do tempo de alistamento fazem {} anos'.format(diferenca))
else:
    diferenca = 18 - (ano_int - anos)
    print('Você ainda vai se alistar, faltam {} anos para você se alistar'.format(diferenca))
