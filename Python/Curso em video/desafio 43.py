altura = float(input('Qual a sua altura? '))
peso = float(input('Quanto você pesa? '))

imc = peso/(altura**2)
print(imc)
if imc < 18.5:
    print(f'Cuidado! seu imc é de {imc:.2f} vc esta baixo do peso')
elif imc >= 18.5 and imc < 25:
    print(f'Parabens! seu imc é de {imc:.2f} vc esta no peso ideal')
elif imc >= 25 and imc < 30:
    print(f'Atencao! seu imc é de {imc:.2f} vc esta com sobre peso')
elif imc >= 30 and imc < 40:
    print(f'Cuidado! seu imc é de {imc:.2f} vc esta com obesidade')
else:
    print(f'Procure ajuda medica urgente! seu imc é de {imc:.2f} vc es com obesidade morbida')