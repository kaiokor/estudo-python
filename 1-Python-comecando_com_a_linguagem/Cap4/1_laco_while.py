print('Bem vindo ao jogo de adivinhação!')
num_secreto = 43
num_tentativas = 3
# WHILE
while (num_tentativas > 0):
    resp = int(input('Digite um número: '))

    acertou = num_secreto == resp
    maior = num_secreto < resp
    menor = num_secreto > resp

    if (acertou):
        print('Você acertou!')
    elif (maior):
        print('Seu chute foi maior do que o número secreto')
    else:
        print('Seu chute foi menor do que o número secreto')

    num_tentativas -= 1