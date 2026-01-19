import random



def mostrar_tabuleiro(tabuleiro):
    print()
    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("--+---+--")
    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("--+---+--")
    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
    print()



def verificar_vitoria(tabuleiro, jogador):
    combinacao_vitorias = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for c in combinacao_vitorias:
        if tabuleiro[c[0]] == jogador and tabuleiro[c[1]] == jogador and tabuleiro[c[2]] == jogador:
            return True
    return False



def jogar_humano(tabuleiro, jogador):
    while True:
        try:
            escolha = int(input(f"Jogador {jogador}, escolha uma posição entre 1 e 9: "))
            posicao = escolha - 1

            if 0 <= posicao <= 8:
                if tabuleiro[posicao] == ' ':
                    tabuleiro[posicao] = jogador
                    break
                else:
                    print("Essa posição já está ocupada!!!")
            else:
                print("Escolha um número entre 1 e 9!!!!")

        except ValueError:
            print("Digite um número válido por favor!")



def AI(tabuleiro_virtual, profundidade, vez_ia, jogador_pc, oponente):
    if verificar_vitoria(tabuleiro_virtual, jogador_pc):
        return 10 - profundidade
    if verificar_vitoria(tabuleiro_virtual, oponente):
        return profundidade - 10
    
    if ' ' not in tabuleiro_virtual:
        return 0

    if vez_ia:
        melhor_nota = -1000
        for i in range(9):
            if tabuleiro_virtual[i] == ' ':
                tabuleiro_virtual[i] = jogador_pc
                nota = AI(tabuleiro_virtual, profundidade + 1, False, jogador_pc, oponente)
                tabuleiro_virtual[i] = ' '
                melhor_nota = max(melhor_nota, nota)
        return melhor_nota

    else:
        melhor_nota = 1000
        for i in range(9):
            if tabuleiro_virtual[i] == ' ':
                tabuleiro_virtual[i] = oponente
                nota = AI(tabuleiro_virtual, profundidade + 1, True, jogador_pc, oponente)
                tabuleiro_virtual[i] = ' '
                melhor_nota = min(melhor_nota, nota)
        return melhor_nota



def jogar_computador(tabuleiro, jogador_pc, oponente):
    print(f"Computador ({jogador_pc}) está pensando...")
    
    melhor_jogada = None
    melhor_nota = -1000
    
    possiveis_jogadas = [i for i in range(9) if tabuleiro[i] == ' ']
    random.shuffle(possiveis_jogadas)
    
    for i in possiveis_jogadas:
        tabuleiro[i] = jogador_pc
        nota_da_jogada = AI(tabuleiro, 0, False, jogador_pc, oponente)
        tabuleiro[i] = ' '
        
        if nota_da_jogada > melhor_nota:
            melhor_nota = nota_da_jogada
            melhor_jogada = i

    if melhor_jogada is not None:
        tabuleiro[melhor_jogada] = jogador_pc
    else:
        print("Erro: nenhuma jogada válida encontrada!")




def jogo_da_velha():
    tabuleiro = [' ' for _ in range(9)]
    print("\n----------------------")
    print("Bem-vindo!")

    while True:
        try:
            modo = int(input(
            "1- Para jogar 1v1"
            "\n2- Para jogar 1vPC"
            "\n3- Sair"
            "\nEscolha o seu modo: "
            ))
            
            if modo in (1, 2, 3):
                break
            else:
                print("Escolha um modo válido! (1, 2 ou 3).")

        except ValueError:
            print("Insira um número válido!")

    simbolo_pc = None

    if modo == 2:
        simbolo_pc = random.choice(['X', 'O'])
        simbolo_humano = 'O' if simbolo_pc == 'X' else 'X'
        print(f"Sorteio realizado! O computador vai jogar como '{simbolo_pc}'")

    elif modo == 3:
        return False

    jogador_atual = 'X'

    for rodada in range(9):
        mostrar_tabuleiro(tabuleiro)

        if modo == 2 and jogador_atual == simbolo_pc:
            jogar_computador(tabuleiro, simbolo_pc, simbolo_humano)

        else:
            jogar_humano(tabuleiro, jogador_atual)

        if verificar_vitoria(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!!!")
            return True

        jogador_atual = 'O' if jogador_atual == "X" else "X"

    mostrar_tabuleiro(tabuleiro)
    print("Empate!")
    return True


while True:
    continuar = jogo_da_velha()
    if not continuar:
        break