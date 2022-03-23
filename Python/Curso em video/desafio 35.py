print('Vamos saber se os valores digitados a seguir é um triangulo!')
ladoa = float(input('Digite o valor do lado: '))
ladob = float(input('Digite o valor do lado: '))
ladoc = float(input('Digite o valor do lado: '))

if ladob + ladoc > ladoa and ladoa + ladoc > ladob and ladoa + ladob > ladoc:
    print('É um triangulo!')
else:
    print('Não é um triangulo!')

print('--fim--')