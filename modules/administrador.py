import json

# Funcao para calcular o total de vendas
def totalVendas(atracoes,vendas):
    total = 0
    for venda in vendas:
        for atracao in atracoes:
            if atracao['id'] == venda['atracao']: #Procurar a atração atraves do id na planilha de vendas
                if venda['tipoCliente'] == 'adulto':
                    total += atracao['precoAdulto']
                else:
                    total += atracao['precoCrianca']
    return total

# Funcao para calcular o total de lucro
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
                        # Calcular o lucro considerando o custo por bilhete
                        lucro = saldo - custo['custoManutencaoBilhete']
                        totalLucro += lucro

    #Retirar os custos fixos das atrações no total de lucro
    for custo in custos:
        totalLucro -= custo['custoFixoMes']
    return totalLucro

# Função para encontrar a atração mais procurada
def maisProcuradaAdultos(vendas, atracoes):
    quantidade = 0
    maisProcurada = None
    for atracao in atracoes:
        bilhetesAdultos = 0
        for venda in vendas:
            if venda['atracao'] == atracao['id'] and venda['tipoCliente'] == 'adulto': #Buscar atraçao e verificar o tipo do bilhete para adulto
                bilhetesAdultos += 1
        if bilhetesAdultos > quantidade:
            quantidade = bilhetesAdultos
            maisProcurada = atracao['atracao']
    return maisProcurada

# Função para consultar a atração mais procurada por crianças
def maisProcuradaCriancas(vendas, atracoes):
    quantidade = 0
    maisProcurada = None
    for atracao in atracoes:
        bilhetesCriancas = 0
        for venda in vendas:
            if venda['atracao'] == atracao['id'] and venda['tipoCliente'] == 'crianca': #Buscar atraçao e verificar o tipo do bilhete para criança
                bilhetesCriancas += 1
        if bilhetesCriancas > quantidade:
            quantidade = bilhetesCriancas
            maisProcurada = atracao['atracao']
    return maisProcurada

# Função para calcular a atração mais lucrativa
def maisLucrativa(vendas, atracoes, custos):
    quantLucro = 0
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
        if lucroAtracao > quantLucro:
            quantLucro = lucroAtracao
            maisLucrativa = atracao['atracao']
    return maisLucrativa

# Função para calcular a atração menos lucrativa
def menosLucrativa(vendas, atracoes, custos):
    quantLucro = 0
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
        if lucroAtracao < quantLucro:
            quantLucro = lucroAtracao
            menosLucrativa = atracao['atracao']
    return menosLucrativa

#Funcao para adicionar novo login

def novoUtilizador(arquivo_logins='storage/Cesaeland_logins.json'):
    with open('storage/Cesaeland_logins.json') as CesaelandLogins:
        logins = json.load(CesaelandLogins)

    #Inserir dados para novo utilizador:
    login = input("Informe o login para o utilizador: ")
    senha = input("Senha: ")

    while True:
        tipoAcesso = input("Informe o tipo de acesso (ADM ou ENG): ").upper()

        if tipoAcesso == "ADM" or tipoAcesso == "ENG": #validação do input realizado para manter o padrão do valor "ADM" ou "ENG"
            break
        else:
            print("Tipo de acesso inválido. Por favor, digite 'ADM' ou 'ENG'.")

    #Adicionar novo login no arquivo json através do append
    logins.append({"username": login, "password": senha, "role": tipoAcesso})

    with open(arquivo_logins, 'w') as CesaelandLogins:
        json.dump(logins, CesaelandLogins, indent=4)

    print("Novo login adicionado com sucesso!")

