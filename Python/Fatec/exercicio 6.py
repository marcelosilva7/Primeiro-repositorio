print('Vamos calcular as prestações atrasadas')
v = float(input('Qual o valor da prestação? R$'))
p = int(input('Digite quantas prestações estão em atraso! '))
m = (v*10/100)
valor = (p*m)+(v*p)
final = valor-(valor*10/100)
print(f'O valor de acrescimo de cada parcela em atraso é {m:.2f} R$ que no total é {valor:.2f} R$ com o desconto de 10% fica {final:.2f} R$')