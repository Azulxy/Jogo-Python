import random

#número secreto aleatório
resultado = random.randint(0, 1000)

#recebendo o número de jogadores
jogadores = int(input("Digite o número de jogadores: "))

jogadores = []

for i in range(jogadores):
    nomeJogador = input(f"Digite o nome do jogador {i+1}: ")
    jogadores.append(nomeJogador)

if (jogadores <= 0):
    print("Impossível jogar com zero ou menos jogadores, tente novamente")

if (jogadores > 1):
    print(f"Vamos iniciar o jogo!\nAs regras são as seguintes:\n1. O objetivo é adivinhar o número secreto.\n2. Cada rodada todos os jogadores tem que dar um palpite.\n3. Ao fim de todas as rodadas será dada uma dica.\n4. Se ao fim de 5 rodadas o número secreto não for acertado ele será revelado e os jogadores perdem.\n5. Apesar de terem perdido será mostrado a quantidade de pontos que cada jogador fez.\n\nBom jogo!\n\n")

#cada jogador tem que dar um palpite 

#loop de rodadas
for rodada in range(1, 6):
    print("A rodada atual é: ", rodada)
    print("Jogador ")