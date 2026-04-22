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
        

def calcula_pontos_sequencia_baixa(listadados):
    for i in range(1, 4):
        contador = 0
        for numero in range(i, i + 4):
            if numero in listadados:
                contador = contador + 1
        if contador == 4:
            return 15
    return 0


def calcula_pontos_sequencia_alta(listadados):
    for i in range(1, 5):
        contador = 0
        for numero in range(i, i + 5):
            if numero in listadados:
                contador = contador + 1
        if contador == 5:
            return 30
    return 0

def calcula_pontos_full_house(listadados):
    soma = 0
    for v1 in listadados: 
        for v2 in listadados:
            if v1 != v2:
                qtd1 = 0 
                qtd2 = 0 
                for dado in listadados: 
                    if dado == v1: 
                        qtd1 = qtd1 + 1 
                    if dado == v2: 
                        qtd2 = qtd2 +  1 
                if qtd1 == 3 and qtd2 == 2: 
                    for dado in listadados: 
                        soma = soma + dado 
                    return soma 
    return 0 


def calcula_pontos_quadra(listadados):
    soma = 0
    for v1 in listadados: 
        qtd1 = 0          
        for dado in listadados: 
            if dado == v1: 
                qtd1 = qtd1 + 1 
            if qtd1 == 4 :
                for dado in listadados: 
                    soma = soma + dado 
                return soma 
    return 0

def calcula_pontos_quina(listadados):
    for v1 in listadados: 
        qtd1 = 0          
        for dado in listadados: 
            if dado == v1: 
                qtd1 = qtd1 + 1 
            if qtd1 == 5 :
                return 50 
    return 0