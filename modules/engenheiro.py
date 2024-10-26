import pandas as pd

# Função para consultar as próximas revisões
def consultaRevisoes(vendas, atracoes):
    #Lista para armazenar os bilhetes vendidos por atracao
    totalBilhetesAtracao = {}

    # Contar o número de bilhetes vendidos para cada atração
    for venda in vendas:
        atracao = venda['atracao']
        if atracao in totalBilhetesAtracao:
            totalBilhetesAtracao[atracao] += 1
        else:
            totalBilhetesAtracao[atracao] = 1

    #Identificar quantos bilhetes faltam para a próxima revisão
    proximasRevisoes = [] #lista para armazenar os valores
    for atracao in atracoes:
        atracaoId = atracao['id']
        bilhetesVendidos = totalBilhetesAtracao.get(atracaoId, 0)
        saldoBilhetes = 50 - (bilhetesVendidos % 50)

        #Criar dicionario com os valores e realizar append na lista "proximasRevisoes":
        proximasRevisoes.append({
            "ID": atracaoId,
            "Nome": atracao['atracao'],
            "Bilhetes para próxima revisao": saldoBilhetes
        })

    #Ciclo for para percorrer a lista "proximasRevisoes" e verificar no dicionario os valores da chave "Bilhetes para proxima revisao" para ordena-los do menor para o maior.
        for i in range(len(proximasRevisoes)):
            for k in range(0, len(proximasRevisoes) - i - 1): #comparar com o elemento anterior
                if proximasRevisoes[k]["Bilhetes para próxima revisao"] > proximasRevisoes[k + 1]["Bilhetes para próxima revisao"]: #comparar se o valor da chave "Bilhetes para proxima revisao na posicao atual é maior do que a proxima posicao"
                    # Trocar os elementos de posição na lista:
                    proximasRevisoes[k], proximasRevisoes[k + 1] = proximasRevisoes[k + 1], proximasRevisoes[k]

    #Criar um dataframe utilizando a biblioteca pandas para exibir no console:
    listaProximasRevisoes = pd.DataFrame(proximasRevisoes)
    return listaProximasRevisoes


