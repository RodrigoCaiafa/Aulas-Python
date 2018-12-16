import random

def jogar():
    print("*********************************")
    print("Bem vindo no jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    numero_jogadas = 0
    tentativa = 0
    pontos_iniciais = 1000
    pontos_perdidos = 0

    print("Selecione o nível de dificuldade:", numero_secreto)
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Digite o nível: "))

    if (nivel == 1):
        numero_jogadas = 20

    elif (nivel == 2):
        numero_jogadas = 10

    elif (nivel == 3):
        numero_jogadas = 5

    else:
        print("Opção inválida. Selecione o nível conforme legenda")

    for tentativa in range(1, numero_jogadas + 1):
        print("Tentativa {} de {}". format(tentativa, numero_jogadas))
        chute = int(input("Digite um número inteiro entre 1 e 100: "))

        if(chute < 1 or chute > 100):
            print("Número inválido. Você deve digitar números entre 1 e 100")
            continue

        if (numero_secreto == chute):
            print("Você acertou! Seu total de pontos é {}.".format(pontos_iniciais))
            break
        else:
            if(chute > numero_secreto):
                print("Você errou! O número secreto é menor")
            elif(chute < numero_secreto):
                print("Você errou! O número secreto é maior")

        pontos_perdidos = round(abs(numero_secreto - chute)/3)
        pontos_iniciais = pontos_iniciais - pontos_perdidos

    print("Fim de jogo!")

if (__name__ == "__main__"):
    jogar()