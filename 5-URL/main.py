url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
print(url)

# Sanetização da URL
url = url.replace(' ', '')



#Validação da URL
if url =='':
    raise ValueError('A URL está vazia!')

# separa base dos parâmetros
pos_iterrogacao = url.find('?')
url_base = url[0:pos_iterrogacao]
url_parametro = url[pos_iterrogacao+1:]
print(url_base)
print(url_parametro)

# busca o valor de um parâmetro
busca = 'moedaOrigem'
indice_parametro= url_parametro.find(busca)
indice_valor = indice_parametro + len(busca) + 1
indice_e_comercial = url_parametro.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]

print(valor)
# real

a = "\t/a/s"
b = a.strip()
print(b)

