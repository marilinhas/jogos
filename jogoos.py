import forca
import adivinhacao

print("*********************************")
print("   Bem vindo ao Jogos da Mari!   ")
print("*********************************")
print("        Escolha seu jogo!        ")
print("*********************************")
print("(1) Forca (2) Adivinhação")
jogo = int(input("      Qual o jogo?      "))
if (jogo==1):
    print("Jogando Forca")
    forca.jogar()
elif (jogo==2):
    print("Jogando adivinhação")
    adivinhacao.jogar()


