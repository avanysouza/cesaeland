import json
import pandas as pd
def dadosAtracoes(arquivo_json='Cesaeland_atracoes.json'):
    with open('Cesaeland_atracoes.json') as CesaelandAtracoes:
        atracoes = json.load(CesaelandAtracoes)
    return atracoes

def dadosVendas(arquivo_json='Cesaeland_vendas.json'):
    with open('Cesaeland_vendas.json') as CesaelandVendas:
        vendas = json.load(CesaelandVendas)
    return vendas

def consultarAtracoes(atracoes):
    # Cria uma lista para armazenar os dados formatados
    listaAtracoes = []

    # Preenche a tabela com os dados das atrações
    for atracao in atracoes:
        # Extrai os dados necessários
        atracaoId = atracao['id']
        nome = atracao['atracao']
        precoAdulto = atracao['precoAdulto']
        precoCrianca = atracao['precoCrianca']
        duracao = atracao['duracaoSegundos']  # Duração no formato "min:seg"

        #Conversao da duração em minutos
        minutos = duracao // 60
        segundos = duracao % 60
        duracaoMinutos = f"{minutos:02}:{segundos:02}"

        # Adiciona uma linha à tabela
        listaAtracoes.append([atracaoId, nome, precoAdulto, precoCrianca, duracaoMinutos])

    df_atracoes = pd.DataFrame(listaAtracoes, columns=['ID', 'Atração', 'Adulto (€$)', 'Criança (€$)', 'Duração'])
    return df_atracoes

def bilhetes(vendas):
    # Dicionários com a quantidade de bilhetes para adultos e crianças
    bilhetesAdultos = {}
    bilhetesCriancas = {}

    # Contabiliza bilhetes vendidos para adultos e crianças
    for venda in vendas:
        atracaoId = venda['atracao']
        if venda['tipoCliente'] == 'adulto':
            if atracaoId in bilhetesAdultos:
                bilhetesAdultos[atracaoId] += 1
            else:
                bilhetesAdultos[atracaoId] = 1
        else:
            if atracaoId in bilhetesCriancas:
                bilhetesCriancas[atracaoId] += 1
            else:
                bilhetesCriancas[atracaoId] = 1

    return bilhetesCriancas, bilhetesAdultos

def atracaoFavoritaAdulto(bilhetesAdultos, atracoes):
    # Identificar a atração mais procurada para adultos
    maisProcuradaAdultos = 0
    atracaoAdultos = None
    for atracao in atracoes:
        atracaoId = atracao['id']
        if atracaoId in bilhetesAdultos and bilhetesAdultos[atracaoId] > maisProcuradaAdultos:
            maisProcuradaAdultos = bilhetesAdultos[atracaoId]
            atracaoAdultos = atracao['atracao']

    return atracaoAdultos

def atracaoFavoritaCrianca(bilhetesCriancas, atracoes):
    maisProcuradaCriancas = 0
    atracaoCriancas = None
    for atracao in atracoes:
        atracaoId = atracao['id']
        if atracaoId in bilhetesCriancas and bilhetesCriancas[atracaoId] > maisProcuradaCriancas:
            maisProcuradaCriancas = bilhetesCriancas[atracaoId]
            atracaoCriancas = atracao['atracao']

    return atracaoCriancas




