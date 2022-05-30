mes = ['janeiro', 'fevereiro', 'março', 'aril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

desejado = int(input('Digite o numero de mes desejado: '))

if desejado <= 12:
    print(f'Voce escolheu o mes {mes[desejado]}')
else:
    print('mes invalido')
