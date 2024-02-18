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
    usuarios = get_todos_usuarios()
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario      # retorna os dados do usuário, caso ele exista
    return None     # 'None', caso o usuário respectivo ao CPF passado como argumento não exista
