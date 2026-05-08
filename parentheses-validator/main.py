expressao = input('digite a expressão que quer analizar')
p = []
for simbolo in expressao:
    if simbolo == '(':
        p.append('(')
    elif simbolo == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
if len(p) == 0:
    print('A expressão está correta')
else:
    print('A expressão está errada')