# FUNCAO OPEN
# ela abre um arquivo
# open("nome_do_arquivo", "qual_o_modo_de_trabalho")
# Modos de trabalho: w - escrita | r - leitura | a - append

# ao rodar pela primeira vez, vais ser criada uma pasta
# a escrita vai apagar aquele arquivo caso ele exista
# caso não queira apagar, só adicionar conteúdo, use o append

arquivo = open('palavras.txt', 'w', encoding='utf-8')
arquivo.write('banana\n')
arquivo.write('melancia\n')
arquivo.close()

arquivo = open('palavras.txt', 'a',encoding='utf-8')
arquivo.write('morango\n')
arquivo.write('maça\n')
arquivo.close()


# é uma boa prática fechar o arquivo
# quando abrimos um arquivo, o pyhton, por de baixo dos panos, pede ao sistema operacional um canal de comunicação 
# se não fechar, esse canal continuará aberto

arquivo = open('palavras.txt', 'r', encoding="utf-8")
# print(arquivo.read())
# banana
# melancia
# morango
# maça

# for linha in arquivo:
#     print(linha)

# banana

# melancia

# morango

# maça

# read faz ler o arquivo inteiro, colocando o ponteiro de leitura no final do arquivo
# se chamarmos a função read novamente, ja q o ponteiro esta no final do arquivo, nada será lido

# conteudo = arquivo.read()
# print(conteudo)
# conteudo = arquivo.read()
# print(conteudo)

# readline faz ler linha a linha do nosso arquivo
linha = arquivo.readline()
print(type(linha))
# <class 'str'>
print(linha)
#banana
linha.strip()

arquivo.close()

# temos uma sintaxe especial para abertura de arquivos
# o with usa a funcao open
# não precisamos fechar o arquivo com o with
# não é necessário pois o python cuida disso, mesmo com erro ele garante o fechamento do arquivo
with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)

# é bom ir separando o código em funções
# uma função define um escopo, e um escopo significa que as variáveis declaradas dentro delas só são visiveis dentro da sua função
# a convenção é criarmos funções no padrão snake_case
# uma única função, deve apresentar apenas uma única responsabilidade
