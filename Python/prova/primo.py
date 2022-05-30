numero = int(input('Digite um numero: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\33[32m', end='')
        total += 1
    else:
        print('\33[33m', end='')
    print(f'{c} ', end='')
if total == 2:
    print(' numero é primo')
else:
    print(' numero nao é primo')

