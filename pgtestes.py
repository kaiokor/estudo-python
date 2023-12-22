lista_comida =[]

class Comida:
    lista_comida = []

    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco
        Comida.lista_comida.append(self)

    def __str__(self):
        return f'{self._nome} | {self._preco}'    

class Prato(Comida):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self._descricao = descricao
    
        
    def __str__(self):
        return f'{self._nome} | {self._preco} | {self._descricao}'
    
class Bebida(Comida):
    def __init__(self,nome,preco,tamanho):
        super().__init__(nome,preco)
        self._tamanho = tamanho

    def __str__(self):
        return f'{self._nome} | {self._preco} | {self._tamanho}'


nhoque = Prato('Nhoque', 20.00, 'É um prato de origem')
suco_uva = Bebida('Suco de Uva', 2.00, 'Tem uva')


for item in Comida.lista_comida:
    print(item)
    print(hasattr(item,'_descricao'))
