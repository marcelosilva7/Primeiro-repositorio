aniversairo = input('Digite a data de nascimento no formado __/__/____ : ')

dia = int(aniversairo[:2])
mes = int(aniversairo[3:5])

if 20 <= dia <= 31 and mes == 3 or 1 <= dia <= 20 and mes == 4:
    print('aries')
elif 21 <= dia <= 30 and mes == 4 or 1 <= dia <= 20 and mes == 5:
    print('touro')
elif 21 <= dia <= 31 and mes == 5 or 1 <= dia <= 20 and mes == 6:
    print('gemeos')
elif 21 <= dia <= 30 and mes == 6 or 1 <= dia <= 21 and mes == 7:
    print('cancer')
elif 22 <= dia <= 31 and mes == 7 or 1 <= dia <= 22 and mes == 8:
    print('leao')


