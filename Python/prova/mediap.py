from random import randint

acumla = divisor = 0
for c in range(1, 6):
    aleatorio = randint(1, 10)
    vamo = aleatorio * c
    acumla += vamo
    divisor += c
    print(f'{aleatorio} * {c} = {vamo}')
print(f'A maedia ponderada é {acumla/divisor}')