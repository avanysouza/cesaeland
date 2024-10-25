import json
import pandas as pd

#Funções para importar os dados das planilhas:
def dadosAtracoes(arquivo_json='Cesaeland_atracoes.json'):
    with open('Cesaeland_atracoes.json') as CesaelandAtracoes:
        atracoes = json.load(CesaelandAtracoes)
    return atracoes
def dadosVendas(arquivo_json='Cesaeland_vendas.json'):
    with open('Cesaeland_vendas.json') as CesaelandVendas:
        vendas = json.load(CesaelandVendas)
    return vendas

# Função para consultar as próximas revisões
def consultaRevisoes(vendas, atracoes):
    #Bilhetes vendidos por atracao
    totalBilhetesAtracao = {}

    # Contar o número de bilhetes vendidos para cada atração
    for venda in vendas:
        atracao = venda['atracao']
        if atracao in totalBilhetesAtracao:
            totalBilhetesAtracao[atracao] += 1
        else:
            totalBilhetesAtracao[atracao] = 1

    #Identificar quantos bilhetes faltam para a próxima revisão
    proximasRevisoes = []
    for atracao in atracoes:
        atracaoId = atracao['id']
        bilhetesVendidos = totalBilhetesAtracao.get(atracaoId, 0)
        saldoBilhetes = 50 - (bilhetesVendidos % 50)

        # Criar lista com os valores para a próxima revisão
        proximasRevisoes.append({
            "ID": atracaoId,
            "Nome": atracao['atracao'],
            "Bilhetes - Proxima Revisao": saldoBilhetes
        })

    df_proximas_revisoes = pd.DataFrame(proximasRevisoes)
    return df_proximas_revisoes


