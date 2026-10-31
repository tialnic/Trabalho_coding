simbolo_jogador1 = "X"
simbolo_jogador2 = "O"

vitorias_jogador1 = 0
vitorias_jogador2 = 0
empates = 0
total_partidas = 0

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

executando = True

while executando == True:
    print("\n=========================")
    print("      JOGO DA VELHA      ")
    print("=========================")
    print("1 - Jogar")
    print("2 - Ver Regras")
    print("3 - Ver Placar")
    print("4 - Sair")
    print("=========================")

    opcao = input("Escolha uma opção (1 a 4): ")

    if opcao == "4":
        print("Saindo do jogo... Até logo!")
        executando = False
