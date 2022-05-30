from random import randint
cont = 0
menor = 0
maior = 0
for c in range(1, 9):
    aleatorio = randint(0, 30)
    cont += 1
    print(f'{aleatorio}, ', end='')
    if cont == 1:
        maior = menor = aleatorio
    if aleatorio < menor:
        menor = aleatorio
    if aleatorio > maior:
        maior = aleatorio
print(f'o maior numero é o {maior} e o menor é o {menor}')

