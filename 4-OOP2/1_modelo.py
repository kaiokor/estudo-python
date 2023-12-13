# modelo é o nome que a gente da para quando estamos criando conceitos de classes que vão representar um domínio no nosso sistema

# especialização é o ato de se fazer classes mais específicas

class Programa:
     def __init__(self, nome, ano):
                           # o title deixa todas as palavras com a primeira maiúscula 
          self._nome = nome.title()
          self.ano = ano
          self._likes = 0


     @property
     def likes(self):
         return self._likes
    
     @property
     def nome(self):
         return self._nome
    
     @nome.setter
     def nome(self,novo_nome):
         self._nome = novo_nome
            # informando a classe mãe, agora filme esta herdando coisas da classe mãe
            # quando fazemos herança, estamos herdando todas as comportamentos da classe mãe, menos alguns
            # aqui ele não recebe o __nome, ele recebe _Programa__nome, ja que ele esta herdando algo "privado"
            # ou seja, valores privados não vão para classes filhas

            # para resolver isso, usamos apenas um _ e não dois, ele ainda continua privado

     def dar_likes(self):
         self._likes += 1

     # rodando o código com os métodos das classes Filme e Serie sem o método abaixo, ainda funciona
     # def imprime(self):
     #      print(f'Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}')

     # o jeito certo de usar o método de cima seria usando esse aqui de baixo
     # ele é uma representação textual
     # na verdade, essa é só uma base, ja que esta em uma classe mãe, as classes filhas vão pegar essa base e sobrescreves dentro de suas classes com seus atributos próprios
     def __str__(self):
          return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes}'


     
# class Filme(Programa):
#     def __init__(self, nome, ano, duracao):
#           self.__nome = nome.title()
#           self.ano = ano
#           self.duracao = duracao
#           self.__likes = 0



class Filme(Programa):
     def __init__(self, nome, ano, duracao):
          # temos uma função que chama um método ou uma funcionalidade da nossa classe mãe, ela é a supper()
                  # a unica diferença é que não estamos declarando o __init__, logo, não precisamos do SELF
          super().__init__(nome, ano)
          self.duracao = duracao

     def __str__(self):
         return f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} - Likes: {self.likes}'

    
class Serie(Programa):

     # a = "palavras não bastam"
     # esse seria um exemplo de atributo da classe
     # ele pode ser usado por toda a classe, bsata ela ligado a classe ao invés de ligado à instância self
     # podemos alterar o valor desse atributo
     def __init__(self, nome, ano, temporadas):
          super().__init__(nome, ano)
          self.temporadas = temporadas

     def __str__(self):
          return f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self.likes}'
# classe Playlist antes de ser modificada   
# voltamos pra ela de qqualquer forma
# voltamos por que não sabemos direito como a classe list funciona e qual são as limitações que ela tem, então voltamos pois temos mais controle sobre essa forma
# não queremos que nossa classe faça um monte d ecoisa que nem sabemos oque é, não é uma boa prática
# usando o list, o parâmetro 'programa' estáva preso ao list apenas, não podendo ser um dicionário por exemplo
class Playlisty:
     def __init__(self,nome,programas):
          self.nome = nome
          self._programas = programas

     # com essa função conseguimos listar os dados e tudo mais, só para proteger um pouco esse atributo programas
     @property
     def listagem(self):
          return self._programas

     @property
     def tamanho(self):
                 # eu não entendi direito, mas na teoria isso vai tirar o problema dele ser só list   
          return len(self._programas)



               # estamos herdando da classe list, ou seja, ela esta pegando as informações do list
class Playlist(list):
         # do jeito que estamos fazendo esse inicializador, estamos sobrescrevendo o inicializador do list
         # mas qual escolher, esse ou o do list
         # o list ja recebe uma lista preparada pra poder ser inicializada por aquel objeto, mas o nosso tem um nome
         # se usar o do list, não temos o nome, se o usar o nosso, não vamor ter o benefício do list
         # o jeito para usar os dois é usando o método inicializador da nossa super classe
     def __init__(self,nome,programas):
          self.nome = nome
          # para definir nossa lista de programas, na verdade estanos definindo a lista de programas que esta na list, e como a classe Playlist é uma list, vamos definir como super
          # self.programas = programas
          # o super esta se referindo a list, que é nossa classe mãe
                           # passamos programas para dentro do inicializador do list                    
          super().__init__(programas)

