# Jogo da Velha no Terminal (3x3)
Projeto desenvolvido para a 2ª Avaliação da disciplina de Coding  
- Curso: Bacharelado em Ciência da Computação — UNINASSAU  
- Professor: Tiago Martins Ribeiro  

## Descrição do Projeto
O projeto consiste em um Jogo da Velha (3x3) desenvolvido em Python para ser executado diretamente no terminal. O jogo é disputado entre dois jogadores que se alternam marcando as casas do tabuleiro com seus respectivos símbolos (`X` e `O`).

## Integrantes e Divisão de Tarefas
Gabriel Leal: readme, variáveis do jogo, menu, estatísticas.         
Gabriel Ramos: parte gráfica do jogo (tabuleiro), loop do jogo e jogadas, troca de turno, atualização do readme
Jose Claudionor: regras do jogo: não poder jogar na mesma casa, vitoria se completar linha, coluna ou diagonal, empate e recomeçar

## Tecnologias e Conceitos usados
1.​Variáveis e Tipos de Dados: Manipulação de Strings, Inteiros, Floats e Booleanos.
2.​Estruturas de Dados: Uso de Matrizes (Listas bidimensionais) para construir o tabuleiro e o mapa de posições.
3.​Estruturas de Repetição: Laços while (para controle de menus e turnos) e for (para verificação de vitória e varredura do tabuleiro).
4.​Estruturas Condicionais: Uso de if, elif e else para validação de jogadas e definição de ganhadores.
5.​Operadores Lógicos e Relacionais: Uso de and, == e != para aplicar as regras do jogo.
6.​F-Strings: Formatação de texto dinâmica para a interface do tabuleiro e cálculo de porcentagens nas estatísticas.

## Como Executar o Programa
### Pré-requisitos
- Ter o Python 3.x instalado no computador.

### Passo a Passo
1. Clonar o repositório:
```bash
git clone https://github.com/tialnic/Trabalho_coding.git
```
2. Acessar a pasta do projeto:
```bash
cd Trabalho_coding
```
3. Executar o jogo:
```bash
python jogo.py
```

## Regras do Jogo
1. O jogo é disputado em um tabuleiro 3x3 por dois jogadores.
2. O jogador 1 é representado pelo símbolo "X" e o jogador 2 é representado pelo símbolo "O"
3. os jogadores escolhem uma casa de 1 a 9 para jogar
4. Não é permitido jogar em uma casa ja ocupada
5.Vence quem completar uma linha, coluna ou diagonal
6. Se o tabuleiro for preenchido sem vencedor o jogo empata

## Desafio de Lógica Implementado
- Estatísticas da Sessão: Exibição do total de partidas disputadas, vitórias do Jogador 1, vitórias do Jogador 2, número de empates e porcentagem de aproveitamento dos jogadores ao longo das partidas.
