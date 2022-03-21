import random
numero = random.randint(1, 5)
usuario = int(input('Escolha um numero inteiro de 1 a 5: '))

if numero == usuario:
    print('Parabens, vc acerto!!!')
else:
    print('Que pena, tente novamente!')
print('--fim--')
