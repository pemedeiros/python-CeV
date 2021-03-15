from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'teste.txt'
if not arqexiste(arq):
    criararquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair'])
    if resposta == 1:
        #Listar
        lerarquivo(arq)
        sleep(2)
    elif resposta == 2:
        #Cadastrar
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(2)
    elif resposta == 3:
        cabecalho('Saindo do sistema...Até mais.')
        break
    else:
        print('\033[031mERRO! Digite uma opção válida.\33[m')
        sleep(2)
