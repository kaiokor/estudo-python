# paradigma procedural da Orientação a Objetos

# Começando com a orientação a objetos
# a base dela é juntar os dados, as coisas que pertencem a outras juntas em um lugar só
# seria as características de algo, cor azul, tamanho pequeno, chapéu gorro

              # aqui são variáveis que vamos receber quando chamarmos essa função cria_conta  
def cria_conta(numero, titular, saldo, limite):
    # criando lista conta, ela vai armazenar os dados inseridos
    conta = {'numero': numero, "titular":titular, "saldo":saldo, "limite":limite}
    # retornamos a lista para a função
    return conta

# aqui a variável usuario armazena a lista que criamos
usuario = cria_conta(123,"samara",1200,1500)

# lista usuario antes das modificações
print(usuario)

# criamos uma função para criar uma conta por meio de um dicionário
# e quando inserimos os dados, é retornado para a variável usuario nossa lista com os dados escolhidos

# criando função de deposito
# como sempre, apenas criamos as funções, mas não somos obrigados a usar elas
def depositar(conta, valor):
    conta['saldo'] += valor 
    print('Saldo depositado')

# criando função de saque
def sacar(conta, valor):
    conta['saldo'] += valor 
    print('Saldo sacado')

# criando função para consulta de extrato
def extrato(conta):
    print('O saldo é de {}'.format(conta['saldo']))

# chamando funções
extrato(usuario)
depositar(usuario,1000)
sacar(usuario,500)

# lista depois das modificações
# só para saber se mudou mesmo a conta usuario
print(usuario)


# o problema do paradigma procedural, é que todos conseguem modificar os dados de uma lista
# as funções ficam espalhadas e pode acontecer de criarmos uma nova função, sendo que ela sempre esteve lá

