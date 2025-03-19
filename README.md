# API RESTful com Flask e JWT

Este é um projeto de uma API RESTful desenvolvida com **Flask**, **SQLAlchemy** e **Flask-JWT-Extended**. A API permite **registro de usuários**, **login com JWT**, **autenticação segura** e manipulação de dados (CRUD). Ideal para demonstrar a criação de APIs seguras com autenticação e persistência de dados.

## Funcionalidades

- **Cadastro de usuários**: Os usuários podem se registrar na aplicação.
- **Login com JWT**: Após o login, um token JWT é gerado e pode ser usado para acessar rotas protegidas.
- **Rotas protegidas**: Algumas rotas exigem autenticação, garantindo a segurança da aplicação.
- **CRUD de usuários**: Capacidade de criar, ler, atualizar e excluir dados dos usuários.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento da API.
- **Flask**: Microframework para criar APIs e aplicações web.
- **SQLAlchemy**: ORM (Object Relational Mapper) utilizado para interagir com o banco de dados.
- **Flask-JWT-Extended**: Extensão para autenticação JWT (JSON Web Token).
- **SQLite**: Banco de dados leve para armazenar as informações dos usuários.

## Instalação

### Requisitos

- **Python 3.x**: A API foi desenvolvida utilizando a versão mais recente do Python.
- **pip**: Gerenciador de pacotes Python.

### Passos para rodar a aplicação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:
    - No Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - No MacOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Execute a aplicação:
    ```bash
    python main.py
    ```

A API estará disponível em `http://localhost:5000`.

## Endpoints da API

### 1. **POST /register** - Criar um novo usuário

- **Body**:
    ```json
    {
        "name": "Nome do Usuário",
        "email": "email@dominio.com",
        "password": "senha123"
    }
    ```
- **Resposta**:
    - Status 201: `{"message": "User created"}`
    - Status 400: `{"error": "Missing required fields"}` ou `{"error": "User already exists"}`

### 2. **POST /login** - Login de um usuário e geração do token JWT

- **Body**:
    ```json
    {
        "email": "email@dominio.com",
        "password": "senha123"
    }
    ```
- **Resposta**:
    - Status 200: `{"access_token": "jwt_token"}`
    - Status 400: `{"error": "Missing required fields"}`
    - Status 401: `{"error": "Invalid credentials"}`

### 3. **GET /protected** - Rota protegida, só acessível com JWT

- **Requer autorização**: O usuário precisa passar um token JWT válido no header `Authorization: Bearer <token>`.
- **Resposta**:
    - Status 200: `{"message": "Hello, Nome do Usuário!"}`

## Contribuições

Sinta-se à vontade para contribuir para este projeto! Se encontrar algum bug ou tiver sugestões de melhorias, crie uma *issue* ou envie um *pull request*.
