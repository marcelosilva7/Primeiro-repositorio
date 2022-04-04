from random import randint
from time import sleep

itens  = ('pedra', 'papel', 'tesoura')
computador = 0

print('Vamos jogar Jokenpo!!!')
sleep(2)
print('-=-'*15)
print('''Faça sua jogada :
[0] Pedra
[1] Papel
[2] Tesoura''')
print('-=-'*15)
sleep(2)
jogador = int(input('Qual a sua jogada? '))
sleep(2)
print('JO')
sleep(1.3)
print('KEN')
sleep(1.3)
print('PO')
sleep(1.3)
print('-=-'*15)
print(f'Computador jogou: {itens[computador].upper()}')
print(f'Jogador jogou: {itens[jogador].upper()}')
print('-=-'*15)
sleep(1)
print('PROCESSANDO...')
sleep(3)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('OPCAO ESCOLHIDA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('OPCAO ESCOLHIDA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('OPCAO ESCOLHIDA INVALIDA')

