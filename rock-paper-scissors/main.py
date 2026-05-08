from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('''[1] pedra
[2] papel
[3] tesoura''')
e = int(input('qual sua escolha?: '))
jogador = (e - 1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('o computador escolheu {}'.format(itens[computador]))
print('o jogador escolheu {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    else:
        print('JOGADOR VENCE')
if computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    if jogador == 1:
        print('empate')
    else:
        print('JOGADOR VENCE')
if computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    if jogador == 1:
        print('COMPUTADOR VENCE')
    if jogador == 2:
        print('EMPATE')