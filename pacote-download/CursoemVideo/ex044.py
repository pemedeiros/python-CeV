val_ini = float(input('Qual o valor do produto? R$'))
print('========== MÉTODO DE PAGAMENTO ==========')
print('====== 1. À vista(Dinheiro/Cheque) ======')
print('====== 2. À vista(Cartão) ===============')
print('====== 3. Até 2x(Cartão) ================')
print('====== 4. 3x ou mais(Cartão) ============')
opcao = int(input('Insira a opção desejada, sabendo que:'
                  '\n===== 1. Tem 10% de desconto. ====='
                  '\n===== 2.Tem 5% de desconto. ====== '
                  '\n===== 3. Preço normal. ============'
                  '\n===== 4. 20% de juros. ============'
                  '\nOpção: '))
if opcao == 1:
    val_fim = val_ini * 0.9
    print('O valor final foi de R${:.2f}'.format(val_fim))
elif opcao == 2:
    val_fim = val_ini * 0.95
    print('O valor final foi de R${:.2f}'.format(val_fim))
elif opcao == 3:
    val_fim = val_ini
    print('O valor final foi de R${:.2f}'.format(val_fim))
elif opcao == 4:
    val_fim = val_ini * 1.20
    print('O valor final foi de R${:.2f}'.format(val_fim))
else:
    print('A opção digitada não existe.')
