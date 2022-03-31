numero = int(input('Digite um numero inteiro: '))
print('Escolha as bases para comversão: ')
print('[ 1 ] converter para binario')
print('[ 2 ] converter para octal')
print('[ 3 ] converter para hexadecimal')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print(f'o numero {numero} convertido para binario é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'o numero {numero} convertido em octal é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'o numero {numero} convertido em hexadecimal é {hex(numero)[2:]}')
else:
    print('opção invalida')