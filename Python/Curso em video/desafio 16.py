import math
numero = float(input('Digite um numero com casas decimais: '))
print(f'o numero {numero }  {math.trunc(numero)}  Sua versão arredondando para baixo é {math.floor(numero)}\n'
      f'Arredondando para cima é {math.ceil(numero)}')
