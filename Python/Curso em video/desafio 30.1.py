numero = int(input('Digite um numero e vamos descobrir se ele é par ou impar: '))

par = numero % 2

if par == 0:
    print(f'O {numero} é par!')
else:
    print(f'O {numero} é impar!')

print('--fim--')
