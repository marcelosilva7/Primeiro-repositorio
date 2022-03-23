import random
import time
numero = random.randint(1, 5)
print('-=-' * 20)
print('Tente adivinhar.........')
print('-=-' * 20)
usuario = int(input('Escolha um numero inteiro de 1 a 5: '))
print('-=-' * 20)
print('Processando.......')
time.sleep(3)
if numero == usuario:
    print('Parabens, vc acerto!!!')
else:
    print(f'Que pena, pensei no numero {numero}, e não no {usuario}, tente novamente!')

print('--fim--')
time.