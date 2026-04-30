from funcoes import *

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela)

for rodada in range(12):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")

    rodada_ativa = True
    while rodada_ativa:
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao_valida = False
        while opcao_valida == False:
            opcao = input(">")
            if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4" or opcao == "0":
                opcao_valida = True
            else:
                print("Opção inválida. Tente novamente.")

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input(">"))
            resultado = guardar_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input(">"))
            resultado = remover_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")

        elif opcao == "3":
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens = rerrolagens + 1
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")

        elif opcao == "4":
            imprime_cartela(cartela)
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")

        elif opcao == "0":
            print("Digite a combinação desejada:")
            escolha_valida = False
            while escolha_valida == False:
                categoria = input(">")

                categoria_existe = False
                if categoria in cartela['regra_avancada']:
                    categoria_existe = True
                elif categoria == "1" or categoria == "2" or categoria == "3" or categoria == "4" or categoria == "5" or categoria == "6":
                    if int(categoria) in cartela['regra_simples']:
                        categoria_existe = True

                if categoria_existe == False:
                    print("Combinação inválida. Tente novamente.")

                else:
                    ja_usada = False
                    if categoria in cartela['regra_avancada']:
                        if cartela['regra_avancada'][categoria] != -1:
                            ja_usada = True
                    else:
                        if cartela['regra_simples'][int(categoria)] != -1:
                            ja_usada = True

                    if ja_usada == True:
                        print("Essa combinação já foi utilizada.")
                    else:
                        todos_dados = dados_rolados + dados_guardados
                        cartela = faz_jogada(todos_dados, categoria, cartela)
                        escolha_valida = True
                        rodada_ativa = False

imprime_cartela(cartela)

pontuacao = 0
soma_simples = 0

for v in cartela['regra_simples'].values():
    if v != -1:
        pontuacao = pontuacao + v
        soma_simples = soma_simples + v

for v in cartela['regra_avancada'].values():
    if v != -1:
        pontuacao = pontuacao + v

if soma_simples >= 63:
    pontuacao = pontuacao + 35

print(f"Pontuação total: {pontuacao}")