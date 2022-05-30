idade = int(input('Vmoa saber sua classe elitorial, digite usa idade: '))

if idade < 16:
    print('Voto nao obrigatorio')
elif 18 <= idade <= 65:
    print('voto obrigatorio')
elif 16 <= idade < 18:
    print('voto opcional')
elif idade > 65:
    print('voto facultativo')

