a = float(input('Digite um numero: '))
b = float(input('Digite um numero: '))
c = float(input('Digite um numero: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(f'O menor numero é o {menor}')
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O maior numero é o {maior}')

print('---FIM---')