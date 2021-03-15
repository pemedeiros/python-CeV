valcasa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o valor do seu salário? R$ '))
anos = int(input('Em quantos anos você vai pagar?'))
meses = anos * 12
valprest = valcasa / meses
if valprest >= sal * 0.3:
    print('Seu empréstimo foi aprovado e o valor da prestação é de R${:.2f}'.format(valprest))
else:
    print('O empréstimo foi negado, o valor excede 30% do seu salário')
