def sorteio(lista):
    from random import randint
    for count in range(0, 5):
        lista.append(randint(1, 10))
def somar(lista):
    soma = 0
    for count in range(0, 5):
        if lista[count] % 2 == 0:
            soma += lista[count]
    print('os valores sorteados foram: ', end='')
    for c in range(0, 5):
        print(lista[c], end=' ')
    print()
    print('os valores pares foram: ', end='')
    for c in range(0, 5):
        if lista[c] % 2 == 0:
            print(lista[c], end=' ')
    print()
    print(f'o total somado foi {soma}')
numeros = []
sorteio(numeros)
somar(numeros)