class Play:
     def __init__(self,nome,programas):
          self.nome = nome
          self._programas = programas

     @property
     def listagem(self):
          return self._programas

     # @property
     # def tamanho(self):
     #      return len(self._programas)
     
     def __len__(self):
          return len(self._programas)
     

     # esse método define alguém que é iterável 
                           # precisamos de um item para ser repassado para nossa lista interna que estamos usando, que nesse caso seria programas
     def __getitem__(self, item):
          print(item)
          return self._programas[item]

vingadores = Filme('os vingadores', 2018, 160)
atlanta = Serie('atlanta - o filme',2018,2)
tmep = Filme('Todo Mundo em Pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Temporadas: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')

print('')
atlanta.nome = 'banana'
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')


filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana1 = Playlist('Fim de semana',filmes_e_series)
playlist_fim_de_semana2 = Playlisty('Fim de semana',filmes_e_series)
playlist_fim_de_semana3 = Play('Fim de semana',filmes_e_series)


print('')
# polimorfismo
# É quando não importa a classe sendo usada, contanto que esta classe herde de uma superclasse específica.
# Um código que espera uma superclasse, pode receber qualquer classe filha, reduzindo a quantidade de ifs às vezes, pois não precisamos mais verificar o tipo da classe.
# o polimorfismo é a ideia de usar qualquer subclasse no lugar de uma superclasse.
# podemos fazer um for que não se preocupa com o tipo que está la dentro
for programa in filmes_e_series:
     # print(f'Nome: {programa.nome} - Ano: {programa.ano} - Temporadas: {programa.temporadas} - Likes: {programa.likes}')
     # usar esse tipo de print da erro, porque um dos valores pode não ter o atributo 'temporadas'

     # para resolver isso, colocamos uma condição, podendo ser em apenas uma linha
                # deixa esse valor se a condição for verdadeira                    
                                    # has atribute -> se programa tem o atributo 'duracao'
                                                                      # setta esse valor se a condição for falsa
     # detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
     # print(f'Nome: {programa.nome} - Ano: {programa.ano} - Temporadas: {detalhes} - Likes: {programa.likes}')

     # tive que comentar o código para reduzir os ifs, tem um jeito melhor de fazer, que é chamando o método da superclasse
     # a gente tem que ter uma sobrescrevre a função imprime da nossa classe mãe
     
     # programa.imprime()
     
     # quando chamamos esse imprime, não importa o tipo de objeto, ele vai chamar o método imprime de quem tiver o método imprime

     # ainda não é a melhor forma de usar o "imprime", a melhor forma é usando a linguagem do python
     # temos uma outra forma de fazer representação textual no python, na verdade temos duas
     # a primeira é com string, que seria o que o método print faz, ela pega o objeto ela recebou e tenta mostrar como string
     # por de baixo dos panos ele faz o seguinte, em vez de
     # print(1234)
     # ele faz
     # print(str(1234))

     # o python tem alguns métodos, os chamados dunder methods, que significa double underscore, ou dois underlines
     # assim como o __init__, temos que ter na classe, mas não é obrigatório, mas é bom ter um método especial que faz mostrar aquela classe, representar o objeto daquela classe, textualmente
     # esse método especial seria o __str__
     # quando usamos ele, não podemos usar o print dentro dele
     # ele espera que retorne um valor, que é o valor como string, que é aquele objeto que estamos tentando representar
     print(programa)

print('')

print(f'Tamanho da playlist: {len(playlist_fim_de_semana1)}')

# um jeito de ver se tem um elemennto dentro da lista
print(f'Demolidor esta nesssa playlist?: {demolidor in playlist_fim_de_semana1}')
# se for rodar o for em o .programas, vai dar erro falando que é uma lista nãop iterável
# ja que temos umas string no meio
                                       # por isso escolhemos percorrer apenas a lista
for programa in playlist_fim_de_semana1:
     print(programa)

print(playlist_fim_de_semana1)
# mas para fazer isso, temos que saber mais ou menos a estrutura da classe Playlist 
# como que ela funciona, se tem uma lista de programas la dentro, qual o nome da variável etc

