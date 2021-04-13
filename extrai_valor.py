def extrai_valor(carta):
    if len(carta) == 3:
        valor = '10'
    else:
        valor = carta[0]
    return valor