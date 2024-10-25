import json
import cliente
import administrador
import engenheiro
import pandas as pd

# Função para obter os dados de login do arquivo json
def dadosLogin(arquivo_json='Cesaeland_logins.json'):
    with open(arquivo_json) as CesaelandLogins:
        logins = json.load(CesaelandLogins)
    return logins


# Função para validar as credenciais e tipo de acesso do utilizador
def acesso():
    logins = dadosLogin()

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

# Funções para exibição dos menus por tipo de acesso
def menuCliente():
    while True:
        print("Parque Temático CESAELand - Área do Cliente")
        print("1 - Consultar Atrações Disponíveis")
        print("2 - Consultar Atrações Favoritas")
        print("3 - Voltar ao Menu Inicial")

        try:
            opcao = int(input("Digite o número da opção desejada: \n"))
            atracoes = cliente.dadosAtracoes()

            match opcao:
                case 1:
                    print(cliente.consultarAtracoes(atracoes))
                case 2:
                    vendas = cliente.dadosVendas()
                    bilhetesCriancas, bilhetesAdultos = cliente.bilhetes(vendas)
                    print("Atração mais procurada por adultos:",
                          cliente.atracaoFavoritaAdulto(bilhetesAdultos, atracoes))
                    print("Atração mais procurada por crianças:",
                          cliente.atracaoFavoritaCrianca(bilhetesCriancas, atracoes))
                case 3:
                    return acesso()
                case _:
                    print("Opção inválida!")

            novaConsulta = input("Deseja realizar uma nova consulta? (s/n): ").lower()
            if novaConsulta == 'n':
                print("Obrigado por usar o Parque Temático CESAELand! Até a próxima!")
                exit()
            elif novaConsulta != 's':
                return menuCliente()

        except ValueError:
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

            atracoes = administrador.dadosAtracoes()
            vendas = administrador.dadosVendas()
            custos = administrador.dadosCustos()

            match opcao:
                case 1:
                    print("Total de Vendas: {:.2f}".format(administrador.totalVendas(atracoes, vendas)))
                case 2:
                    print("Total de Lucro: {:.2f}".format(administrador.totaLucro(vendas, atracoes, custos)))
                case 3:
                    print("Atração mais procurada Adultos:", administrador.maisProcuradaAdultos(vendas, atracoes))
                case 4:
                    print("Atração mais procurada Crianças:", administrador.maisProcuradaCriancas(vendas, atracoes))
                case 5:
                    print("Atração mais lucrativa:", administrador.maisLucrativa(vendas, atracoes, custos))
                case 6:
                    print("Atração menos lucrativa:", administrador.menosLucrativa(vendas, atracoes, custos))
                case 7:
                    administrador.novoUtilizador()
                case 8:
                    return acesso()
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
                    atracoes = engenheiro.dadosAtracoes()
                    vendas = engenheiro.dadosVendas()

                    df_revisoes = engenheiro.consultaRevisoes(vendas, atracoes)  # Chama a função e armazena o DataFrame

                    print(df_revisoes)

                    novaConsulta = input("Deseja realizar uma nova consulta? (s/n): ").lower()
                    if novaConsulta == 'n':
                        print("Obrigado por usar o Parque Temático CESAELand! Até a próxima!")
                        exit()
                    elif novaConsulta != 's':
                        return menuEngenheiro()
                case 2:
                    return acesso()
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

main()