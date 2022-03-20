litros = float(input('Quantos litros de combustivel deseja abastecer? '))
performace = litros*10
tanque = 50
tl = litros/tanque
restante = 50-litros

print(f'Com {litros:.2f} litros de combustivel é possivel rodar {performace:.2f} KMs equivalente a {tl:.2f} tanque de combustivel\n'
      f'que ao final de rodar com o abastecido seu tanque ainda tera {restante:.2f} litros de combustivel\n'
      f'sendo possivel ainda rodar ainda {restante*10} KMs')
