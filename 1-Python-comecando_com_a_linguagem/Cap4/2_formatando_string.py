# INTERPOLAÇÃO DE STRING
# é uma boa dar uma olhada na documentação
num1 = 2
num2 = 4

print("Número 1: {}, Número 2: {}".format(num1,num2))
# Número 1: 2, Número 2: 4
print("Número 1: {1}, Número 2: {0}".format(num1,num2))
# Número 1: 4, Número 2: 2

# f é float
# d é int
print("R$ {:f}".format(1.59))
# R$ 1.590000
print("R$ {:d}".format(4))
# R$ 4
print("R$ {:.2f}".format(1.59))
# R$ 1.59
print("R$ {:.2f}".format(1.5))
# R$ 1.50
print("R$ {:7.2f}".format(1234.5))
# R$ 1234.50
print("R$ {:7.2f}".format(4.5))
# R$    4.50
print("R$ {:07.2f}".format(4.5))
# R$ 0004.50

print('Data {:02d}/{:02d}'.format(9,4))
# Data 09/04
print('Data {:02d}/{:02d}'.format(19,11))
# Data 19/11


# F-STRING (no python 3.6+)
nome = 'Matheus'
print(f'Meu nome é {nome}')
# Meu nome é Matheus

# quando colocamos f antes das aspas, informamos que estamos usando f-string
# o bom dessa função é que podemos passar funções nas variáveis

nome = 'Matheus'
print(f'Meu nome é {nome.lower()}')
# Meu nome é matheus
# que no caso, essa função seria o .lower()