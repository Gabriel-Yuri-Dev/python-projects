v = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('em quantos anos você vai pagar?'))
m = s * (30/100)
p = v / (12 * a)
if p > m:
    print('Pedido negado, a prestação ficara muito alta pro seu sálario, a prestação custara {:.2f}'.format(p))
else:
    print('Emprestimo aprovado, você pagara {:.2f}'.format(p))
