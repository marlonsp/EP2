def extrai_naipe(carta):
    if len(carta) == 3:
        if carta[2] == '♠':
            return '♠'
        if carta[2] == '♥':
            return '♥'
        if carta[2] == '♦':
            return '♦'
        else:
            return '♣'
    else: 
        if carta[1] == '♠':
            return '♠'
        if carta[1] == '♥':
            return '♥'
        if carta[1] == '♦':
            return '♦'
        else:
            return '♣'