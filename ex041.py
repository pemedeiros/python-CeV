from datetime import date

anos = int(input('Que ano você nasceu?'))
data_atual = date.today()
ano_atual = '{}'.format(data_atual.year)
ano_int = int(ano_atual)

if ano_int - anos <= 9:
    print('Sua categoria é\n=====MIRIM=====')
elif ano_int - anos <= 14:
    print('Sua categoria é\n=====INFANTIL=====')
elif ano_int - anos <= 19:
    print('Sua categoria é\n=====JUNIOR=====')
elif ano_int - anos <= 20:
    print('Sua categoria é\n=====SENIOR=====')
else:
    print('Sua categoria é\n=====MASTER=====')