from f_extrai_valor import extrai_valor as exv
from f_extrai_naipe import extrai_naipe as exn
from movimentos_possiveis import lista_movimentos_possiveis as lmp

def possui_movimentos_possiveis(baralho):
    total_movimentos = []
    for i in range(0, len(baralho)-1, 1):
        total_movimentos += lmp(baralho, i)
    if total_movimentos == []:
        return False
    else:
        return True