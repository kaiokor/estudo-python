# Dar uma pesquisada nos built-in do pyhton, é importante

# IMPORTANTO BIBLIOTECA RANDOM
# é importante deixar as importações no topo do código
# isso serve para deixar claro quais bibliotecas estamos usando
import random

num = random.random() * 100
rando1 = int(num)
rando2 = round(num)

print(rando1)
print(rando2)

num_random = random.randrange(1,101)
# 101 porque ele funciona da mesma forma que o range
# logo, ele irá de 0 até 100
print(num_random)


