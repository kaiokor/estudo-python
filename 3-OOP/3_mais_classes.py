# ANOTAÇÕES DE PROPRIEDADE
# é usar o @property e o seu setter
# servem para tirar os prefixos get_ e set_

class Cliente:
    def __init__(self,nome):
        # para o property funcionar, temos que deixar o nosso atributo privado, se não, vai dar erro
        self.__nome = nome

    @property
    def nome(self):
        print("chamando @property nome()")
                        # title deixa a primeira letra maiúscula
        return self.__nome.title()
    
    @nome.setter
    def nome(self,nome):
        print("chamando setter nome()")
        self.__nome = nome

cliente1 = Cliente('samara')

print(cliente1.nome)
# Samara

# quando criamos um método de uma classe

# def get_nome(self):
#     return self.__nome.title()

# chamamos ela da seguinte forma

# print(cliente.get_nome())

# mas queremos o tratamento do dado chamando da seguinte forma

# print(cliente1.nome)

# ela parece que estamos acessando o dado direto o atributo do nosso objeto
# para que isso funcione, usamos o @property, ele faz parecer que estamos acessando o valor do atributo
# mas na verdade estamos acessando um método sem os ()

# o @property é apenas para os getter
# para o setter usamos:
# @nome_atributo.setter
cliente1.nome = 'Julia'
print(cliente1.nome)
# Julia

# então não precisamos usar o comando
# cliente1.get_nome('Julia')
# parecendo ainda que estamos inserindo um valor diretamente ao atributo do objeto
