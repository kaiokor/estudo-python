# palavras chaves sempre começam com letra maiuscula



palavra = "banana"


# ITERAR
# iterar significa receber a cada iteração
# nesse caso será uma letra da palavra
letra_compara = "b"
for letra in palavra:
    if (letra == letra_compara):
        print("Achou!")


# o find procura oque foi solicitado como parâmetro na variável
# e retorna o index, caso ela encontre o que foi pedido
# se não achar, ela retorna o valor -1
print(palavra.find('b'))
# 0

frase = '  a samara   Anda  de   Fiorino. e anda bastante'
# métodos e funções por enquanto são a mesma coisa
# é uma boa dar uma lida em todos os métodos

# METODO CAPTALIZE
# formata para deixar apenas a primeira letra em maiúsculo
print(frase.capitalize())
# Banana

# METODO UPPER E LOWER
# deixa tudo em maiúsculo
print(frase.upper())
# BANANA

# deixa tudo em minúsculo
print(frase.lower())
# banana

# METODO STRIP
# formata os espaços antes e depois da frase, mas não os espaços no meio dela
print(frase.strip())

