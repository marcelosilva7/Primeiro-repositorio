#estudar sobre a evdnc k21

altura = float(input('Digite sua altura: '))
sexo = input('Qua seu sexo? M ou F? ').upper().strip()

if sexo == 'M':
    print(f'O peso ideal do sexo masculino é {(72.7*altura)-58:.2f}')
else:
    print(f'O peso ideal para o sexo feminino é {(62.1*altura)-44.7:.2f}')
print('--fim--')
