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
