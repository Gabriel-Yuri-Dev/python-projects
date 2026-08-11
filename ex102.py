def fatorial(n, show = False ):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f' {c} ', end='')
            if c == 1:
             print(' = ', end='')
            else:
             print(' x ', end='')
    print(f'{f}')
valor = int(input('DIGITE UM VALOR: '))
while True:
    resp = input('DESEJA VER O CÁLCULO? [S/N] ').strip().upper()[0]
    if resp not in 'SN':
        print('Resposta invalida, tente novamente')
    if resp == 'S':
        fatorial(valor, True)
        break
    if resp == 'N':
        fatorial(valor, False)
        break