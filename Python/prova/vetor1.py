numeros = []
menor = maior = 0
for v in range(0,10):
    numeros.append(int(input('Digite um numero: ')))
    if v == 0:
        menor = maior = numeros[v]
    else:
        if numeros[v] > maior:
            maior = numeros[v]
        if numeros[v] < menor:
            menor = numeros[v]
print(f'maior numero {maior} e menor numero {menor}')





