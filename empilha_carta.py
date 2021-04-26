def empilha(baralho, origem, destino):
    baralho[destino] = baralho[origem]
    del(baralho[origem])
    return baralho
