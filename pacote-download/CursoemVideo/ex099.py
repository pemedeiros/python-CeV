from time import sleep


def maior(*num):
    m = 0
    print('-' * 30)
    print('ANALISANDO OS VALORES PASSADOS')
    for n in num:
        print(n, end = ' ')
        sleep(0.5)
        if n > m:
            m = n
    print(f'\nForam informados {len(num)} números')
    sleep(1)
    print(f'O maior deles é {m}')
    sleep(1)
    print('-' * 30)


maior(2, 3, 1 )
maior(5)
maior(2,8)