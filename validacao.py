def valida_inteiro(string):
    v = "0123456789"
    for letra in string:
        if letra not in v:
            return False
    if string == '':
        return False
    else:
        return True

def valida_faixa(a, b, string):
    if not valida_inteiro(string):
        return False
    valor = int(string)
    return valor>=a and valor<=b