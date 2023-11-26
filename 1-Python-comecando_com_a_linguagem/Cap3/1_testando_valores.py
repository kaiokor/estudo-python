# a condição ELIF

print('Bem vindo ao jogo de adivinhação!')
num_secreto = 43

resp = int(input('Digite um número: '))

acertou = num_secreto == resp
maior = num_secreto < resp
menor = num_secreto > resp
# essa variável é do tipo bool

if (acertou):
    print('Você acertou!')
elif (maior):
    print('Seu chute foi maior do que o número secreto')
else:
    print('Seu chute foi menor do que o número secreto')

# if acertou | if (acertou)
# os doi tipos estão certos, mas o segundo deixa mais claro