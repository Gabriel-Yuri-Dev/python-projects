opcao = 0
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
while opcao != 5:
    opcao = int(input('''Escolha a opção desejada: 
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa
    '''))
    if opcao == 1:
        resultado = n1 + n2
        print('A soma entre {} e {} vale {}'.format(n1, n2, resultado))
    if opcao == 2:
        resultado = n1 * n2
        print('A multiplicação entre {} e {} vale {}'.format(n1, n2, resultado))
    if opcao == 3:
        if n1 > n2:
            print('o maior é igual a: '.format(n1))
        else:
            print('o maior é igual a: '.format(n2))
    if opcao == 4:
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
    if opcao == 5:
        print('fim')





