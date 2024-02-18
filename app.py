from flask import Flask, jsonify, request
import json

# Cria um objeto de aplicação Flask
app = Flask(__name__)

# Caminho para o arquivo que armazena os dados dos usuários
USUARIOS = 'usuarios.json'

# Checa se o arquivo que armazena os dados existe, se não existir, cria um
try:
    with open(USUARIOS, 'r') as file:
        pass
except FileNotFoundError:
    with open(USUARIOS, 'w') as file:
        json.dump([], file)

# Função que retorna todos os usuários armazenados
def get_todos_usuarios():
    with open(USUARIOS, 'r') as file:
        return json.load(file)
    
# Função que retorna um usuário referente a um CPF
def get_usuario(cpf):
    todos_usuarios = get_todos_usuarios()
    for usuario in todos_usuarios:
        if usuario['cpf'] == cpf:
            return usuario      # retorna os dados do usuário, caso ele exista
    return None     # 'None', caso o usuário respectivo ao CPF passado como argumento não exista

# Função que adiciona um novo usuário no arquivo 'usuarios.json'
def add_usuario(usuario):
    todos_usuarios = get_todos_usuarios()
    todos_usuarios.append(usuario)
    with open(USUARIOS, 'w') as file:
        json.dump(todos_usuarios, file)

add_usuario({"cpf": 12632382409, "nome": "Maia Takeguma", "data_nascimento": "2020-05-05"})