from f_extrai_valor import extrai_valor
from f_extrai_naipe import extrai_naipe
from movimentos_possiveis import lista_movimentos_possiveis

def possui_movimentos_possiveis(baralho):
    total_movimentos = []
    for i in range(0, len(baralho)):
        total_movimentos += lista_movimentos_possiveis(baralho, i)
    if total_movimentos == []:
        return False
    else:
        return True