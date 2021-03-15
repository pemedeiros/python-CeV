teste = list()
teste.append('Pedro')
teste.append(18)
galera = list()
galera.append(teste[:])
teste[0] = 'Gustavo'
teste[1] = 40
galera.append(teste[:])
print(galera)
maisteste = [['Pedro', 18], ['Joao', 16], ['Jaqueline', 41]]
print(maisteste[0])
print(maisteste[1][1])
for p in maisteste:
    print(f'{p[0]} tem {p[1]} anos de idade')

teste1 = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    teste1.append(dado[:])
    dado.clear()
print(teste1)