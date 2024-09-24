import os
import plotly.graph_objects as go


def clear():
    """Essa função limpa todos caracteres do console"""
    print("\n" * 130)  # Comando para limpar o console
    os.system("clear") # Limpar o terminal em dispositivos que utilizam Linux
    os.system("cls") # Limpar o terminal em dispositivos que utilizam windows
    print(techNovaSolutions)  # Imprimir a logo da empresa e os divisores


menuMsg = " Pressione qualquer tecla para retornar ao Menu."
divisor = f"\n=====================↪↩=======================\n"
techNovaSolutions = f"""
{divisor} 
 _____         _       _   _                  
|_   _|__  ___| |__   | \ | | _____   ____ _  
  | |/ _ \/ __| '_ \  |  \| |/ _ \ \ / / _` | 
  | |  __/ (__| | | | | |\  | (_) \ V / (_| | 
 _|_|\___|\___|_| |_|_|_|_\_|\___/ \_/ \__,_| 
/ ___|  ___ | |_   _| |_(_) ___  _ __  ___    
\___ \ / _ \| | | | | __| |/ _ \| '_ \/ __|   
 ___) | (_) | | |_| | |_| | (_) | | | \__ \   
|____/ \___/|_|\__,_|\__|_|\___/|_| |_|___/  
{divisor}
"""

corridasDisponiveis = [
    {"data": "2024-10-05", "hora": "15:00", "local": "São Paulo"},
    {"data": "2024-10-12", "hora": "18:00", "local": "Nova York"},
    {"data": "2024-10-20", "hora": "16:00", "local": "Tóquio"},
    {"data": "2024-10-28", "hora": "14:00", "local": "Berlim"}
]

# FUNÇÃO PARA COMPRAR TICKETS PARA EVENTOS
# FUNÇÃO PARA COMPRAR TICKETS PARA EVENTOS
def comprarTickets(listaDeCompras):
    """Essa função simula a compra de ingressos, selecionando a corrida e adicionando os itens a uma lista (Carrinho)."""
    adicionar = "s"
    valorTotal = 0
    while adicionar == "s":
        # Seleção de corrida
        print("Selecione a corrida desejada:")
        print(divisor)
        for i, corrida in enumerate(corridasDisponiveis, 1):
            print(f"[{i}] - {corrida['data']} às {corrida['hora']} - {corrida['local']}")
        print(divisor)
        try:
            opcao = int(input("Escolha a corrida ou '0' para cancelar: "))
            if 1 <= opcao <= len(corridasDisponiveis):
                corridaEscolhida = corridasDisponiveis[opcao - 1]
                corridaDescricao = f"🚗 Corrida em {corridaEscolhida['local']} - {corridaEscolhida['data']} às {corridaEscolhida['hora']}"
                print(f"Corrida selecionada: {corridaEscolhida['local']} em {corridaEscolhida['data']} às {corridaEscolhida['hora']}")
            elif opcao == 0:
                print("Operação cancelada!")
                main()
                return
            else:
                print("Erro! Corrida inexistente.")
                continue
        except ValueError:
            print("Erro! Digite um número válido.")
            continue

        # Seleção do tipo de ingresso
        print("[1] - Inteira: R$ 300,00")
        print("[2] - Meia: R$ 150,00")
        print("[3] - Cancelar operação")
        print(divisor)

        try:
            tipoDeIngresso = int(input("Selecione o tipo de Ingresso: "))
        except ValueError:
            print("Erro! Por favor, insira um número válido.")
            continue

        match tipoDeIngresso:
            case 1:
                try:
                    numeroDeIngressos = int(input("Quantos ingressos você irá querer desse tipo? "))
                    valorTotal += 300 * numeroDeIngressos
                    for _ in range(numeroDeIngressos):
                        listaDeCompras.append(f"[🎟] x1 Ingresso Inteira {corridaDescricao}")
                except ValueError:
                    print("Erro! Insira um número válido para a quantidade de ingressos.")
                    continue
            case 2:
                try:
                    numeroDeIngressos = int(input("Quantos ingressos você irá querer desse tipo? "))
                    valorTotal += 150 * numeroDeIngressos
                    for _ in range(numeroDeIngressos):
                        listaDeCompras.append(f"[🎫] x1 Ingresso Meia {corridaDescricao}")
                except ValueError:
                    print("Erro! Insira um número válido para a quantidade de ingressos.")
                    continue
            case 3:
                print("Operação cancelada!")
                main()
                return
            case _:
                print("Opção inválida!")
                continue

        adicionar = input("Deseja adicionar outro ingresso? [s/n]").lower()
        if adicionar not in ["s", "n"]:
            print("Entrada inválida! Por favor, insira 's' ou 'n'.")
            adicionar = "n"

    print(f"✅ Ingressos comprados com sucesso! O valor total é de: R$ {valorTotal}!")
    main()



