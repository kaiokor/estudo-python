# Classes e objetos

# DECLARANDO UMA CLASSE
# como boa prática, os nomes de classes devem começar com letra maiúscula
class Cont:    
    # pass serve para deixar passar essa classe caso ela esteja em branco
    pass

# CRIANDO UM OBJETO
print(Cont())
# <__main__.Conta object at 0x0000020BB48FE550>
                            # esse é o endereço em memória onde esse objeto foi criado

# cont é uma instância da classe Cont
# essa variável cont nós chamamos de referência, ela vai guardar o nosso endereço de memória do objeto
# essa variável sabem onde se encontra o objeto
cont = Cont()
print(cont)
# <__main__.Conta object at 0x000002716124E590>

# sempre que chamamos a classe, ela sempre cria um objeto novo
# ISSO TUDO SERIA A CLASSE
class Conta:
    # na hora de criar o objeto, o python pode também executar uma função automaticamente dentro da nossa classe
    # para a gente definir nossos atributos, essas características      
    # funções com __ são funções com um significado especial

    # essa seria uma função construtora, que é chamado automaticamente através do python na hora de construir o objeto
    # na verdade ele constrói o objeto, cria na memória e depois chama essa função
    # def __init__(self):
    #     print('Contruindo objeto...')

    # é apenas uma boa prática adicionar o construtor __init__ em classes, isso não é obrigatório no python
    # caso criar sem ela, a instância não vai dar erro
    # sem o construtor nós precisaríamos definir os atributos depois de instanciar, teríamos o trabalho de descobrir quais atributos definir.
    def __init__(self,numero,titular,saldo,limite): # self é a referência do enredeço que guardamos nosso objeto
        print('Contruindo objeto...{}'.format(self))
        # Contruindo objeto...<__main__.Conta object at 0x00000299B707EC50>

        # usamos o . para acessar o objeto dentro do self
        # esses são os ATRIBUTOS DA CLASSE (o que um objeto tem)        
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    # esses são os MÉTODOS (o que um objeto sabe fazer)
    # eles podem receber qualquer nome, não é como o init
    # ela vai receber de forma automática o self, estramos no objeto através de sua referência, essa seria o self
    def extrato(self):
        print('Saldo {} do titular {}'.format(self.saldo,self.titular))

    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        self.saldo -= valor
    
# conta = Conta()
# Contruindo objeto...<__main__.Conta object at 0x00000205C340EC90>

# conta
# <__main__.Conta object at 0x00000205C340EC90>

# um objeto seria o resultado do que seria entregue com o comando abaixo
# Objetos seria cópias de uma classe
# tem que preencher todos os argumentos
# pode escrever o atributos (titular = "samara"), mas não é obrigatório, só torna o código mais legível
# a ordem dos atributos devem ser estar na mesma ordem que foram definidos no construtor
        # criamos uma classe Conta dentro da referência conta1 por meio da classe Conta, ela sabe onde o objeto foi criado, por meio dela podemos ver esse objeto
conta1 = Conta(1234,'Samara', 55.5, 1000.0)

# ACESSANDO OS ATRIBUTOS ATRAVÉS DO OBJETO
print(conta1.saldo)

# ACESSANDO MÉTODOS
# extrato()
# não conseguimos chamar o método extrato desse jeito
conta1.extrato()
# Saldo 55.5 do titular Samara
conta1.deposita(100)
conta1.saca(50)
conta1.extrato()
# Saldo 105.5 do titular Samara

# quando criamos dois objetos
# usuario = cria_conta(123,"lucas",1200,1500)
# usuario = cria_conta(123,"marcela",1200,1500)
# não conseguimos mais encontrar o primeiro objeto ('nome': lucas), ele é abandonado
# dentro da máquina vitual, da execução do pyhton, um processo que procura objetos que não estão mais sendo utilizados
# esse é o garbage colector (coletor de lixo), ele apaga objetos abandonados

# mas podemos guardar o endereço desse objeto em outra variável
# usuario = cria_conta(123,"lucas",1200,1500)
# outraRef = usuario
# e caso queira derreferenciar essa referência, podemos atribuir o valor None a essa variável
# outraRef = None
# None equivale a nulo de outras linguagens

# ENCAPSULAMENTO DO ACESSO AOS ATRIBUTOS
# até agora estamos acessando as informações do objeto botando a mão dentro do objeto, ou seja, diretamente
# no python não existe o private para colocar antes do atributo,
# o modificador de visibilidade do python é __

