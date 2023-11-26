# tem uma plataforma chamada PyCharm pra codificar em python

# funcao input()
# ela recebe o que vai ser impresso no console

# INDENTAÇÂO
# o pyhton obriga a ter 4 espaços (1 tab) depois de um bloco de código
# depois dos dois pontos (:) será realizado o comando dependendo da condição

# funcao int()
# chute_str = input("Digite seu número")
# chute = int(chute_str)
# converte uma string para variavel do tipo int

# temos que usar == em coparação, e não =
# = atribui um valor a variável
# == compara valores ou variáveis

print('Bem vindo ao jogo de adivinhação!')
num_secreto = 43

resp = int(input('Digite um número: '))

if (num_secreto == resp):
    print('Você acertou!')
else:
    print('Número errado :(')

