import random
def jogar():



    msg_de_abertura()
    palavra_secreta = carrega_palavras_secretas()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    print (letras_acertadas)

    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto (chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print ("Ops! Você errou restam {} tentativas".format (7 - erros))
            desenha_forca (erros)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print (letras_acertadas)

    if (acertou):
        imprime_msg_vencedor ()

    else:
        imprime_msg_perdedor (palavra_secreta)

    print ("Fim de jogo")










def msg_de_abertura():
    print ("*********************************")
    print ("Bem vindo ao jogo de Forca!")
    print ("*********************************")

def carrega_palavras_secretas():
    arquivo = open ("palavra.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip ()
        palavras.append (linha)

    arquivo.close ()
    numero = random.randrange (0, len (palavras))
    palavra_secreta = palavras[numero].upper ()
    return (palavra_secreta)

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input ("Qual letra?")
    chute: str = chute.strip ().upper ()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
            print ("uhul, temos a letra {}".format (chute))
        index += 1

def imprime_msg_vencedor():
    print ("Parabéns! Você ganhou, que tal outra partida?!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def imprime_msg_perdedor(palavra_secreta):
    print ("Poxa, você foi enforcado! Você perdeu,tente outra vez!")
    print ("A palavra era {}".format (palavra_secreta))
    print ("    _______________         ")
    print ("   /               \       ")
    print ("  /                 \      ")
    print ("//                   \/\  ")
    print ("\|   XXXX     XXXX   | /   ")
    print (" |   XXXX     XXXX   |/     ")
    print (" |   XXX       XXX   |      ")
    print (" |                   |      ")
    print (" \__      XXX      __/     ")
    print ("   |\     XXX     /|       ")
    print ("   | |           | |        ")
    print ("   | I I I I I I I |        ")
    print ("   |  I I I I I I  |        ")
    print ("   \_             _/       ")
    print ("     \_         _/         ")
    print ("       \_______/           ")
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar ()


