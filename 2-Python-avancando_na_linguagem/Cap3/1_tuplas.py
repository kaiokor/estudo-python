# podemos colocar um range em variáveis
tamanho = range(0,10)

# além disso, ele é considerado uma sequência
# tempos 3 tipos de sequências: list, tuple, range
# mas sequência é tudo aquilo considerado como um conjunto de valores ordenados
# então elas podem ser acessadas por []

# TUPLAS
# é uma lista que não pode ser alterada
# basta usar nome_tupla = ()
dias_semana = ('S','T','Q','Q','S','S','D')
print(dias_semana)
# ('S', 'T', 'Q', 'Q', 'S', 'S', 'D')

p1 = ('Samara', 19)
p2 = ('Nico', 21)

instrutores = [p1,p2]
print(instrutores)
# [('Samara', 19), ('Nico', 21)]
print(instrutores[0][1])
# 19

# TRANSFORMANDO UMA LISTA EM TUPLA
tupla_instrutores = tuple(instrutores)
print(tupla_instrutores)
# (('Samara', 19), ('Nico', 21))

# TRANSFORMANDO UMA TUPLA EM LISTA
lista_instrutores = list(tupla_instrutores)
print(lista_instrutores)
# [('Samara', 19), ('Nico', 21)]

# AGORA
# se precisarmos achar a samara, mas não sabemos o seu índice
# podemos usar dicionários
alunos = {'Samara': 19, 'Nico': 21}

# aqui temos como CHAVE o nome e o VALOR como a idade

print(alunos['Samara'])

# COLECAO SET
# não deixa valores repetidos entrarem, e não é ordenado
colecao = {11122233344, 22233344455, 33344455566}
colecao.add(44455566677) #vai adicionar pois não existe ainda
colecao.add(11122233344) #nao vai adicionar pois este CPF já existe!

# set não possui índice
# por causa disso, não sabemos qual ordem vem o valores quando imprimimos usando SET em um FOR

for i in colecao:
    print(i)

# 11122233344
# 44455566677
# 33344455566
# 22233344455


# List Comprehension
fruta = 'abacaxi'
secreto = ['_' for i in fruta]
print(secreto)

inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]

print(pares)