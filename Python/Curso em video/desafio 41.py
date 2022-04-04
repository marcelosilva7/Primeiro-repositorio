idade = int(input('Digite sua idade: '))

if idade < 9:
    print('Categoria Mirim')
elif idade < 14 and idade >= 9:
    print('Categoria Infantil')
elif idade >= 14 and idade < 19:
    print('Categoria Junior')
elif idade >= 19 and idade < 20:
    print('Categoria sênior')
else:
    print('Categoria Master')
