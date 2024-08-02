import mysql.connector
from flask import Flask
from flask_mysqldb import MySQL
from flask import Flask, request, jsonify
from mysql.connector import Error

app = Flask(__name__)

# Conexão do banco de dados
conexao = mysql.connector.connect(
    host="192.168.0.161",
    user="root",
    password="Root",
    database="LIVRARIA"
)

# Configurações do banco de dados
db_config = {
    'host': '192.168.0.161',
    'database': 'LIVRARIA',
    'user': 'root',
    'password': 'Root',
    'autocommit': True
}

mysql = MySQL(app)

#Código antí injeção MYSQL não utiliza variavel global
class DatabaseHelper:
    def __init__(self):
        self.db_config = {
            'host': '192.168.0.161',
            'database': 'LIVRARIA',
            'user': 'root',
            'password': 'Root',
            'autocommit': True
        }

# Função para conectar ao banco de dados
def conectar(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            return connection
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

# Operações CRUD para a tabela Editora
@app.route('/editora', methods=['POST'])
def inserir_editora():
    data = request.json
    email = data.get('E_mail')
    nome_contato = data.get('Nome_contato')
    fk_telefone = data.get('fk_Telefone_Telefone_PK')

    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO Editora (E_mail, Nome_contato, fk_Telefone_Telefone_PK) VALUES (%s, %s, %s)"
            cursor.execute(query, (email, nome_contato, fk_telefone))
            return jsonify({'message': 'Dados inseridos na tabela Editora com sucesso.'}), 200
        except Error as e:
            return jsonify({'error': f"Erro ao inserir dados na tabela Editora: {e}"}), 500
        finally:
            cursor.close()
            connection.close()

# Operações CRUD para a tabela Livro
@app.route('/livro', methods=['POST'])
def inserir_livro():
    data = request.json
    titulo = data.get('Titulo')
    ano_publicacao = data.get('Ano_publicacao')
    autor = data.get('Autor_a')
    editora = data.get('Editora')
    categoria = data.get('Categoria')
    valor = data.get('Valor')
    isbn = data.get('ISBN')
    fk_editora = data.get('FK_Editora_Cod_editora')
    fk_estoque_livro = data.get('FK_ESTOQUE_Cod_livro')
    fk_estoque_editora = data.get('FK_ESTOQUE_Cod_editora')

    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO LIVRO (Titulo, Ano_publicacao, Autor_a, Editora, Categoria, Valor, ISBN, Cod_livro, FK_Editora_Cod_editora, FK_ESTOQUE_Cod_livro, FK_ESTOQUE_Cod_editora) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (titulo, ano_publicacao, autor, editora, categoria, valor, isbn, None, fk_editora, fk_estoque_livro, fk_estoque_editora))
            return jsonify({'message': 'Dados inseridos na tabela Livro com sucesso.'}), 200
        except Error as e:
            return jsonify({'error': f"Erro ao inserir dados na tabela Livro: {e}"}), 500
        finally:
            cursor.close()
            connection.close()

# Função para conectar ao banco de dados
def conectar():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Operações CRUD para a tabela Editora
@app.route('/editora', methods=['POST'])
def inserir_editora():
    data = request.json
    email = data.get('E_mail')
    nome_contato = data.get('Nome_contato')
    fk_telefone = data.get('fk_Telefone_Telefone_PK')

    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO Editora (E_mail, Nome_contato, fk_Telefone_Telefone_PK) VALUES (%s, %s, %s)"
            cursor.execute(query, (email, nome_contato, fk_telefone))
            return jsonify({'message': 'Dados inseridos na tabela Editora com sucesso.'}), 200
        except Error as e:
            return jsonify({'error': f"Erro ao inserir dados na tabela Editora: {e}"}), 500
        finally:
            cursor.close()
            connection.close()

# Operações CRUD para a tabela Livro
@app.route('/livro', methods=['POST'])
def inserir_livro():
    data = request.json
    titulo = data.get('Titulo')
    ano_publicacao = data.get('Ano_publicacao')
    autor = data.get('Autor_a')
    editora = data.get('Editora')
    categoria = data.get('Categoria')
    valor = data.get('Valor')
    isbn = data.get('ISBN')
    fk_editora = data.get('FK_Editora_Cod_editora')
    fk_estoque_livro = data.get('FK_ESTOQUE_Cod_livro')
    fk_estoque_editora = data.get('FK_ESTOQUE_Cod_editora')

    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO LIVRO (Titulo, Ano_publicacao, Autor_a, Editora, Categoria, Valor, ISBN, Cod_livro, FK_Editora_Cod_editora, FK_ESTOQUE_Cod_livro, FK_ESTOQUE_Cod_editora) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (titulo, ano_publicacao, autor, editora, categoria, valor, isbn, None, fk_editora, fk_estoque_livro, fk_estoque_editora))
            return jsonify({'message': 'Dados inseridos na tabela Livro com sucesso.'}), 200
        except Error as e:
            return jsonify({'error': f"Erro ao inserir dados na tabela Livro: {e}"}), 500
        finally:
            cursor.close()
            connection.close()

