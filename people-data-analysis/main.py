cadastro = []
pessoas = []
quantidade = pesado = leve = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        pesado = pessoas[1]
        leve = pessoas[1]
    else:
        if pessoas[1] > pesado:
            pesado = pessoas[1]
        if pessoas[1] < leve:
            leve = pessoas[1]

    cadastro.append(pessoas[:])
    quantidade += 1
    pessoas.clear()
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('_'*30)
cadastro.sort()
print(f'Foram cadastradas {quantidade} pessoas.')
print(f'O maior peso foi de {pesado}kg. Peso de ', end='')
for p in cadastro:
    if p[1] == pesado:
        print(p[0])
print(f'O menor peso foi de {leve}. peso de ', end='')
for p in cadastro:
    if p[1] == leve:
        print(p[0])