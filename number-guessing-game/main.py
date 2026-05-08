import random
e = random.randint(1, 5)
print('Vou pensar em um numero entre 1 e 5')
r=int(input('Em que numero eu pensei? '))
if e == r:
    print('dessa vez você ganhou, mas não fique se achando ein')
else:
    print('hahahahhahahahahaha, você errou')