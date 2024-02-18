import requests

# Requisição POST
dados_requisicao = {
    "cpf": 12345672222,
    "nome": "Joane H",
    "data_nascimento": "1980-12-01"
}

my_post = requests.post('http://127.0.0.1:5000/usuario', json=dados_requisicao)
print(my_post.json())

#my_get = requests.get('http://127.0.0.1:5000/usuario/12345678900')
#print(my_get.json())
