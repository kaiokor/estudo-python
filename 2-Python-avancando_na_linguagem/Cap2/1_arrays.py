# ARRAYS (LISTAS)
# array é do tipo list

# é uma boa dar uma olhada na documentação das arrays

# ACHANDO VALOR NA ARRAY
valores = [0,1,2,3,'x']
print(valores[4])
# x

# OPERADOR IN
# podemos usar ele para ver se temos um elemento nessa lista
if (1 in valores):
    print('Temos esse número')


# MIN e MAX
# não da para usar min e max caso tenha uma string no meio da array
valor = [0,0,1,2,3]
print(min(valor))
# 0
print(max(valor))
# 3

# LEN
# mostra o tamanho da array
print(len(valor))

# APPEND e POP
print(valor)
# [0, 1, 2, 3]

# APPEND
# adiciona um valor na array
valor.append(7)
print(valor)
# [0, 1, 2, 3, 7]

# POP
# exclui o ultimo elemento da array
valor.pop()
print(valor)
# [0, 1, 2, 3]

# FUNÇÃO COUNT
# conta quantas vezes um elemento aparece na lista
print(valor.count(0))
# 2

# FUNÇÃO INDEX
# retorna o índice do primeiro elemento que procuramos em uma lista
# ela vai dar erro caso procure um elemento que não exista
# use um IN para evitar esse erro, isso é uma boa prática
if 2 in valores:
    print('Index:',valor.index(2))
# 3

# DEL
# apaga um valor
valores = ["a","b","c","d","e"]
del(valores[0])


# VARIAVEL DE INDICE
# é uma variável que armazena a posição de um elemento me uma coleção de dados
# como um array ou uma string
# o índice é geralemente um número inteiro que representa a posição do elemento dentro da coleção

numeros = [10, 20, 30]

for i in range(len(numeros)):
    print("O elemento na posição", i, "é", numeros[i])

# nesse caso, o índice seria o "i" ja que usamos ela para percorrer a array

