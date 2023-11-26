# idade1 = 10
# idade2 = "20"
# print(idade1 + idade2)

# não é possivel executar o código acima, ele da erro
# isso acontece porque não podemos realizar uma operação de soma com string

idade1 = 10
idade2 = int("20")
print(idade1 + idade2)
# 30



nome = "Nico"
sobrenome = "Steppat"
print(nome + sobrenome)
# NicoSteppat

# O + não soma, ele concatena as duas strings
# para ter espaço entre as duas strings, use , no lugar de +

nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome)
# Nico Steppat

print(5 * "20")
# 2020202020
# tem essa função também no python