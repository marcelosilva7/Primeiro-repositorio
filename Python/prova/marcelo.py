from math import factorial

numero = int(input('insira um numero: '))
h = 0
dividento = 1

for i in range(1,numero+1):
    h += 1 /dividento
    dividento +=1
print(h)