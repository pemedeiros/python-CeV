from datetime import date
data_atual = date.today()
ano_atual = '{}'.format(data_atual.year)
ano_int = int(ano_atual)
trabalhador = {}
trabalhador['nome'] = input('Nome: ')
trabalhador['idade'] = ano_int - int(input('Ano de nascimento: '))
trabalhador['ctps'] = int(input('Carteira de Trabalho: (0 não tem)'))
if trabalhador['ctps'] == 0:
    print('Dados...')
    for k, v in trabalhador.items():
        print(f'O {k} tem valor {v}', end=' ')
        print()
else:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$ '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + 35
    for k, v in trabalhador.items():
        print(f'O {k} tem valor {v}', end=' ')
        print()

