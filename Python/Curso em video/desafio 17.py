import math

print('Vamos calcular a hipotenusa!')
cateto_oposto = float(input('Digite o valor do cateto oporto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

hipotenusa1 = (cateto_oposto**2 + cateto_adjacente **2)**(1/2)

print(f'A hipotenusa é {hipotenusa} e {hipotenusa1}')