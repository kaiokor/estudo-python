class Cliente:
    def __init__(self,nome):
        # para o property funcionar, temos que deixar o nosso atributo privado, se não, vai dar erro
        self.__nome = nome

    @property
    def nom(self):
        print("chamando @property nome()")
                        # title deixa a primeira letra maiúscula
        return self.__nome.title()
    
    @nom.setter
    def nome(self,nome):
        print("chamando setter nome()")
        self.__nome = nome

cliente1 = Cliente('samara')

print(cliente1.nom)