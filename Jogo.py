import random

def jogo_adivinhacao():
    # Escolha da dificuldade
    dificuldade = input("Escolha a dificuldade (fácil, intermediário, difícil): ").lower()
    if dificuldade == "fácil":
        resultado = random.randint(0, 50)
    elif dificuldade == "intermediário":
        resultado = random.randint(0, 100)
    elif dificuldade == "difícil":
        resultado = random.randint(0, 200)
    else:
        print("Dificuldade inválida. Escolha entre fácil, intermediário ou difícil.")
        return

    # Recebendo o número de jogadores
    num_jogadores = int(input("Digite o número de jogadores: "))
    if num_jogadores <= 0:
        print("Impossível jogar com zero ou menos jogadores. Tente novamente.")
        return

    jogadores = []
    for i in range(num_jogadores):
        nome_jogador = input(f"Digite o nome do jogador {i+1}: ")
        jogadores.append(nome_jogador)

    # Mensagem de boas-vindas
    if num_jogadores >= 1:
        print("\nVamos iniciar o jogo!\nAs regras são as seguintes:\n1. O objetivo é adivinhar o número secreto.\n2. Cada rodada todos os jogadores têm que dar um palpite.\n3. Ao fim de todas as rodadas, será dada uma dica.\n4. Se ao fim de 5 rodadas o número secreto não for acertado, ele será revelado e os jogadores perdem.\n5. Apesar de terem perdido, será mostrada a quantidade de pontos que cada jogador fez.\n\nBom jogo!\n")

    palpites_totais = 0
    acertos_totais = 0

    # Loop de rodadas
    for rodada in range(1, 6):
        print("\nA rodada atual é:", rodada)
        for jogador in jogadores:
            palpite = int(input(f"{jogador}, digite o seu palpite: "))
            palpites_totais += 1

            if palpite == resultado:
                print(f"Parabéns, {jogador}! Você acertou o número secreto!")
                acertos_totais += 1
                break  # Sai do loop de rodadas
            elif palpite < resultado:
                print("O número secreto é maior que o seu palpite!")
            else:
                print("O número secreto é menor que o seu palpite!")

    # Se o loop terminar sem ninguém acertar
    else:
        print(f"\nO número secreto era {resultado}. Ninguém acertou.")

    # Estatísticas do jogo
    media_palpites = palpites_totais / (num_jogadores * 5)
    porcentagem_acertos = (acertos_totais / num_jogadores) * 100

    print("\nEstatísticas do jogo:")
    print("Número médio de palpites por rodada:", media_palpites)
    print("Porcentagem de acertos dos jogadores:", porcentagem_acertos, "%")

jogo_adivinhacao()
