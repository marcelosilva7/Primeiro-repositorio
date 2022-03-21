numero = int(input('Digite um numero e vamos descobrir se ele é par ou impar: '))

par = numero % 2

if par == 0:
    print('Esse numero é par!')
else:
    print('Esse numero é impar!')
print('--fim--')