# Operações CRUD para a tabela Pedido
@app.route('/pedido', methods=['POST'])
def inserir_pedido():
    data = request.json
    data_pedido = data.get('Data')
    valor_pedido = data.get('Valor_pedido')
    cod_cliente = data.get('Cod_cliente')
    cod_pedido = data.get('Cod_pedido')
    fk_cliente = data.get('FK_cliente_Cod_cliente')

    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO PEDIDO (Data, Valor_pedido, Cod_cliente, Cod_pedido, FK_cliente_Cod_cliente) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (data_pedido, valor_pedido, cod_cliente, cod_pedido, fk_cliente))
            return jsonify({'message': 'Dados inseridos na tabela Pedido com sucesso.'}), 200
        except Error as e:
            return jsonify({'error': f"Erro ao inserir dados na tabela Pedido: {e}"}), 500
        finally:
            cursor.close()
            connection.close()
# Operações CRUD para a tabela mklog_cliente_login_admin_amazena_login
@app.route('/cliente', methods=['POST'])
def inserir_cliente():
    data = request.json
    nome = data.get('Nome')
    cod_cliente = data.get('Cod_cliente')
    ie = data.get('IE')
    cnpj = data.get('CNPJ')
    cpf = data.get('CPF')
    rg = data.get('RG')
    cliente_tipo = data.get('cliente_TIPO')

    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO mklog_cliente_login_admin_amazena_login (Nome, Cod_cliente, IE, CNPJ, CPF, RG, cliente_TIPO) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (nome, cod_cliente, ie, cnpj, cpf, rg, cliente_tipo))
            return jsonify({'message': 'Dados inseridos na tabela mklog_cliente_login_admin_amazena_login com sucesso.'}), 200
        except Error as e:
            return jsonify({'error': f"Erro ao inserir dados na tabela mklog_cliente_login_admin_amazena_login: {e}"}), 500
        finally:
            cursor.close()
            connection.close()

# Operações CRUD para a tabela pedidos
@app.route('/pedidos', methods=['POST'])
def inserir_pedidos():
    data = request.json
    # Adicione as variáveis conforme necessário
    # Implemente a operação CRUD para a tabela pedidos

# Operações CRUD para a tabela Telefone
@app.route('/telefone', methods=['POST'])
def inserir_telefone():
    data = request.json
    telefone_pk = data.get('Telefone_PK')
    telefone = data.get('Telefone')

    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO Telefone (Telefone_PK, Telefone) VALUES (%s, %s)"
            cursor.execute(query, (telefone_pk, telefone))
            return jsonify({'message': 'Dados inseridos na tabela Telefone com sucesso.'}), 200
        except Error as e:
            return jsonify({'error': f"Erro ao inserir dados na tabela Telefone: {e}"}), 500
        finally:
            cursor.close()
            connection.close()

# Operações CRUD para a tabela impedimento
@app.route('/impedimento', methods=['POST'])
def inserir_impedimento():
    data = request.json
    fk_cliente = data.get('fk_mklog_cliente_login_admin_amazena_login_Cod_cliente')

    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO impedimento (fk_mklog_cliente_login_admin_amazena_login_Cod_cliente) VALUES (%s)"
            cursor.execute(query, (fk_cliente,))
            return jsonify({'message': 'Dados inseridos na tabela impedimento com sucesso.'}), 200
        except Error as e:
            return jsonify({'error': f"Erro ao inserir dados na tabela impedimento: {e}"}), 500
        finally:
            cursor.close()
            connection.close()

# Endpoint Flask para conectar ao banco de dados
@app.route('/conectar_banco', methods=['GET'])
def conectar_banco():
    connection = conectar()
    if connection:
        return jsonify({'message': 'Conexão com o banco de dados estabelecida com sucesso.'}), 200
    else:
        return jsonify({'error': 'Erro ao conectar ao banco de dados.'}), 500

if __name__ == "__main__":
    app.run(debug=True)