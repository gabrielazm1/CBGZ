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

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    nova_lista = []
    dados_rolados.append(dados_no_estoque[dado_para_remover])
    del dados_no_estoque[dado_para_remover]
    nova_lista.append(dados_rolados)
    nova_lista.append(dados_no_estoque)
    return nova_lista

def calcula_pontos_regra_simples (listadados):
    dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range (len(listadados)):
        dic[listadados[i]] = dic[listadados[i]] + listadados[i]
    return dic

def calcula_pontos_soma(listadados):
    soma = 0
    for i in range(len(listadados)):
        soma = soma + listadados[i]
    return soma
        