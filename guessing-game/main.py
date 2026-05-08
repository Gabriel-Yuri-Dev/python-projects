import random
r = 11
e = random.randint(0, 10)
print('Vou pensar em um numero entre 0 e 10')

while r != e:
    if r == 11:
        r=int(input('Em que numero eu pensei? '))
    else:
        print('errado, tente novamente!')
        r = int(input('Em que numero eu pensei? '))
print('Voce acertou!!!')