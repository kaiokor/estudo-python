# aqui vamos começar a mexer com funções
# funcao seria o DEF nos outros dois arquivos
# def jogar():
# usamos funções para reaproveitar códigos

# def soma(a, b):
#      return a + b

# no código acima, retornamos a função soma o resultado da soma de a + b


import forca
import adivinhacao
# importando outras pastas
# só usar import e o nome da pasta que estamos querendo

print("(1) - Forca")
print("(2) - Adivinhacao")

jogo = int(input("Escolha um jogo: "))

if (jogo == 1):
    print('Jogando Forca!')
    forca.jogar()
    # executa uma função da outra pasta
    # usa o nome do import e a função do outro arquivo
elif (jogo == 2):
    print('Jogando Adivinhação!')
    adivinhacao.jogar()