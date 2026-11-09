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

mapa = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
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
        
        jogadas_feitas = 0
        jogador_atual = jogador1
        vencedor = ""
        while jogadas_feitas < 9 and vencedor == "":
            print("\n=== JOGO DA VELHA ===")

            print(f" {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} ")
            print("-----------")
            print(f" {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} ")
            print("-----------")
            print(f" {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} \n")
            
            jogada = input(f"Jogador {jogador_atual}, digite a casa: ")

            posicao_valida = False
            
            for linha in range(3):
               for coluna in range(3):
                
                  if mapa[linha][coluna] == jogada: 
                    if tabuleiro[linha][coluna] == " ":
                       tabuleiro[linha][coluna] = jogador_atual
                       posicao_valida = True

                    elif tabuleiro[linha][coluna] == "":
                       tabuleiro[linha][coluna] = jogador_atual
                       posicao_valida = True

            
            if posicao_valida == True:
                print("Jogada realizada!")
                jogadas_feitas += 1

            for linha in range(3):
                if ( tabuleiro[linha][0] == jogador_atual and
                     tabuleiro[linha][1] == jogador_atual and
                     tabuleiro[linha][2] == jogador_atual):
                    vencedor = jogador_atual

            for coluna in range(3):
                if ( tabuleiro[0][coluna] == jogador_atual and
                     tabuleiro[1][coluna] == jogador_atual and 
                     tabuleiro[2][coluna] == jogador_atual):
                     vencedor = jogador_atual    

            if (tabuleiro[0][0] == jogador_atual and 
                tabuleiro[1][1] == jogador_atual and 
                tabuleiro[2][2] == jogador_atual):
                vencedor = jogador_atual

            elif (tabuleiro[0][2] == jogador_atual and
                  tabuleiro[1][1] == jogador_atual and
                  tabuleiro[2][0] == jogador_atual):
                  vencedor = jogador_atual
                      
            if vencedor == "" :      
                if jogador_atual == jogador1:
                    jogador_atual = jogador2
                else:
                    jogador_atual = jogador1
            else:
                print("Jogada inválida! Tente novamente.")

    if vencedor == jogador1:
        print("Jogador 1 venceu!")
        vitorias_jogador1 += 1
        
    elif vencedor == jogador2:
        print("Jogador 2 venceu!")
        vitorias_jogador2 += 1

        print("=== JOGO DA VELHA ===")
        print(f" {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} ")
        print("-----------")
        print(f" {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} ")
        print("-----------")
        print(f" {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} \n")
     
        
    elif opcao == "2":
        print("\n=========================")
        print("     REGRAS DO JOGO      ")
        print("=========================")
        print("1. O jogo é disputado em um tabuleiro 3x3 por dois jogadores.")
        print("2. O Jogador 1 utiliza o símbolo 'X' e o Jogador 2 utiliza 'O'.")
        print("3. Os jogadores escolhem uma jogada de 1 a 9(1 a 3 primeira linha da esquerda pra direita)")
        print("numero 3 a 6 escolhe a casa da esquerda pra direita da segunda linha e 7 a 9 da terceira linha")
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
    
