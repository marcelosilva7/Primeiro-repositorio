idade = int(input('Digite sua idade: '))

if idade < 16:
    print('voto nao obrigatoairo')
if 16 <= idade < 18:
    print('voto opcional')
if 18 <= idade <= 65:
    print('voto obrigatorio')
if idade > 65:
    print('ovot seila')