def printBuyList(list):
    """Essa função exibe os itens da lista de compras."""
    for i in range(len(list)):
        print(f"{list[i]}")
    print(divisor)

# FUNÇÃO PARA VERIFICAR OS ITENS NO CARRINHO E ADICIONAR NOVOS
def verificarCarrinho(listaDeCompras, listaItensLoja):
    """Essa função verifica e gerencia o carrinho de compras, permitindo ao usuário adicionar, remover ou limpar itens"""
    clear()
    if len(listaDeCompras) == 0:
        print("Carrinho vazio")
        print(divisor)
    else:
        printBuyList(listaDeCompras)

    print("[1] - Adicionar um novo item")
    print("[2] - Limpar a Lista de compras")
    print("[3] - Remover um ou mais itens da lista de compras")
    print("[4] - Voltar ao menu")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Erro! Insira uma opção válida.")
        main()
        return

    match opcao:
        case 1:
            continuar = "s"
            while continuar != "n":
                clear()
                print("Itens da Loja - Fórmula E")
                print(divisor)
                for i, item in enumerate(listaItensLoja, 1):
                    print(f"[{i}] - {item}")

                try:
                    novoItem = int(input("Digite o número do item: "))
                    if 1 <= novoItem <= len(listaItensLoja):
                        listaDeCompras.append(f"🚗 {listaItensLoja[novoItem - 1]}")
                    else:
                        print("Erro! Item indisponível ou inexistente.")
                except ValueError:
                    print("Erro! Digite um número válido.")
                    continue

                print(divisor)
                printBuyList(listaDeCompras)
                continuar = input("Deseja continuar? [s/n]").lower()
                if continuar not in ["s", "n"]:
                    print("Entrada inválida! Por favor, insira 's' ou 'n'.")
                    continuar = "n"

            verificarCarrinho(listaDeCompras, listaItensLoja)
        case 2:
            clear()
            if len(listaDeCompras) > 0:
                listaDeCompras.clear()
                print("❌ Você removeu todos os itens do seu carrinho.")
            else:
                print("Erro! Seu carrinho já está vazio.")
            main()
        case 3:
            clear()
            if len(listaDeCompras) > 0:
                print("Selecione o número do item que deseja remover:")
                # Exibir todos os itens do carrinho
                for i, item in enumerate(listaDeCompras, 1):
                    print(f"[{i}] {item}")
                print(divisor)

                try:
                    itemDelete = int(input("Digite o número do item a ser removido ou '0' para cancelar: "))
                    if 1 <= itemDelete <= len(listaDeCompras):
                        itemParaRemover = listaDeCompras[itemDelete - 1]
                        listaDeCompras.remove(itemParaRemover)  # Remover o item correto
                        print(f"✔️ Item removido: {itemParaRemover}")
                    elif itemDelete == 0:
                        print("Operação cancelada.")
                    else:
                        print("Erro! Item não encontrado.")
                except ValueError:
                    print("Erro! Digite um número válido.")
            else:
                print("Erro! Seu carrinho está vazio.")
            main()
        case 4:
            main()
        case _:
            print("Opção inválida!")
            main()

