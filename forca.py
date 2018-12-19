import random

def jogar():
    print("*********************************")
    print("***Bem vindo no jogo da forca!***")
    print("*********************************")

    with open("palavras.txt", "r") as arquivo:
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    tentativas = len(palavra_secreta) + (len(palavra_secreta)/2)

    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()
        index = 0

        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            print("Errou! {} Tentativas restantes".format(tentativas))
            tentativas -= 1

        enforcou = tentativas == 0
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("fim de jogo")

if(__name__ == "__main__"):
    jogar()