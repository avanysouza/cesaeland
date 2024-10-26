import json

def dadosAtracoes(arquivo_json='../storage/Cesaeland_atracoes.json'):
    with open('storage/Cesaeland_atracoes.json') as CesaelandAtracoes:
        atracoes = json.load(CesaelandAtracoes)
    return atracoes
def dadosVendas(arquivo_json='../storage/Cesaeland_vendas.json'):
    with open('storage/Cesaeland_vendas.json') as CesaelandVendas:
        vendas = json.load(CesaelandVendas)
    return vendas

def dadosCustos(arquivo_json='../storage/Cesaeland_custos.json'):
    with open('storage/Cesaeland_custos.json') as CesaelandCustos:
        custos = json.load(CesaelandCustos)
    return custos

def dadosLogin(arquivo_logins='Cesaeland_logins.json'):
    with open('storage/Cesaeland_logins.json') as CesaelandLogins:
        logins = json.load(CesaelandLogins)
    return logins
