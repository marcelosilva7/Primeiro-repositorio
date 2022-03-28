idade = int(input('Qual sua idade? '))

if 18 > idade:
    tempo = 18 - idade
    print(f'Ainda nao deu seu tempo de alistar, falta {tempo} anos ainda!')
elif 18 == idade:
    print('Já esta na hora de se alistar!')
elif 18 < idade:
    tempo = idade - 18
    print(f'Você esta atrasado em se alistar, ja passou {tempo} anos do seu tempo de alistamento!')
