import json

#Funções para importar os dados das planilhas:
def dadosAtracoes(arquivo_json='Cesaeland_atracoes.json'):
    with open('Cesaeland_atracoes.json') as CesaelandAtracoes:
        atracoes = json.load(CesaelandAtracoes)
    return atracoes
def dadosVendas(arquivo_json='Cesaeland_vendas.json'):
    with open('Cesaeland_vendas.json') as CesaelandVendas:
        vendas = json.load(CesaelandVendas)
    return vendas

def dadosCustos(arquivo_json='Cesaeland_custos.json'):
    with open('Cesaeland_custos.json') as CesaelandCustos:
        custos = json.load(CesaelandCustos)
    return custos

#Funcao para calcular o preço por atração
def precoAtracao(atracoes, atracaoId, tipo):
    for atracao in atracoes:
        if atracaoId == atracao['id']:
            if tipo == 'adulto':
                return atracao['precoAdulto']
            else:
                return atracao['precoCrianca']
def totalVendas(atracoes,vendas):
    total = 0
    for venda in vendas:
        for atracao in atracoes:
            if atracao['id'] == venda['atracao']:
                if venda['tipoCliente'] == 'adulto':
                    total += atracao['precoAdulto']
                else:
                    total += atracao['precoCrianca']
    return total

def totaLucro(vendas, atracoes, custos):
    totalLucro = 0
    for venda in vendas:
        for atracao in atracoes:
            if atracao['id'] == venda['atracao']:
                for custo in custos:
                    if custo['atracao'] == venda['atracao']:
                        if venda['tipoCliente'] == 'adulto':
                            saldo = atracao['precoAdulto']
                        else:
                            saldo = atracao['precoCrianca']
                        # Calcula lucro considerando o custo por bilhete
                        lucro = saldo - custo['custoManutencaoBilhete']
                        totalLucro += lucro

    #Retirar os custos fixos das atrações no total de lucro
    for custo in custos:
        totalLucro -= custo['custoFixoMes']
    return totalLucro


# Função para encontrar a atração mais procurada
def maisProcuradaAdultos(vendas, atracoes):
    maximo = 0
    maisProcurada = None
    for atracao in atracoes:
        bilhetesAdultos = 0
        for venda in vendas:
            if venda['atracao'] == atracao['id'] and venda['tipoCliente'] == 'adulto':
                bilhetesAdultos += 1
        if bilhetesAdultos > maximo:
            maximo = bilhetesAdultos
            maisProcurada = atracao['atracao']
    return maisProcurada, maximo

# Função para consultar a atração mais procurada por crianças
def maisProcuradaCriancas(vendas, atracoes):
    maximo = 0
    maisProcurada = None
    for atracao in atracoes:
        bilhetesCriancas = 0
        for venda in vendas:
            if venda['atracao'] == atracao['id'] and venda['tipoCliente'] == 'crianca':
                bilhetesCriancas += 1
        if bilhetesCriancas > maximo:
            maximo = bilhetesCriancas
            maisProcurada = atracao['atracao']
    return maisProcurada, maximo

# Função para calcular a atração mais lucrativa
def maisLucrativa(vendas, atracoes, custos):
    maxLucro = 0
    maisLucrativa = None

    for atracao in atracoes:
        lucroAtracao = 0
        for venda in vendas:
            if venda['atracao'] == atracao['id']:
                for custo in custos:
                    if custo['atracao'] == atracao['id']:
                        if venda['tipoCliente'] == 'adulto':
                            saldo = atracao['precoAdulto']
                        else:
                            saldo = atracao['precoCrianca']
                        lucro = saldo - custo['custoManutencaoBilhete']
                        lucroAtracao += lucro
        for custo in custos:
            if custo['atracao'] == atracao['id']:
                lucroAtracao -= custo['custoFixoMes']
        if lucroAtracao > maxLucro:
            maxLucro = lucroAtracao
            maisLucrativa = atracao['atracao']
    return maisLucrativa, maxLucro

# Função para calcular a atração menos lucrativa
def menosLucrativa(vendas, atracoes, custos):
    minLucro = 0
    menosLucrativa = None
    for atracao in atracoes:
        lucroAtracao = 0
        for venda in vendas:
            if venda['atracao'] == atracao['id']:
                for custo in custos:
                    if custo['atracao'] == atracao['id']:
                        if venda['tipoCliente'] == 'adulto':
                            saldo = atracao['precoAdulto']
                        else:
                            saldo = atracao['precoCrianca']
                        lucro = saldo - custo['custoManutencaoBilhete']
                        lucroAtracao += lucro
        for custo in custos:
            if custo['atracao'] == atracao['id']:
                lucroAtracao -= custo['custoFixoMes']
        if lucroAtracao < minLucro:
            minLucro = lucroAtracao
            menosLucrativa = atracao['atracao']
    return menosLucrativa, minLucro

#Funcao para adicionar novo login

def novoUtilizador(arquivo_logins='Cesaeland_logins.json'):
    with open('Cesaeland_logins.json') as CesaelandLogins:
        logins = json.load(CesaelandLogins)

    #Inserir dados para novo utilizador:
    login = input("Informe o login para o utilizador: ")
    senha = input("Senha: ")
    tipoAcesso = input("Informe o tipo de acesso (ADM ou ENG): ").upper()

    # Adicionar novo login no arquivo json
    logins.append({"username": login, "password": senha, "role": tipoAcesso})

    with open(arquivo_logins, 'w') as CesaelandLogins:
        json.dump(logins, CesaelandLogins, indent=4)

    print("Novo login adicionado com sucesso!")

