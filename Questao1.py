import random
def rolar_dados(n):
    i = 0
    lista = []
    while i < n:
        x = random.randint(1,6)
        lista.append(x)
    i = i + 1
    return lista
