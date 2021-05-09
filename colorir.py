from f_extrai_naipe import extrai_naipe
def colorir_cartas(carta):
    CEND = '\033[0m'
    Ccopas = '\033[91m'
    Cpaus = '\033[92m'
    Couro = '\033[93m'
    Cespadas = '\033[94m'
    naipe = extrai_naipe(carta)
    if naipe == '♥':
        return (Ccopas + '{}'.format(carta) + CEND)
    elif naipe == '♣':
        return (Cpaus + '{}'.format(carta) + CEND)
    elif naipe == '♦':
        return (Couro + '{}'.format(carta) + CEND)
    else:
        return (Cespadas + '{}'.format(carta) + CEND)