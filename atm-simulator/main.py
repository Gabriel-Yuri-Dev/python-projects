saque = int(input('Digite o valor do saque: '))
total = saque
nota50 = nota20 = nota10 = nota1 = 0
while True:
    while total >= 50:
        total -= 50
        nota50 += 1
    while total >= 20:
        total -= 20
        nota20 += 1
    while total >= 10:
        total -= 10
        nota10 += 1
    while total >= 1:
        total -= 1
        nota1 += 1
    break
print(f'''O total de notas para este saque é:
{nota50} notas de R$50
{nota20} notas de R$20
{nota10} notas de R$10
{nota1} notas de R$1''')