produto = float(input('Quanto custa o produto desejado: R$'))
pagamento = input('Qual a forma de pagamento? ').lower()

if pagamento == 'dinheiro':
    print(f'O produto custa R${produto:.2f}\n'
          f'com desconto de 10% fica R${produto-(produto*10/100):.2f}')
elif pagamento == 'cartao':
    print(f'O produto custa R${produto:.2f}\n'
          f'com desconto de 5% fica R${produto-(produto*5/100)}')
elif pagamento == '2xcartao':
    print(f'O produto custa R${produto:.2f}')
else:
    print(f'O produto custa R${produto:.2f}'
          f'Com juros de 20% custa R${produto:.2f}')
