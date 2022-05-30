numero = int(input('Dgitie um numero para calcular fatorial: '))
fatorial = 1
for c in range(1, numero +1):
    print(f'{c}x ', end='')
    fatorial *= c
print(f'= {fatorial}')