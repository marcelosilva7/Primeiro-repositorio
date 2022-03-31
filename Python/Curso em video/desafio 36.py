casa = float(input('Quanto vai custar a casa? R$'))
salario = float(input('Qual é seu salario? '))
anos = int(input('Em quantos anos pretende pagar ?'))
prestacao = casa/(anos*12)


if (salario*30/100) <= salario:
    print(f'Parabens seu emprestimo foi aprovado em {anos*12} prestaçoes de R${prestacao:.2f}')
else:
    print('Infelizmente você nao tem renda suficiente para comprar essas casa')
