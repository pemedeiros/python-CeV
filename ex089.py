dados = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    opcao = input('Deseja continuar? [S/N]').upper()
    if opcao == 'N':
        break
print('-=' * 30)
print(f'{"N°":.<4}{"Nome":<10}{"Média":.<8}')
print('-=' * 30)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    escolha = int(input('Você quer ver as notas de qual aluno?(999 interrompe)'))
    if escolha == 999:
        print('ENCERRANDO...')
        break
    if escolha <= len(dados) - 1:
        print(f'Notas de {dados[escolha][0]} são {dados[escolha][1]} ')