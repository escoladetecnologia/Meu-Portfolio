import tkinter as tk
from copy import deepcopy


# Definir as constantes para os jogadores
JOGADOR_X = "X"
JOGADOR_O = "O"
COMPUTADOR = JOGADOR_O  # O computador jogará com "O"

# Definir a função de utilidade para avaliar o estado do tabuleiro
def utilidade(tabuleiro):
    # Verificar se o jogador X venceu
    if ((tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == JOGADOR_X) or
        (tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == JOGADOR_X) or
        (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == JOGADOR_X) or
        (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == JOGADOR_X) or
        (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == JOGADOR_X) or
        (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == JOGADOR_X) or
        (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == JOGADOR_X) or
        (tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == JOGADOR_X)):
        return -1  # O jogador X venceu

    # Verificar se o jogador O venceu
    elif ((tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == JOGADOR_O) or
          (tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == JOGADOR_O) or
          (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == JOGADOR_O) or
          (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == JOGADOR_O) or
          (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == JOGADOR_O) or
          (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == JOGADOR_O) or
          (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == JOGADOR_O) or
          (tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == JOGADOR_O)):
        return 1  # O jogador O venceu

    # Verificar se houve empate
    elif all(tabuleiro[i] != " " for i in range(9)):
        return 0  # Empate

    # Caso contrário, o jogo ainda está em andamento
    else:
        return None

# Função Minimax com poda alfa-beta
def minimax(tabuleiro, profundidade, maximizando, alfa, beta):
    resultado = utilidade(tabuleiro)
    if resultado is not None:
        return resultado

    if maximizando:
        melhor_valor = -float("inf")
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = COMPUTADOR
                valor = minimax(tabuleiro, profundidade + 1, False, alfa, beta)
                tabuleiro[i] = " "
                melhor_valor = max(melhor_valor, valor)
                alfa = max(alfa, melhor_valor)
                if beta <= alfa:
                    break  # Poda beta
        return melhor_valor

    else:
        melhor_valor = float("inf")
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = JOGADOR_X
                valor = minimax(tabuleiro, profundidade + 1, True, alfa, beta)
                tabuleiro[i] = " "
                melhor_valor = min(melhor_valor, valor)
                beta = min(beta, melhor_valor)
                if beta <= alfa:
                    break  # Poda alfa
        return melhor_valor

# Função para obter a melhor jogada para o computador
def melhor_jogada(tabuleiro):
    melhor_valor = -float("inf")
    melhor_jogada = None
    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = COMPUTADOR
            valor = minimax(tabuleiro, 0, False, -float("inf"), float("inf"))
            tabuleiro[i] = " "
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_jogada = i
    return melhor_jogada

# Função para atualizar o tabuleiro após uma jogada
def atualizar_tabuleiro(tabuleiro, jogada, jogador):
    tabuleiro[jogada] = jogador

# Função para verificar se o jogo acabou
def jogo_acabou(tabuleiro):
    resultado = utilidade(tabuleiro)
    if resultado is not None:
        if resultado == 0:
            return "Empate"
        elif resultado == -1:
            return "Jogador X venceu"
        else:
            return "Jogador O venceu"
    else:
        return None

# Função para reiniciar o jogo
def reiniciar_jogo():
    global tabuleiro, jogador_atual
    tabuleiro = [" "] * 9
    jogador_atual = JOGADOR_X
    atualizar_tabuleiro_gui()

# Função para atualizar a interface gráfica
def atualizar_tabuleiro_gui():
    for i in range(9):
        botoes[i].config(text=tabuleiro[i])

# Função para lidar com as jogadas do jogador
def jogada_jogador(botao):
    global jogador_atual
    indice = botoes.index(botao)
    if tabuleiro[indice] == " ":
        atualizar_tabuleiro(tabuleiro, indice, jogador_atual)
        atualizar_tabuleiro_gui()
        resultado = jogo_acabou(tabuleiro)
        if resultado is not None:
            mensagem_final.config(text=resultado)
        else:
            jogador_atual = COMPUTADOR
            jogada_computador()

# Função para lidar com as jogadas do computador
def jogada_computador():
    global jogador_atual
    jogada = melhor_jogada(tabuleiro)
    atualizar_tabuleiro(tabuleiro, jogada, COMPUTADOR)
    atualizar_tabuleiro_gui()
    resultado = jogo_acabou(tabuleiro)
    if resultado is not None:
        mensagem_final.config(text=resultado)
    else:
        jogador_atual = JOGADOR_X

# Inicializar o jogo
tabuleiro = [" "] * 9
jogador_atual = JOGADOR_X

# Criar a janela do jogo
janela = tk.Tk()
janela.title("Jogo da Velha")

# Criar os botões para o tabuleiro
botoes = []
for i in range(9):
    botao = tk.Button(janela, text=" ", font=("Arial", 20), width=5, height=2, command=lambda i=i: jogada_jogador(botoes[i]))
    botao.grid(row=i // 3, column=i % 3)
    botoes.append(botao)

# Criar a mensagem final
mensagem_final = tk.Label(janela, text="", font=("Arial", 16))
mensagem_final.grid(row=3, column=0, columnspan=3)

# Criar o botão de reiniciar
botao_reiniciar = tk.Button(janela, text="Reiniciar", font=("Arial", 14), command=reiniciar_jogo)
botao_reiniciar.grid(row=4, column=0, columnspan=3, pady=10)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
