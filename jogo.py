jogador1 = "X"
jogador2= "O"

vitorias_jogador1 = 0
vitorias_jogador2 = 0
empates = 0
total_partidas = 0

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

opcao = ""

print("=========================")
print("        Bem-vindo")
print("           ao")
print("     Jogo da Velha!")
print("=========================")

while opcao != "4":
    print("\n=========================")
    print("      JOGO DA VELHA      ")
    print("=========================")
    print("1 - Jogar")
    print("2 - Ver Regras")
    print("3 - Ver Placar")
    print("4 - Sair")
    print("=========================")

    opcao = input("Escolha uma opção (1 a 4): ")
    while opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4":
        print("Entrada inválida! Digite um número de 1 a 4.")
        opcao = input("Escolha uma opção (1 a 4): ")

    if opcao == "1":
        
        print("=== JOGO DA VELHA ===")

        print(f" {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} ")
        print("-----------")
        print(f" {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} ")
        print("-----------")
        print(f" {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} \n")
        
        jogador_atual = jogador1
        
        
        
    elif opcao == "2":
        print("\n=========================")
        print("     REGRAS DO JOGO      ")
        print("=========================")
        print("1. O jogo é disputado em um tabuleiro 3x3 por dois jogadores.")
        print("2. O Jogador 1 utiliza o símbolo 'X' e o Jogador 2 utiliza 'O'.")
        print("3. Os jogadores alternam escolhendo uma linha (1 a 3) e uma coluna (1 a 3).")
        print("4. Não é permitido jogar em uma casa já ocupada.")
        print("5. Vence quem completar primeiro uma linha, coluna ou diagonal com seu símbolo.")
        print("6. Se o tabuleiro for todo preenchido sem vencedor, a partida empata.")
        print("=========================")
        input("\nPressione Enter para voltar ao menu...")
    elif opcao == "3":
        # fazer placar aglomerativo (olhar o grupo)
        pass
    elif opcao == "4":
        print("Saindo do jogo... Obrigado por jogar!")
