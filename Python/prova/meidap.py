from random import randint
cont = dividorp = 0
for c in range(1, 5):
    aleatorio = randint(1,10)
    somap = aleatorio * c
    cont += somap
    dividorp += c
    print(f'{aleatorio} x {c} = {somap}')
print(f'Total {cont} / {dividorp} = {cont/dividorp}')