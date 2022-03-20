print('Vamos Calcular Quantos litros de tinta sera necessario para pintar uma parede!\n ')
l = float(input('Qauntos metros de largura a parede tem? '))
a = float(input('Quantos metros de altura a parede tem? '))
m1 = l*a
m2 = (l*a)/2
print('Para pintar {:.2f} m2 é necessario {:.2f} litros de tinta!' .format(m1, m2))

