par = []
impar = []
lista = []

for v in range(0, 4):
    lista.append(int(input('Digite um numero: ')))

    if lista[v] % 2 == 0:
        par.append(lista[v])
    if lista[v] % 2 != 0:
        impar.append(lista[v])
print(lista)
print(par)
print(impar)