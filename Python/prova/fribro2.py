numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
print(f'{numero1} -> {numero2} -> ', end='')
for c in range(1, 21):
    t3 = numero1 + numero2
    print(f'{t3} -> ', end='')
    numero1 = numero2
    numero2 = t3
print('fim')