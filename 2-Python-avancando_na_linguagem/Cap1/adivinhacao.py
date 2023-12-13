import random
def jogar():
    print('Bem vindo ao jogo de adivinhação!')
    num_secreto = int(random.randrange(1,101))
    num_tentativas = 3
    num_base = 3

    for rodada in range (1,num_tentativas + 1):

        print('Tentativa {} de {}'.format(rodada, num_base))
        resp = int(input('Digite um número: '))

        if (resp < 1):
            print('Você deve digitar um número entre 1 e 100!')
            continue
        acertou = num_secreto == resp
        maior = num_secreto < resp
        menor = num_secreto > resp

        if (acertou):
            print('Você acertou!')
            break
        elif (maior):
            print('Seu chute foi maior do que o número secreto')
        else:
            print('Seu chute foi menor do que o número secreto')

        num_tentativas -= 1

    print('Número secretpe era: ', num_secreto)
    print('Fim de jogo!')

if(__name__ == "__main__"):
    jogar()
