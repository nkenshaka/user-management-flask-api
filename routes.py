from flask import request, jsonify
from app import app, db
from models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data or not data.get('name') or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Missing required fields"}), 400

    user = User.query.filter_by(email=data["email"]).first()

    if user:
        return jsonify({"error": "User already exists"}), 400

    new_user = User(name=data["name"], email=data["email"], password=data["password"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Missing required fields"}), 400

    user = User.query.filter_by(email=data["email"]).first()

    if not user or user.password != data["password"]:
        return jsonify({"error": "Invalid credentials"}), 401

    # Gerar o token JWT
    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), 200
