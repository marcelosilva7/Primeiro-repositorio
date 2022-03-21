print('Digite um numero de 0 a 9999')
numero = int(input('Digite um numero: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Numero escolhido foi {numero}')
print(f'Unidade {unidade}')
print(f'dezena {dezena}')
print(f'centena {centena}')
print(f'milhar {milhar}')