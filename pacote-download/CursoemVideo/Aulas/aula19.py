'''teste = {}
teste['nome'] = 'Pedro'
teste['idade'] = 18
teste['sexo'] = 'M'
print(teste)
del teste['idade']
print(teste)
filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items)

for k, v in filme.items():
    print(f'O {k} é {v}')'''

'''pessoas = {'nome': 'Pedro', 'sexo': 'M', 'idade': 18}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''
'''brasil = []
estado1 = {'uf': 'rio de janeiro', 'sigla': 'rj'}
estado2 = {'uf': 'são paulo', 'sigla': 'sp'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil[1]['uf'])'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['silga'] = str(input('Siga do estado: '))
    brasil.append(estado.copy())

