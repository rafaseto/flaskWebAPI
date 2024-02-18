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


# Rota referente à requisição POST
@app.route('/usuario', methods=['POST'])
def req_post_usuario():
    # Dados da requisição no formato json
    dados_requisicao = request.json

    # Checamos se algum campo está faltante
    if 'cpf' not in dados_requisicao:
        return jsonify({'error': 'CPF é um campo obrigatório.'}), 400
    elif 'nome' not in dados_requisicao:
        return jsonify({'error': 'Nome é um campo obrigatório.'}), 400
    elif 'data_nascimento' not in dados_requisicao:
        return jsonify({'error': 'Data de nascimento é um campo obrigatório.'}), 400
    
    # Checamos se o usuário já existe, ou seja, se o CPF já está armazenado
    todos_usuarios = get_todos_usuarios()
    for usuario in todos_usuarios:
        if usuario['cpf'] == dados_requisicao['cpf']:
            return jsonify({'error': 'Usuário já existe!'}), 409

    # Adiciona o usuário ao arquivo de armazenamento 
    add_usuario(dados_requisicao)
    return jsonify({'message': 'Usuário armazenado com sucesso!'}), 201

# Rota referente à requisição GET
@app.route('/usuario', methods=['GET'])
def req_get_usuario(cpf):
    usuario = get_usuario(cpf)
    if usuario == None:
        return jsonify({'error': 'Usuário not found.'}), 404
    return jsonify(usuario), 200