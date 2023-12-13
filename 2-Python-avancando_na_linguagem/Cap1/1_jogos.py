import forca
import adivinhacao

print("(1) - Forca")
print("(2) - Adivinhacao")

jogo = int(input("Escolha um jogo: "))

if (jogo == 1):
    print('Jogando Forca!')
    forca.jogar()
elif (jogo == 2):
    print('Jogando Adivinhação!')
    adivinhacao.jogar()