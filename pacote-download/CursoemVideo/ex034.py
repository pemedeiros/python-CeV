sal = float(input('Digite seu salário: '))
if sal > 1250.0:
    nsal = sal * 1.10
    print('Seu novo salário é R${:.2f}'.format(nsal))
else:
    nsal = sal * 1.15
    print('Seu novo salário é R${:.2f}'.format(nsal))
