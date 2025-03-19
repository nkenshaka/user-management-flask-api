import pytest
from main import app, db, User

# Configuração do cliente de teste
@pytest.fixture
def cliente():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_users.db'
    app.config['TESTING'] = True
    db.create_all()  # Cria um banco de dados temporário para testes

    yield app.test_client()  # Retorna o cliente de teste

    db.drop_all()  # Limpa o banco de dados após os testes

# Testa a rota de registro de usuário
def test_register(client):
    response = client.post('/register', json={
        'name': 'Test User',
        'email': 'teste@hmail.com',
        'password': 'senhadificil123'
    })
    assert response.status_code == 201  # Verifica se o código de status é 201 (Criado)
    assert b"User created" in response.data  # Verifica se a mensagem "User created" está na resposta

# Testa a rota de login
def test_login(client):
    client.post('/register', json={
        'name': 'Test User',
        'email': 'teste@hmail.com',
        'password': 'senhadificil123'
    })
    response = client.post('/login', json={
        'email': 'teste@hmail.com',
        'password': 'senhadificil123'
    })
    assert response.status_code == 200  # Verifica se o código de status é 200 (OK)
    assert b"access_token" in response.data  # Verifica se o token de acesso está na resposta
