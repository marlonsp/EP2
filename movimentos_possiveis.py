from f_extrai_valor import extrai_valor
from f_extrai_naipe import extrai_naipe

def lista_movimentos_possiveis(baralho, indice):
    movimentos = []
    if indice == 0:
        return movimentos
    elif 0 < indice < 3:
        if extrai_valor(baralho[indice]) == extrai_valor(baralho[indice-1]) or extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice-1]):
            movimentos.append(1)
        return movimentos
    else:
        if extrai_valor(baralho[indice]) == extrai_valor(baralho[indice-1]) or extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice-1]):
            movimentos.append(1)
        if extrai_valor(baralho[indice]) == extrai_valor(baralho[indice-3]) or extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice-3]):
            movimentos.append(3)
        return movimentos
