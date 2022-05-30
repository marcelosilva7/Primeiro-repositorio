numero = int(input('Digite um numero: '))
cont = 1
for c in range(1, numero + 1):
    print(f'{c}x ', end='')
    cont *= c
print(f'= {cont}', end='')