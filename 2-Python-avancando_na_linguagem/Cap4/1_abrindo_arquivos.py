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

