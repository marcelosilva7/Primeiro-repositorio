frase = str(input('Digite uma frase: ').strip().lower())
print('Vamos contar a letra a...')
print('Na frase aparece {} letras a'.format(frase.count('a')))
print('A primeira posição da letra é na posição: {}'.format(frase.find('a')+1))
print('Ultima posição que aparece a letra é: {} '.format(frase.rfind('a')+1))




