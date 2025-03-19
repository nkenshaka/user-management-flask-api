from flask import request, jsonify
from app import app, db
from models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash


# Rota para registro de usuário
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data or not data.get('name') or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Missing required fields"}), 400

    user = User.query.filter_by(email=data["email"]).first()

    if user:
        return jsonify({"error": "User already exists"}), 400

    # Criptografa a senha antes de salvar
    hashed_password = generate_password_hash(data["password"])

    new_user = User(name=data["name"], email=data["email"], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created"}), 201


# Rota para login
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Missing required fields"}), 400

    user = User.query.filter_by(email=data["email"]).first()

    # Verifica a senha criptografada
    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    # Gerar o token JWT
    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), 200


# Rota para atualizar dados do usuário autenticado
@app.route("/update-user", methods=["PUT"])
@jwt_required()
def update_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing required fields"}), 400

    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    # Atualiza apenas os campos enviados
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)

    # Se a senha for enviada, criptografa antes de salvar
    if "password" in data:
        user.password = generate_password_hash(data["password"])

    db.session.commit()

    return jsonify({"message": "User updated"}), 200


# Rota para deletar o usuário autenticado
@app.route("/delete", methods=["DELETE"])
@jwt_required()
def delete():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"}), 200
