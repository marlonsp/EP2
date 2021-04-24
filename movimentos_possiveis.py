from f_extrai_valor import extrai_valor as exv
from f_extrai_naipe import extrai_naipe as exn

def lista_movimentos_possiveis(baralho, indice):
    movimentos = []
    if indice == 0:
        return movimentos
    elif 0<indice<3:
        if exv(baralho[indice]) == exv(baralho[indice-1]) or exn(baralho[indice]) == exn(baralho[indice-1]):
            movimentos.append(1)
        return movimentos
    else:
        if exv(baralho[indice]) == exv(baralho[indice-1]) or exn(baralho[indice]) == exn(baralho[indice-1]):
            movimentos.append(1)
        if exv(baralho[indice]) == exv(baralho[indice-3]) or exn(baralho[indice]) == exn(baralho[indice-3]):
            movimentos.append(3)
        return movimentos
