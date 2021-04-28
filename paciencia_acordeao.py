from f_cria_baralho import cria_baralho
from f_extrai_valor import extrai_valor as exv
from f_extrai_naipe import extrai_naipe as exn
from movimentos_possiveis import lista_movimentos_possiveis as lmp
from possibilidade_de_movimento import possui_movimentos_possiveis as pmp
from empilha_carta import empilha

print('Paciencia Acordeão')
print('=-='*8)

Jogar = str(input('Aperte Enter para iniciar o jogo: ')) #start do jogo

if Jogar == '':
    baralho = cria_baralho()
    print('Estado atual do baralho: ')
    n = 1 #númerador para as cartas
    for i in baralho:
        print('{0}- {1}'.format(n, i))
        n += 1
    continua = pmp(baralho)
    while continua:
        print('')
        movimento = int(input('Escolha o número de uma carta para movê-la: '))
        while movimento not in range(1, 53):
            movimento = int(input('Esse não um número válido, escolha outro: '))
        while len(lmp(baralho, movimento-1)) == 0:
            movimento = int(input('Essa carta não possui movimentos disponíveis, escolha outra: '))
        if len(lmp(baralho, movimento-1)) == 1:
            if lmp(baralho, movimento-1)[0] == 1:
                baralho = empilha(baralho, movimento-1, movimento-2)
            else:
                baralho = empilha(baralho, movimento-1, movimento-4)
        else:
            escolha_de_movimento = int(input('As posições possíveis para mover essa carta são: {0} e {1}, reescreva o número para movê-la: '.format(movimento-1,movimento-3)))
            baralho = empilha(baralho, movimento-1, escolha_de_movimento-1)
        n = 1 #númerador para as cartas
        print('Estado atual do baralho: ')
        for i in baralho:
            print('{0}- {1}'.format(n, i))
            n += 1
        continua = pmp(baralho)

    print('Fim de jogo')
    if len(baralho) == 1:
        print('Você venceu')
    else:
        ('Você perdeu')
else:
    print('Fim de jogo')