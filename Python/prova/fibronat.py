numero = int(input('Digite um numero de fibro: '))

t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end='')
cont = 3
while cont <= numero:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM', end='')