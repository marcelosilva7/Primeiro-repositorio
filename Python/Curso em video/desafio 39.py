ano_nascimento = int(input('Que ano vc nasceu? '))
ano_atual = 2022
idade = ano_nascimento - ano_atual


if 18 > idade:
    tempo = 18 - idade
    print(f'Ainda nao deu seu tempo de alistar, falta {tempo} anos ainda!')
elif 18 == idade:
    print('Já esta na hora de se alistar!')
elif 18 < idade:
    tempo = idade - 18
    print(f'Você esta atrasado em se alistar, ja passou {tempo} anos do seu tempo de alistamento!')
