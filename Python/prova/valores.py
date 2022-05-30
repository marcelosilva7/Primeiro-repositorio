from random import randint
menor = maior = cont = 0
for c in range(1, 6):
    aleatorio = randint(1, 10)
    cont += 1
    if cont == 1:
        maior = menor = aleatorio
    if aleatorio < menor:
        menor = aleatorio
    if aleatorio > maior:
        maior = aleatorio
    print(f'{aleatorio} ', end='')
print(f'o menor numero é {menor} e o maior é {maior}')

