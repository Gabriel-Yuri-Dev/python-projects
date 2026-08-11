def voto(ano):
    """
    :param ano: recebe o ano de nascimento
    :return: se o voto é obrigatorio, opcional ou negado
    """
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if 16 <= idade <= 18 or idade >= 65:
        return f'Quem nasceu em {ano} tem {idade} anos e o voto é opcional.'
    elif idade < 16:
        return f'Quem nasceu em {ano} tem {idade} e não pode votar.'
    elif 18 < idade < 65:
        return f'quem nasceu em {ano} tem {idade} e o voto é obrigatorio'
print(voto(int(input('Digite o ano de nascimento: '))))