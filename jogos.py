import adivinhacao
import forca

def escolha_jogo():
    print("*********************************")
    print("********Escolha o jogo!**********")
    print("*********************************")

    print("(1) jogo da adivinhação (2) jogo da forca")
    jogo = int(input("Selecione o jogo"))

    if (jogo == 1):
        print("Jogo da adivinhação")
        adivinhacao.jogar()

    elif (jogo == 2):
        print("Jogo da forca")
        forca.jogar()

    else:
        print("Número inválido!Selecione a opção conforme a legenda.")

if(__name__ == "__main__"):
    escolha_jogo()