class Contas:
    def __init__(self,numero,titular,saldo,limite):
        print('Contruindo objeto...{}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        # código antes de mudar com o uso do @staticmethod
        # self.__codigo_banco = "001"

    def tudo(self):
        print('número: {}, titular: {}, saldo: {}, limite: {}'.format(self.__numero,self.__titular,self.__saldo,self.__limite))
    def extrato(self):
        print('Saldo {} do titular {}'.format(self.__saldo,self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
    
    # esse método funciona, mas vamos melhorar ele com os dois métodos seguintes
    # def saca(self, valor):
              # "essa condição"
    #     if (valor <= (self.__saldo + self.__limite)):
    #         self.__saldo -= valor
    #         print('Valor sacado com sucesso!')
    #     else:
    #         print("O valor {} passou do limite, limite atual {}".format(valor,self.__limite))
    
    # criamos um método para desmenbrar o "essa condição" para melhorar a legibilidade
    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_a_sacar
    
    # como não queremos que alguém acesse esse método, usamos o __ para deixar ele privado

    def saca(self, valor):
            # fica mais fácil de ler, o pode sacar só vai retornar TRUE ou FALSE com a sua lógica
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            print('Valor sacado com sucesso!')
        else:
            print("O valor {} passou do limite, limite atual {}".format(valor,self.__limite))
    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)
    # GET E SET (eu explico mais pra frente)
    def get_limite(self):
        return self.__limite
    
    def set_limite(self, limite):
        self.__limite = limite

    # esse daqui seria o código do banco antes das modificações
    # def codigo_banco(self):
    #     return self.__codigo_banco

    @staticmethod
    def codigo_banco():
        return "001"
    
    

contas1 = Contas(1234,'Samara', 55.5, 1000.0)
contas2 = Contas(123,"marcela",1200,1500)

# conseguimos ainda acessar diretamente dessa forma, ja que o __ faz renomear o atributo real
print(contas1._Contas__saldo)
# o pythom não proíbe de acessar os atributos diretamente, mas avisa que voce esta por conta e risco por meio do _
# além disso, ele não proíbe a alteração dos valores do método, para fazer que o método seja constante, devemos escrever seu atributo em UPPERCASE o nome do atributo
contas1.__saldo=3000

print(contas1.__saldo)
# 3000
print(contas1.tudo())
# número: 1234, titular: Samara, saldo: 55.5, limite: 1000.0

# ele apenas indica que o atributo é privado
# o jeito certo é acessar por meio dos métodos
print(contas1.extrato())
# 55.5

# O prefixo __ não impede a alteração do atributo, mas sim do seu valor
# contas1._Contas__saldo = 200
# mas se colocar desse jeito, ele muda o valor, não entendi muito bem o porque :/

# podemos fazer métodos privados, eles só sãoa acessíveis dentro da sua classe


# TESTANDO O MÉTODO TRANSFERE
contas2.transfere(10,contas1)

print(contas1.tudo())
# número: 1234, titular: Samara, saldo: 65.5, limite: 1000.0
print(contas2.tudo())
# número: 123, titular: marcela, saldo: 1190, limite: 1500

# na teoria, só vamos usar métodos dentro da classe caso elas usem o termo self em alguma parte do código, um método que se relaciona diretamente com a sua classe
# uma class  deve ter apenas uma razão para mudar, uma responsabilidade única, uma razão para existir, não assumir responsabilidades que não são delas
# esse seria o S do princípio SOLID

# GET e SET
# são métodos epeciais para obter ou modificar
# se quiser acessar apenas um atributo, vai ter que criar um método
# se for um só pra retornar dados, temos que chamar de get_nome_do_atributo
# se for um só pra setar dados, temos que chamar de set_nome_do_atributo
# ele nunca retorna algo, ele muda algo
# só crie gets e sets quando forem realmente precisos
print(contas1.get_limite())
# 1000.0
novo_limite = contas1.set_limite(5000.0)
print(contas1.get_limite())
# 5000.0
print(contas1.tudo())
# número: 1234, titular: Samara, saldo: 65.5, limite: 5000.0
# voltando com o valor original
novo_limite = contas1.set_limite(1000.0)

# TESTANDO CONDIÇÕES DO MÉTODO SACA()
contas1.saca(2000)
# O valor 2000 passou do limite, limite atual 1000.0
contas1.saca(500)
# Valor sacado com sucesso!

# digamos que queremos saber o código do banco, mas para sabermos dele temos que criar uma conta e usar o seguinte código
# print(contas1.codigo_banco())
# 001

# ja que ele é um código comun entre as contas, o código do banco não depende do objeto aqui
# esses métodos que não dependem de um objeto (não tem o self), aqueles que não tem referência
# são considerados métodos da classe, chamados de MÉTODOS ESTÁTICOS
# para declarar eles, usamos @staticmethod
print(Contas.codigo_banco())   
# 001