def acessarDados():
    """Essa função exibe um menu para o usuário acessar comparações relacionados a estatisticas da Formula E com outras competições."""
    print("[1] Comparação: Veículos da Fórmula 1 x Fórmula E x Fórmula Indy")
    print("[2] Informações: Corredores brasileiros")
    print(f"{divisor}")
    opcao = int(input("Selecione uma opção - "))
    match opcao:
        case 1:
            clear()
            velocidadeVeiculos()
        case 2:
            clear()
            acessarCorredores()
        case _:
            clear()
            print(f"Opção inválida ou e desenvolvimento! {menuMsg}")


def velocidadeVeiculos():
    """Essa função cria e exibe um gráfico comparativo das velocidades atingidas pelos veículos da Fórmula 1, Fórmula Indy e Fórmula E em diferentes momentos, usando dados simulados."""
    # Dados de exemplo - Simulação
    categorias = [
        'Em repouso 0km/h',
        '1.86s',
        '3s',
        'Velocidade Máxima (Registrada)'
    ]

    # DEFINIÇÃO DAS VELOCIDADES ATINGIDAS EM RAZÃO DO TEMPO

    # Fórmula Indy
    repouso_formula_indy = 0
    um_oitentaedois_segundos_formula_indy = 100
    velocidade_3_segundos_formula_indy = 162
    velocidade_final_segundos_formula_indy = 380

    # Fórmula E
    repouso_formula_e = 0
    um_oitentaedois_segundos_formula_e = 67
    velocidade_3_segundos_formula_e = 110
    velocidade_final_segundos_formula_e = 329

    # Fórmula 1
    repouso_formula_1 = 0
    um_oitentaedois_segundos_formula_1 = 62
    velocidade_3_segundos_formula_1 = 100
    velocidade_final_segundos_formula_1 = 372

    formula_e = [
        repouso_formula_e,
        um_oitentaedois_segundos_formula_e,
        velocidade_3_segundos_formula_e,
        velocidade_final_segundos_formula_e
    ]

    formula_1 = [
        repouso_formula_1,
        um_oitentaedois_segundos_formula_1,
        velocidade_3_segundos_formula_1,
        velocidade_final_segundos_formula_1
    ]

    formula_indy = [
        repouso_formula_indy,
        um_oitentaedois_segundos_formula_indy,
        velocidade_3_segundos_formula_indy,
        velocidade_final_segundos_formula_indy
    ]

    # Criando o gráfico de linhas comparativo
    fig = go.Figure()

    # Adicionando linha para Fórmula E
    fig.add_trace(go.Scatter(
        x=categorias, y=formula_e, mode='lines+markers',
        name='Fórmula E', line=dict(color='blue')
    ))

    # Adicionando linha para Fórmula Indy
    fig.add_trace(go.Scatter(
        x=categorias, y=formula_indy, mode='lines+markers',
        name='Fórmula Indy', line=dict(color='brown')
    ))

    # Adicionando linha para Fórmula 1
    fig.add_trace(go.Scatter(
        x=categorias, y=formula_1, mode='lines+markers',
        name='Fórmula 1', line=dict(color='red')
    ))

    # Atualizando o layout do gráfico
    fig.update_layout(
        title='Velocidades que os Veículos da Fórmula 1, Fórmula Indy e Fórmula E atingem',
        xaxis_title='Tempo',
        yaxis_title='Velocidade',
    )

    # Exibição do gráfico
    fig.show()


