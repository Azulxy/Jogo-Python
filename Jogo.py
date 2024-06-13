import random

def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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
        print("Dificuldade inválida. Escolha entre fácil (0 - 50), intermediário (0 - 100) ou difícil (0 - 200).")
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
        print(f"\nVamos iniciar o jogo!\n\nO nível escolhido foi: {dificuldade}\n\nAs regras são as seguintes:\n\n1. O objetivo é adivinhar o número secreto.\n2. Cada rodada todos os jogadores têm que dar um palpite.\n3. Nas rodadas 2 e 4 serão dadas dicas adicionais.\n4. Se ao fim de 5 rodadas o número secreto não for acertado, ele será revelado e os jogadores perdem.\n5. Apesar de terem perdido, será mostrada a quantidade de pontos que cada jogador fez.\n\nBom jogo!\n")

    palpites_totais = 0
    acertos_totais = 0
    numeroAcertado = False

    # Loop de rodadas
    for rodada in range(1, 6):
        if numeroAcertado:
            break  # Sai do loop de rodadas
        print("\nA rodada atual é:", rodada)
        for jogador in jogadores:
            palpite = int(input(f"{jogador}, digite o seu palpite: "))
            palpites_totais += 1

            if palpite == resultado:
                print(f"Parabéns, {jogador}! Você acertou o número secreto!")
                acertos_totais += 1
                numeroAcertado = True
                break  # Sai do loop de rodadas
            elif palpite < resultado:
                print("O número secreto é maior que o seu palpite!")
            else:
                print("O número secreto é menor que o seu palpite!")

        if not numeroAcertado: #Dica se ninguém tiver acertado
            if rodada == 2:
                if resultado % 2 == 0:
                    print(f"\nJá que ninguém acertou essa rodada aqui vai uma dica: o número secreto é um número par!") 
                else:
                    print(f"\nJá que ninguém acertou essa rodada aqui vai uma dica: o número secreto é um número ímpar")
            if rodada == 4:
                if primo(resultado):
                    print("\nE mais uma dica: o número secreto é um número primo!")
                else:
                    print("\nE mais uma dica: o número secreto não é um número primo!")


    # Se o loop terminar sem ninguém acertar
    if not numeroAcertado:
        print(f"\nO número secreto era {resultado}. Nunguém acertou.")

    # Estatísticas do jogo
    media_palpites = palpites_totais / (num_jogadores * 5)
    porcentagem_acertos = (acertos_totais / num_jogadores) * 100

    print("\nEstatísticas do jogo:")
    print("Número médio de palpites por rodada:", media_palpites)
    print("Porcentagem de acertos dos jogadores:", porcentagem_acertos, "%")

jogo_adivinhacao()