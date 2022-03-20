print('Hoje vamos calcular quanto ficaria seu salario com um aumento de 15%!!!')
s = int(input('Qaunto você ganha autalmente? '))
p = (s*15/100)
p1 = (s*15/100)+s
print('Você receberia com uma promoção de 15% um aumento de {:.0f}R$ que totaliza {:.0f}R$ !'.format(p, p1))
