import requests

# Requisição POST
dados_requisicao = {
    "cpf": 12345678921,
    "nome": "João Guilherme",
    "data_nascimento": "1990-02-01"
}

my_post = requests.post('http://127.0.0.1:5000/usuario', json=dados_requisicao)
print(my_post.json())