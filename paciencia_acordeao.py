#funções para o funcionamento do jogo
from f_cria_baralho import cria_baralho
from f_extrai_valor import extrai_valor
from f_extrai_naipe import extrai_naipe
from movimentos_possiveis import lista_movimentos_possiveis
from possibilidade_de_movimento import possui_movimentos_possiveis
from empilha_carta import empilha
#Funções para validar o input
from validacao import valida_inteiro
from validacao import valida_faixa

from colorir import colorir_cartas

#inicio do jogo
print('=-='*8)
Dstart = '\33[35m'
Dend = '\33[0m'
print(Dstart+ 'Paciencia Acordeão' + Dend)
print('=-='*8)

Jogar = str(input('Aperte Enter para iniciar o jogo: '))  # start do jogo

#verificador de start
while Jogar == '':
    baralho = cria_baralho()
    #Print do baralho
    print('Estado atual do baralho: ')
    n = 1
    for i in baralho:
        i = colorir_cartas(i)
        print('{0}- {1}'.format(n, i))
        n += 1
    #Verifica se existem jogadas possíveis
    continua = possui_movimentos_possiveis(baralho)
    #Se existirem jogadas possíveis, o jogo continua
    while continua:
        print('')
        movimento = input('Escolha o número de uma carta para movê-la (Entre 1 e {}): '.format(len(baralho)))
        # Verifica se a entrada para o movimento é válida
        verificar = False
        while verificar == False:
            if valida_faixa(1, len(baralho), movimento) == True:
                movimento = int(movimento)
                if len(lista_movimentos_possiveis(baralho, movimento-1)) == 0:
                    verificar = False
                    movimento = input('Essa carta não possui movimentos , escolha outro: ')            
                else:
                    verificar = True
            elif movimento == '':
                verificar = False
                movimento = input('Isso não é um número válido , escolha outro: ')
            else:
                verificar = False
                movimento = input('Isso não é um número válido , escolha outro: ')
        movimento = int(movimento)
        #empilha carta com apenas 1 opção de movimento
        if len(lista_movimentos_possiveis(baralho, movimento-1)) == 1:
            if lista_movimentos_possiveis(baralho, movimento-1)[0] == 1:
                baralho = empilha(baralho, movimento-1, movimento-2)
            else:
                baralho = empilha(baralho, movimento-1, movimento-4)
        #Escolha e empilha carta com 2 opções de movimento
        elif len(lista_movimentos_possiveis(baralho, movimento-1)) == 2:
            print('')
            print('Essa carta possui duas opções de movimentos: ')
            print('1- {}'.format(colorir_cartas(baralho[movimento-4])))
            print('2- {}'.format(colorir_cartas(baralho[movimento-2])))
            escolha_de_movimento = input('Qual sua escolha? (1 ou 2): ')
            #valida a escolha de movimento
            while escolha_de_movimento != '1' and escolha_de_movimento != '2':
                escolha_de_movimento = input('Isso não é um movimento válido , escolha outro (1 ou 2): ')
            if escolha_de_movimento == '1':
                baralho = empilha(baralho, movimento-1, movimento-2)
            else:
                baralho = empilha(baralho, movimento-1, movimento-4)
        print('')
        #Print do baralho
        n = 1
        print('Estado atual do baralho: ')
        for i in baralho:
            i = colorir_cartas(i)
            print('{0}- {1}'.format(n, i))
            n += 1
        #Verifica se existem jogadas possíveis
        continua = possui_movimentos_possiveis(baralho)
    print('')
    #Print do resultado do jo
    if len(baralho) == 1:
        Dwin = '\33[92m'
        Dend = '\33[0m'
        print(Dwin + 'Fim de jogo: Você venceu, Parabéns!' + Dend)
    else:
        print('Não existem mais jogadas possíveis...')
        Dlose = '\33[91m'
        Dend = '\33[0m'
        print(Dlose + 'Fim de jogo: Você perdeu' + Dend)
    #Restart do jogo
    quer_novamente = str(input('Deseja jogar novamente? (S/N) '))
    #Valida a escolha
    while quer_novamente != 'S' and quer_novamente != 's' and quer_novamente != 'N' and quer_novamente != 'n':
        quer_novamente = str(input('Essa não é uma resposta válida, deseja jogar novamente? (S/N) '))
    if quer_novamente == 'S' or quer_novamente == 's':
        Jogar = ''
    else:
        Jogar = 'fim'
#Encerramento final do jogo
else:
    print('=-='*8)
    print('Fim de jogo')