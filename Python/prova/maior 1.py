from random import randint
cont = menor = maior = 0

for c in range(1, 6):
    aleatorio = randint(0, 10)
    cont += 1
    if cont == 1:
        menor = maior = aleatorio
    elif aleatorio < menor:
        menor = aleatorio
    elif aleatorio > maior:
        maior = aleatorio
    print(f'{aleatorio} ', end='')
print(f'Maior {maior}, menor {menor}')
