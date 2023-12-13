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

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass


# se euq quiser adicionar um comportamento para converter o meu funcionário para string que não fosse ligada a nenhuma classe mãe, não queremos poluir as classes mães com esse método
# queremos colocar esse método de forma a compartilhar com todas as classes, não precisa ser só um funcionario, pode ser um aluno também
# se quisermos por exemplo colocar, por exemplo, antes no nome dele colocado "hipster", eu possa de alguma forma compartilhar esse código

# imagina que podessemos ter uma classe chamada 'Hipster" que contém essa lógica, esse algorítimo para fazer a conversão do nome e eu posso compartilhar esse código com qualquer classe que eu quiser
# baseada em herança, por exemplo, o Senior ia herdar Alura Caelum e agora Hipster, como que faríamos isto

luan = Senior("Luan")
print(luan)

# Senior > Alura > Funiconario e cadastra nome > Caelum > Hipster e pega o "nome" cadastrado no self.nome quando passou pelo Funcionario

# chamamos essa classes pequenes de mixins onde a ideia é não instanciar nenhum objeto dessa classe
# são usada quando não precisamo fazer esse compartilhamento de um comportamento qu enão é o mais importante da classe