from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))

print(f'os valores sorteados foram {numeros}')
print(f'o maior valor é: {max(numeros)}')
print(f'o menor valor é: {min(numeros)}')