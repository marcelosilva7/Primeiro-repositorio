velocidade = int(input('Digite a velocidade do seu carro em km/h: '))
multa = velocidade * 7

if velocidade > 80:
    print(f'Parabens vc foi multado, a multa vai custar R${multa}')
else:
    print('Parabens vc esta respeitando as leis de transito!')
print('--fim--')
