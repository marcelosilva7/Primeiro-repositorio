print('vamos calcular sua idade em anos, meses e dias!')

d1 = int(input('Que dia vc nasceu? '))
m1 = int(input('Qual mes vc nasceu? '))
a1 = int(input('Que ano vc nasceu? '))

d2 = int(input('Qual dia atual? '))
m2 = int(input('Qual mes atual? '))
a2 = int(input('Qual ano atual? '))

ano = a2 - a1
print(f'Hoje vc tem {ano} anos, sua idade em meses é {(ano*12)+m2} meses e em dias é {(ano * 365)+(m2*30)} dias')
