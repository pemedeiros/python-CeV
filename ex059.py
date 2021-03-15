n = 1
while n != 0:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print('============== MENU ================')
    print('=========== [1] Somar ==============')
    print('=========== [2] Multiplicar ========')
    print('=========== [3] Maior ==============')
    print('=========== [4] Novos números ===== ')
    print('=========== [5] Sair ===============')
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        if n1 < n2:
            print('O maior número é {}'.format(n2))
    elif opcao == 4:
        print('Me informe os números novamente')
    else :
        exit()