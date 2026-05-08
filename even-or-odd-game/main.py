from random import randint
comp = 0
jogador = 0
count = 0
while True:
   print(30*'-')
   comp = randint(1, 2)
   escolha = input('''Jogo do impar ou par, escolha sua opção:
[ 1 ] impar
[ 2 ] par
''').strip().lower()
   if escolha == 1:
       escolha = 'impar'
   else:
       escolha = 'par'
   print(30*'-')
   jogador = int(input('escolha um número: '))
   print(f'o computador escolheu {comp}')
   if escolha == 'impar' and  (comp + jogador) % 2 != 0:
       print('Você ganhou, parabéns')
   elif escolha == 'par' and (comp + jogador) % 2 == 0:
       print('Você ganhou, parabéns')
       count += 1
   else:

       print(f'Game over, você ganhou um total de {count} vezes, Programa finalizado')
       break
