numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite outro numero: '))

if numero1 > numero2:
    maior = numero1
    print(f'o maior numero é o {maior}')
elif numero2 > numero1:
    maior = numero2
    print(f'o maior numero é o {maior}')
elif numero1 == numero2:
    print('os numeros são iguais')


