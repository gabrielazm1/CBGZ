import random
def rolar_dados(n):
    i = 0
    lista = []
    while i < n:
        x = random.randint(1,6)
        lista.append(x)
        i = i + 1
    return lista

def guardar_dado (dados_rolados,dados_no_estoque,dado_para_guardar):
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    nova_lista = []
    i = 0
    while i < len(dados_rolados):
        if i != dado_para_guardar:
            nova_lista.append(dados_rolados[i])
        i = i + 1

    return [nova_lista, dados_no_estoque]

            