# from abc import ABC

# abc é um pacote, nós importamos ele e ele significa abstract base classes, são classes abstratas que servem de base para serem usadas
# não é muito aocnselhavel ficar criando nossas próprias classes bases, é uma coisa um pouco mais avançada 

# se quisermos criar uma classe que dependa da outra, temos que ver se ja não existe um classe base para poder usar, e ja existem diversas base classes

# from collections.abc import MutableSequence

# class Play (MutableSequence):
#     pass


# filmes = Play()
# TypeError: Can't instantiate abstract class Play with abstract methods __delitem__, __getitem__, __len__, __setitem__, insert

# ele esta dizendo todos os métodos que temos que implementar para poder herdar o comportamento e funcionamento todo da mutable sequence

# tem alguma coleção que eu quero implementar? eu quero reforçar que minha classe vai implementar direito?
# então vamos procurar no pacote de coleções, nesse caso foi o MutableSequence, ele vai avisar quais são os métodos,
# as funções que eu tenho que implementar na minha classe para que ela funcione perfeitamente como uma classe ABC

# tem algumas validaçoes que o Duck Type não garante a validação dos comportamentos desejados 

# pra ser sincero, isso não é pra mim ainda


class Funcionario:
    def __init__(self,nome):
        self.nome = nome

    def registra_horas(self,horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes = None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('fez muita coisa, Alurete')

    def bucas_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

# precisamos que nossos funcionarios que são junior pleno e senior, seja da alura, da caelum, dos dois 
# estamos fazendo herança múltipla no caso, estamoss herdando de mais de uma classe

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum):
    pass


jose = Junior()
# jose.bucas_perguntas_sem_resposta()
# jose.busca_cursos_mes
# AttributeError: 'Junior' object has no attribute 'busca_cursos_mes'
# esse não funciona porque ele não herdou essa funcionalidade
# fala atributo no erro porque métodos também são atributos no python

samara = Pleno()
# samara.busca_cursos_do_mes()
# samara.bucas_perguntas_sem_resposta()

samara.mostrar_tarefas()
# fez muita coisa, Alurete
# ORDEM DE EXECUÇÃO
# tinhamos 2 métodos mostrar_tarefas(), uma na classe Alura e outra na class Caelum, a classe filha Pleno pegou o mostrar_tarefas() da alura
# quando criamos uma herança múltipla, ele sempre vai procurar os métodos da primeira classe que aparecer da esquerda para a direita,
# se ele não achar o que procuramos na primeira classe herdada, ele vai procurar na próxima e assim por diante

# o pyhton 3 usa um algorítimo chamado MRO, e o seu funcionamento
# primeira classe que ele vai buscar o método "buscar_tarefas()", ele vai buscar na classe atual, que seria sua própria classe
# pleno >
# depois ele vai buscar na classe mãe do atual, nesse caso temos 2, a Alura e a Caelum 
# mas ele não vai direto para a Alura, antes ele vai para a classe mãe da Alura
# pleno > Alura
# pleno > Alura > Funcionario
# como não tem nenhuma classe acima dela, ela vai passar para a próxima classe herdada do pleno, que seria a Caelum e fazer o mesmo processo de antes
# pleno > Alura > Funcionario > Caelum
# pleno > Alura > Funcionario > Caelum > Funcionario


# temos duas etapas de verificação do algorítimo do MRO
# como vimos antes, temos repetição no meio do processo, onde temos dois Funcionario
# ele tem que tirar essa repetição para ai sim encontrar o lugar que ele vai pegar aquele método
# ele tem que verificar se o primeiro Funcionario que aparece é um "Good Head", se ela for uma boa cabeça, ele pode manter, se não, tem que ser removida
# Good Head quer dizer que não tem nenhuma outra classe que é da mesma hierarquia de Funcionario (que está abaixo de funcionario) que possamos utilziar
# caelum também herda de funcionario, então eu posso usar a Caelum no lugar de funcionario
# ficando assim a lógica
# pleno > Alura > Caelum > Funcionario

# se tem uma classe hendando uma classe mãe, pode ser que ela seja melhor do que a própria classe mãe, por isso tiramos ela da lógica

# para chegar nesse problema, eu comentei o método "mostrar_tarefas()" da Alura



# se euq quiser adicionar um comportamento para converter o meu funcionário para string que não fosse ligada a nenhuma classe mãe, não queremos poluir as classes mães com esse método
# queremos colocar esse método de forma a compartilhar com todas as classes, não precisa ser só um funcionario, pode ser um aluno também
# se quisermos por exemplo colocar, por exemplo, antes no nome dele colocado "hipster", eu possa de alguma forma compartilhar esse código

# imagina que podessemos ter uma classe chamada 'Hipster" que contém essa lógica, esse algorítimo para fazer a conversão do nome e eu posso compartilhar esse código com qualquer classe que eu quiser
# baseada em herança, por exemplo, o Senior ia herdar Alura Caelum e agora Hipster, como que faríamos isto

luan = Senior("Luan")
print(luan)