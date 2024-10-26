from modules import administrador, dados, cliente, engenheiro

# Função para validar as credenciais e o tipo de acesso do utilizador (adm ou eng)
def acesso():
    logins = dados.dadosLogin()

    print("Informe suas credenciais de acesso:")
    utilizador = input("Utilizador: ")
    senha = input("Senha: ")

    for login in logins:
        if login['username'] == utilizador and login['password'] == senha:
            print(f"Login realizado com sucesso!")
            tipo = login['role']
            if tipo == 'ENG':
                # Chamada da função para o tipo "Engenheiro"
                menuEngenheiro()
            else:
                # Chamada da função para o tipo "Administrador"
                menuAdministrador()
            return  # Encerra a função após login bem-sucedido

    print("Credenciais inválidas.")

# Funções para exibição dos menus por tipo de acesso (cliente, administrador ou engenheiro)
def menuCliente():
    while True:
        print("Parque Temático CESAELand - Área do Cliente")
        print("1 - Consultar Atrações Disponíveis")
        print("2 - Consultar Atrações Favoritas")
        print("3 - Voltar ao Menu Inicial")

        try:
            opcao = int(input("Digite o número da opção desejada: \n"))
            atracoes = dados.dadosAtracoes() #Obter dados no ficheiro dados.py

            match opcao:
                case 1:
                    print(cliente.consultarAtracoes(atracoes)) #Função para consulta das atrações no ficheiro cliente.py
                case 2:
                    vendas = dados.dadosVendas() #Obter dados no ficheiro dados.py
                    bilhetesCriancas, bilhetesAdultos = cliente.bilhetes(vendas)
                    print("Atração mais procurada por adultos:",
                          cliente.atracaoFavoritaAdulto(bilhetesAdultos, atracoes)) #Função para atração favorita no ficheiro cliente.py
                    print("Atração mais procurada por crianças:",
                          cliente.atracaoFavoritaCrianca(bilhetesCriancas, atracoes))
                case 3:
                    return main()
                case _:
                    print("Opção inválida!")

            #Opção para realizar nova consulta ou finalizar a aplicação
            novaConsulta = input("Deseja realizar uma nova consulta? (s/n): ").lower()
            if novaConsulta == 'n':
                print("Obrigado por usar o Parque Temático CESAELand! Até a próxima!")
                exit()
            elif novaConsulta != 's':
                return menuCliente()

        except ValueError: #tratamento de exceção
            print("Entrada inválida! Por favor, digite um número válido.")


def menuAdministrador():
    while True:
        print("Parque Temático CESAELand - Área do Administrador")
        print("1 - Consultar o total de todas as vendas")
        print("2 - Consultar o total de lucro")
        print("3 - Consultar a atração mais procurada por adultos (número de bilhetes vendidos)")
        print("4 - Consultar a atração mais procurada por crianças (número de bilhetes vendidos)")
        print("5 - Consultar a atração mais lucrativa (considere o período total)")
        print("6 - Consultar a atração menos lucrativa (considere o período total)")
        print("7 - Adicionar novo acesso para utilizador")
        print("8 - Voltar ao Menu Inicial")
        print("9 - Logout")

        try:
            opcao = int(input("Digite o número da opção desejada: \n"))

            atracoes = dados.dadosAtracoes() #Obter dados no ficheiro dados.py
            vendas = dados.dadosVendas()
            custos = dados.dadosCustos()

            match opcao:
                case 1:
                    print("Total de Vendas: {:.2f}".format(administrador.totalVendas(atracoes, vendas))) #Função para consulta das vendas no ficheiro administrador.py
                case 2:
                    print("Total de Lucro: {:.2f}".format(administrador.totaLucro(vendas, atracoes, custos))) #Função para consulta do lucro no ficheiro administrador.py
                case 3:
                    print("Atração mais procurada Adultos:", administrador.maisProcuradaAdultos(vendas, atracoes)) #Função para consulta da atracao mais procurada no ficheiro administrador.py
                case 4:
                    print("Atração mais procurada Crianças:", administrador.maisProcuradaCriancas(vendas, atracoes))
                case 5:
                    print("Atração mais lucrativa:", administrador.maisLucrativa(vendas, atracoes, custos)) #Função para consulta da atracao mais lucrativa no ficheiro administrador.py
                case 6:
                    print("Atração menos lucrativa:", administrador.menosLucrativa(vendas, atracoes, custos)) #Função para consulta da atracao menos lucrativa no ficheiro administrador.py
                case 7:
                    administrador.novoUtilizador() #Função para adicionar novo utilizador no ficheiro administrador.py
                case 8:
                    return main()
                case 9:
                    print("Obrigado por usar o Parque Temático CESAELand! Até a próxima!")
                    exit()
                case _:
                    print("Opção inválida!")

            novaConsulta = input("Deseja realizar uma nova consulta? (s/n): ").lower()
            if novaConsulta == 'n':
                print("Obrigado por usar o Parque Temático CESAELand! Até a próxima!")
                exit()
            elif novaConsulta != 's':
                return menuAdministrador()

        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")


def menuEngenheiro():
    while True:
        print("Parque Temático CESAELand - Área do Engenheiro de Manutenção")
        print("1 - Consultar Próximas Revisões")
        print("2 - Voltar ao Menu Inicial")
        print("3 - Lougout")

        try:
            opcao = int(input("Digite o número da opção desejada: \n"))

            match opcao:
                case 1:
                    atracoes = dados.dadosAtracoes()
                    vendas = dados.dadosVendas()

                    proximasRevisoes = engenheiro.consultaRevisoes(vendas, atracoes)  #Dataframe em pandas para realizar a exibição em forma de tabela
                    print("\nTabela de acompanhamento para próximas revisões:\n")
                    print(proximasRevisoes)

                    novaConsulta = input("Deseja realizar uma nova consulta? (s/n): ").lower()
                    if novaConsulta == 'n':
                        print("Obrigado por usar o Parque Temático CESAELand! Até a próxima!")
                        exit()
                    elif novaConsulta != 's':
                        return menuEngenheiro()
                case 2:
                    return main()
                case 3:
                    print("Obrigado por usar o Parque Temático CESAELand! Até a próxima!")
                    exit()
                case _:
                    print("Opção inválida!")

        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")

# Função principal da aplicação
def main():
    print("Bem vind@ ao Parque Temático CESAELand!")
    print("Por favor, escolha uma das opções abaixo:\n")
    print("1. Área de Login")
    print("2. Área do Cliente")

    try:
        opcao = int(input("\nDigite o número da opção desejada: "))
        if opcao == 1:
            print("*** Área de Login - Administrador / Engenheiro de Manutenção ***\n")
            acesso()
        elif opcao == 2:
            print("\n*** Acesso ao Menu do Cliente ***")
            menuCliente()
        else:
            print("\nOpção inválida. Por favor, escolha 1 ou 2.")
    except ValueError:
        print("Escolha uma opção válida!")

main() #Chamada da função principal da aplicação