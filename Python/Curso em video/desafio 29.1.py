velocidade = int(input('Digite a velocidade do seu carro em km/h: '))
multa = (velocidade -80) * 7

if velocidade > 80:
    print(f'Parabens vc foi multado por ultrapassar o limete de 80km/h \n'
          f'A multa vai custar R${multa:.2f}')
else:
    print('Parabens vc esta respeitando as leis de transito!')

print('--fim--')
