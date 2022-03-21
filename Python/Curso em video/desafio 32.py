ano = int(input('Digite um ano e vamos saber se ele é bissesto: '))
bissesto = ano % 4

if bissesto == 0:
    print('Ano bissesto')
else:
    print('nao bissesto')
print('--fim--')
