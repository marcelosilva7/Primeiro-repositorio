cont = menor = maior = medio = 0
nome_bronze = nome_prata = nome_ouro = ''
for c in range(1, 4):
    nome = input('Digte o nome do pais: ')
    bronze = int(input('Quantas medalhas de bronz? '))
    prata = int(input('Quantas medalhas de prta? '))
    ouro = int(input('Quantas medalhas de ouro? '))
    prata_peso = prata * 2
    ouro_peso = ouro * 3
    pontos = prata_peso + ouro_peso + bronze
    cont += 1
    if cont == 1:
        menor = maior = medio = pontos
        nome_bronze = nome_prata = nome_ouro = nome
    elif pontos < menor:
        menor = pontos
        nome_bronze = nome
    elif pontos > maior:
        maior = pontos
        nome_ouro = nome
    elif menor < pontos < maior:
        medio = pontos
        nome_prata = nome
print(f'o pais BRONZE foi {nome_bronze} com {menor} pontos')
print(f'o pais com OURO foi {nome_ouro} com {maior} pontos')
print(f'o pais PRAT foi {nome_prata}, com {medio} pontos')


