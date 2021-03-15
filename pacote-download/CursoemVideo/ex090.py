dados = {}
dados['nome'] = input('Digite o nome: ')
dados['media'] = float(input('Digite a média do aluno: '))
if dados['media'] >= 7.0:
    dados['situacao'] = 'Aprovado'
else:
    dados['situacao'] = 'Reprovado'
print(f'O nome é {dados["nome"]}')
print(f'A médoa é é {dados["media"]}')
print(f'A situação final é {dados["situacao"]}')