# FUNÇÃO PARA ACESSAR A LISTA DE CORREDORES
def acessarCorredores():
    """Essa função exibe um menu para o usuário acessar as biografias de dois corredores brasileiros da Fórmula E."""
    print(techNovaSolutions)

    print("[1] - (ERT) Sérgio Sette Câmara")
    print("[2] - (ABT) Lucas Di Grassi")
    print(f"{divisor}")
    corredorBiografia = int(input('Escolha um dos corredores para acessar sua biografia: '))

    match corredorBiografia: # ESSA SEÇÃO DEVERÁ SER IMPLEMENTADA NA WEB
        case 1:
            input("""Sérgio Sette Câmara Filho, nascido em 23 de maio de 1998 em Belo Horizonte, 
            é um piloto de automobilismo brasileiro. Ele competiu em várias categorias, incluindo Fórmula 3 
            e Fórmula 2, antes de ingressar na Fórmula E.
            Na Fórmula 3, Sérgio iniciou sua carreira em 2014, competindo no Brasil e no Europeu. Ele teve 
            uma trajetória consistente, obtendo pódios e mostrando potencial. Sua participação destacada no 
            Masters de Fórmula 3 e no Grande Prêmio de Macau chamou a atenção da Red Bull, que o contratou 
            para seu programa de jovens pilotos.
            Em 2017, Sérgio estreou na Fórmula 2, continuando a demonstrar habilidade e velocidade. Sua jornada 
            na Fórmula 1 começou como piloto de testes da Toro Rosso e depois da McLaren. Ele retornou ao programa 
            de jovens pilotos da Red Bull em 2020.
            Em fevereiro de 2020, Sette Câmara fez a transição para a Fórmula E, inicialmente como reserva na Dragon 
            Racing. Posteriormente, ele foi promovido a piloto titular e continuou a competir na categoria com a equipe 
            NIO 333 Racing, que mais tarde foi rebatizada como ERT Formula E Team.""")
        case 2:
            input("""Lucas Di Grassi, nascido em São Paulo em 11 de agosto de 1984, é um piloto brasileiro 
            de automobilismo, competindo atualmente na Fórmula E pela equipe ABT CUPRA. Sua carreira começou no kart 
            em 1997, com rápidos sucessos, incluindo vitórias no sul-americano e pan-americano. Em 2004, entrou para o 
            programa de desenvolvimento de jovens pilotos da equipe Renault de Fórmula 1, onde permaneceu por 4 anos.
            Na GP2 Series, Di Grassi se destacou, conquistando um vice-campeonato em 2007 com a ART Grand Prix. Em 2010, 
            estreou na Fórmula 1 com a equipe Virgin Racing. Após sua passagem na Fórmula 1, tornou-se piloto de testes da 
            Pirelli em 2011.
            Em 2014, Di Grassi entrou para a Fórmula E pela equipe Audi Sport ABT Formula E Team, conquistando o título na 
            temporada 2016-17. Ao longo de sua carreira na Fórmula E, ele competiu por várias equipes, incluindo a ROKiT Venturi 
            Racing e a Mahindra Racing, antes de se juntar à equipe ABT CUPRA Formula E Team em 2023.""")
        case _:
            input(f"Opção inválida, corredor inexistente! {menuMsg}")

    main()


# PROGRAMA - ESTRUTURA PRINCIPAL
def main():
    """Função principal que exibe o menu principal do programa e permite ao usuário navegar pelas opções disponíveis."""
    clear()
    print("[1] - Comprar tickets")
    print("[2] - Verificar carrinho")
    print("[3] - Dados da Fórmula E")
    print("[4] - Encerrar programa")
    print(divisor)

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Erro! Digite um número válido.")
        main()
        return

    match opcao:
        case 1:
            clear()
            comprarTickets(listaDeCompras)
        case 2:
            clear()
            verificarCarrinho(listaDeCompras, listaItensLoja)
        case 3:
            clear()
            acessarDados()
        case 4:
            clear()
            print("Programa encerrado...")
        case _:
            print("Opção inválida!")
            main()

# Inicializar a lista de itens comprados pelo usuário
listaDeCompras = []
# Inicializar a lista de itens disponíveis na loja
listaItensLoja = ["[🎒] Bolsa - Fórmula E", "[👕] Camiseta - Fórmula E", "[👖] Calça - Fórmula E", "[👚] Blusa - Fórmula E", "[🚗] Carro Lego - Fórmula E"]

# DEFAULT
if __name__ == "__main__":
    clear()
    main()
