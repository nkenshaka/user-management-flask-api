from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Configurações 
app.config.from_object('config.Config')

# extensões
db = SQLAlchemy(app)
jwt = JWTManager(app)

# rotas e modelos
from routes import *
from models import *

if __name__ == '__main__':
    app.run(debug=True)
