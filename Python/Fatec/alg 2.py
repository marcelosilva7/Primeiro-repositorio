print('pronto de gasolina, vamos abastercer!')

combustivel = input('Deseja abastecer com Gasolina(G) ou Alcool(A)? ').upper().strip()
litros = float(input('Quantos litros deseja abastercer? '))

if combustivel == 'G':
    if litros <= 20:
        print(f'O litro de gasolina vai custar R${(litros-(litros*4/100))*3.3:.2f}')
    else:
        print(f'O preço da gasolin vai custar R$ {(litros-(litros*6/100))*3.3:.2f}')
else:
    if litros <= 20:
        print(f'O litro de alcool vai custar R${(litros-(litros*3/100))*2.9:.2f}')
    else:
        print(f'O litro de alcool vai custar R${(litros-(litros*5/100))*2.9:.2f}')
print('--fim--')



