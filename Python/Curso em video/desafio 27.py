nome = str(input('Digite seu nome: ')).strip().lower()
dividindo = nome.split()
print('Seu primeiro nome é: {}'.format(dividindo[0]))
print('Seu ultimo nome é: {}'.format(dividindo[len(dividindo)-1]))

