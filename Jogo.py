import random

#número secreto aleatório
resultado = random.randint(0, 100)

#recebendo o número de jogadores
numJogadores = int(input("Digite o número de jogadores: "))

jogadores = []

for i in range(numJogadores):
    nomeJogador = input(f"Digite o nome do jogador {i+1}: ")
    jogadores.append(nomeJogador)

if (numJogadores <= 0):
    print("Impossível jogar com zero ou menos jogadores, tente novamente")

if (numJogadores > 1):
    print("Vamos iniciar o jogo!\nAs regras são as seguintes:\n1. O objetivo é adivinhar o número secreto.\n2. Cada rodada todos os jogadores tem que dar um palpite.\n3. Ao fim de todas as rodadas será dada uma dica.\n4. Se ao fim de 5 rodadas o número secreto não for acertado ele será revelado e os jogadores perdem.\n5. Apesar de terem perdido será mostrado a quantidade de pontos que cada jogador fez.\n\nBom jogo!\n\n")

#loop de rodadas
for rodada in range(1, 6):
    print("A rodada atual é: ", rodada)
    for jogador in jogadores:
        palpite = int(input(f"{jogador}, Digite o seu palpite: "))
        if palpite == resultado:
            print(f"Parabéns, {jogador}! Você acertou o número secreto!")
            break #sai do loop de rodadas
        elif palpite < resultado:
            print("O número secreto é maior que o seu palpite!")
        else:
            print("O número secreto é menor que o seu palpite!")
    else:
        continue #continua pra proxima rodada
    break #sai do loop de rodadas quando acerta o numero secreto

#se o loop terminar sem ninguem acertar aparece isso ai
else:
    print(f"O número secreto era {resultado}. Ninguém acertou.")