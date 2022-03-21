distancia = int(input('Digite a distancia da sua viagem: '))
valor1 = distancia*0.5
valor2 = distancia*0.45
if distancia > 200:
    print('O preço dessa viagem vai custar R${}'.format(valor2))
else:
    print('O preço dessa viagem vai custar R${}'.format(valor1))
print('--fim--')