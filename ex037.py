num = int(input('Insira um valor inteiro:'))
print('========== BASE PARA CONVERSÃO ==========')
print('============= 1. Binário ================')
print('============= 2. Octal ==================')
print('============= 3. Hexadecimal ============')
opcao = int(input('Qual a opção?'))
if opcao == 1:
    print('O valor {} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O valor {} convertido para OCATL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O valor {} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')