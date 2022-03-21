salario = float(input('Digite seu salario: R$'))
aumento1 = (salario*10/100)+salario
aumento2 = (salario*15/100)+salario
if salario > 1250:
    print('Seu salario com um aumento de 10% ficará em R${:.2f}'.format(aumento1))
else:
    print('Seu salario com um aumento de 15% ficará em R${:.2f}'.format(aumento2))
print('--fim--')