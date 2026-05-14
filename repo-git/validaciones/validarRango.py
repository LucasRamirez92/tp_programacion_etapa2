def validar_rango(numero, minimo, maximo):
    if numero >= minimo and numero <= maximo:
        return True
    else:
        return False

def num_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def num_multiplo(numero, divisor):
    if divisor == 0:
        return False

    if numero % divisor == 0:
        return True
    else:
        return False

def num_primo(numero, divisor=2):
    if numero < 2:
        return False

    if divisor >= numero:
        return True

    if numero % divisor == 0:
        return False

    return num_primo(numero, divisor + 1)