# encapsulamento é deixar para a parte de fora o que queremos que a parte de fora interaja 

print('')

# esse daqui é só pra funcionar com a Playlisty
print(f'Tamanho da playlist: {len(playlist_fim_de_semana2.listagem)}')
for programa in playlist_fim_de_semana2.listagem:
     print(programa)

# meio que vimos as vantagens da herança de um iterável e as desvantagens dele também

# temos uma forma para fazer uma classe ser considerada iterável sem recorrer à herança
# e essa forma é por meio do método __getitem__, ele representa o comportamento de uma sequência que consegue ser iterável, funcinando mais ou menos como uma lista
# não é exatamente uma lista por que a lista tem mais comportamentos, mas ainda conssguimos iterar para uma lista, conseguimos usar um IN por exemplo
# com ele não precisamos dizer que ele é do tipo list por exemplo, apenas que ele tem que se comporta como um objeto daquele tipo
print('')
print(f'Tamanho da playlist: {len(playlist_fim_de_semana3.listagem)}')
for programa in playlist_fim_de_semana2.listagem:
     print(programa)

# len(playlist_fim_de_semana3)
# TypeError: object of type 'Play' has no len()

# não conseguimos ver o tamanho
# temos também um método para que algo tenha objeto do tipo sized, que seria algo que tem tamanho
# basta usar __len__
print(len(playlist_fim_de_semana3))

# duck typing, é a ideia de que não precisa ser um pato, eu vou olhar uma ave e não vamos saber exatamente se é um pato, não queremos saber
# só queremos saber se ela faz quack como um pato, se voa como um pato e se anda como um pato
# no python funciona da mesma forma, só queremos saber "se ele se comporta como", então não precisamos nos preocupar com a tipagem


# o que que embasa esses métodos com __
# existe um conceito chamado "Python Data Model" que tem a ideia de que todo objeto em python pode se comportar de um jeito que vai ficar compatível e mais próximo da linguagem
# e de toda aquela ideia idiomática da linguagem no funcionamento do python, com ja vimos que o len é um pouco diferente das outras linguagens


# inicialização          __init__                                          obj = Novo()
# Representação          __str__, __repr__                                 print(obj), str(obj), repr(obj)
# Container, sequencia   __contains__, __iter__, __len__, __getitem__      len(obj), item in obj, for i in obj, obj[2:3]
# numéricos              __add__, __sub__, __mul__, __mod__                obj + outro_obj, obj * obj


# realmente, tudo oque fizemos até agora esta girando no mundo dos objetos do python
# se quisermos adicionar uma item na nossa playlist, não poderiamos fazer isso usando o append, ja que não herdamos o método append da estrutura de lista
# para isso, teremos que usar o __add__


# Extensão acontece quando temos uma relação é um entre subclasse e superclasse.
# Quando fazemos composição, estamos diminuindo o acoplamento


# agora temos que fazer todas as classes filhas sejam também __getitem__
# mas isso eu vou deixar para a próxima página







# MÉTODOS ESTÁTIVOS E DE CLASSE


# temos também os chamados MÉTODOS DA CLASSE, ele é parecido com os staticmethods
# quando criamos ele, temos acesso aos atributos da classe
class Funcionario:
     prefixo = 'Instrutor'

     @classmethod
               # ao invés do self, passamos cls como método, cls é uma conveção. assim como o self
     def info(cls):
          return f'Esse é um {cls.prefixo}'


# métodos estáticos, ja vimos antes
# a diferença é que não precisamos passar nenhum primeiro argumento fixo para o método estático
# não é possível acessar as informações da classe, mas o método estático é acessível a partir da classe e também da instância
class FolhaDePagamento:
    @staticmethod
    def log():
        return f'Isso é um log qualquer'
# print(Funcionario.info())
# print(FolhaDePagamento.log())


# sempre que usar métodos estáticos em classes que contém herança, veja se não está tentando acessar alguma informação da classe a partir do método estático
# isso pode dar alguns problemas, tanto que não é recomendável usar o staticmethod, já que ela poderia ser substituida por uma simples função no corpo do módulo
# outros entendem que os métodos estáticos fazem sentido sim e que devem ser vistos com responsabilidade das classes

