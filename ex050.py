t = 0
np = 0
for c in range(0, 6):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        t += n1
        np += 1
if np == 0:
     print('Você não digitou nenhum número par, portanto, o seu total é 0.')
elif np == 1:
    print('Você digitou {} número par. O seu total é {}.'.format(np, t))
else:
    print('Você digitou {} números pares. A soma total deles é {}.'.format(np, t))
