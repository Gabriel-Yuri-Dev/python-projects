def contador(inicio, fim, passo):
    from time import sleep
    atual = inicio
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    if inicio < fim:
        while atual <= fim:
            print(f'{atual}', end=' ')
            atual += passo
            sleep(0.5)
    if inicio > fim:
        while atual >= fim:
            print(f'{atual}', end=' ')
            atual -= passo
            sleep(0.5)
    print('')
    print('-'*20)
print('contagem de 1 a 10 de 1 em 1')
contador(1, 10, 1)
print('contagem de 10 a 0 de 2 em 2')
contador(10, 0, 2)
print('Sua vez')
print('-' * 20)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)