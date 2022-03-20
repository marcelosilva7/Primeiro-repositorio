print('vamos calcular a idade em anos, meses, semanas e dias')
ano = int(input('Digite o ano que vc nasceu! '))
ano1 = int(input('Digite o ano atual! '))
ano2 = ano1-ano
print(f'Sua idade hoje é de {ano2} anos em meses equivale a {ano2*12} meses em semanas equivale a {ano2*12*4} semanas\n'
     f' e em dias equivale a {365*ano2} dias')