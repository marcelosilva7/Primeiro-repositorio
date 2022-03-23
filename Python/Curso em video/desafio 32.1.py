import datetime
print('Vamos analisar se um ano é bissexto')
ano = int(input('Digite um ano desejado e 0 para o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if (ano % 4) == 0 and (ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissesto')
else:
    print(f'O ano {ano} nao é bissesto')

print('--fim--')
