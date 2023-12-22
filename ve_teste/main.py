from fastapi import FastAPI, Query
import requests
app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da programação!
    
    '''
    return {'Hello':'World'}

@app.get('/api/restaurantes/')
										# esse restaurante é uma variável que vamos settar o valor pela URL
																	# esse é o valor que settamos pela URL 
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes  
    
    '''
    url ='https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

	# se tudo estiver ok
    if response.status_code == 200:

		#transformando a api em um json
        dados_json = response.json()

		# se a variável for nenhuma
        if restaurante is None:

			# ele retorna um dicionário com a lista de dados
            return {'Dados':dados_json}
        
		# uma lista para armazenar os items que procuramos
        dados_restaurante = []

		# para cada item em dados, esse seria um exemplo de um item nesta api
		# {"Company":"McDonald’s","Item":"Hamburger","price":32.42,"description":"Uma explosão de sabores em cada mordida."}
        for item in dados_json:

			# se Company tem o mesmo valor da variável que settamos
            if item['Company'] == restaurante:

				# jogamos esse dado dentro da lista dados_restaurante
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })

		# definindo um retorno personalizado para mostrar os resultados econtrados
        return {'Restaurante':restaurante,'Cardapio':dados_restaurante}

    else:

		# exibe uma mensagem caso dê erro
        return {'Erro':f'{response.status_code} - {response.text}'}