print('Vamos verificar se os 3 valores digitados a seguir conseguem formar um triangulo!')

lado_a = float(input('Digite o valor do lado a: '))
lado_b = float(input('Digite o valor do lado b: '))
lado_c = float(input('Digite o valor do lado c: '))

if (lado_b - lado_c) < (lado_a + lado_b < lado_c):
    print('Não é um triangulo')
elif (lado_a - lado_c) < (lado_a + lado_c < lado_b):
    print('Não é um triangulo')
elif (lado_a - lado_b) < (lado_b + lado_c < lado_a):
    print('Não é um triangulo')
elif (lado_a == lado_b):
    print('É um triangulo equilatero')
elif (lado_a == lado_c):
    print('É um triangulo equilatero')
elif (lado_b == lado_c):
    print('É um triangulo isoceles')
elif (lado_a == lado_b):
    print('É um triangulo isoceles')
elif (lado_a == lado_c):
    print('É um triangulo isoceles')
else:
    print('é um triangulo escaleno ')