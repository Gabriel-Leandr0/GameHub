import forca
import adivinhacao


print("🎮-------------------------------------🎮")
print("🕹️ Bem vindo a central de jogos Python 🕹️ ")
print("🎮-------------------------------------🎮")
print("Selecione seu jogo:")
print("(1) Forca (2) Adivinhação")
jogo = int(input())

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando Adivinhação")
    adivinhacao.jogar()

