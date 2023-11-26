print('Bem vindo ao jogo de adivinhação!')
num_secreto = 43
num_tentativas = 3


for rodada in range (1,num_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, num_tentativas))
    resp = int(input('Digite um número: '))

    if (resp < 1):
        print('Você deve digitar um número entre 1 e 100!')
        continue
        # CONTINUE
        # ele não sai do laço, apenas da iteração
        # ele faz voltar para o início, que seria o FOR

    acertou = num_secreto == resp
    maior = num_secreto < resp
    menor = num_secreto > resp

    if (acertou):
        print('Você acertou!')
        break
        # BREAK
        # faz sair do seu laço de repetição
    elif (maior):
        print('Seu chute foi maior do que o número secreto')
    else:
        print('Seu chute foi menor do que o número secreto')

    num_tentativas -= 1


