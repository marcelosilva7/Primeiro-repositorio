distancia = int(input('Digite a distancia da sua viagem: '))
valor1 = distancia*0.5
valor2 = distancia*0.45

if distancia <= 200:
    print('O preço dessa viagem vai custar R${:.2f}'.format(valor1))
else:
    print('O preço dessa viagem vai custar R${:.2f}'.format(valor2))

print('--fim--')

