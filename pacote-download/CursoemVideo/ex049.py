from time import sleep
for c in range(0, 2):
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    s = num1 * num2
    print('A entre {} e {} é: {}'.format(num1, num2, s))
    sleep(2)
