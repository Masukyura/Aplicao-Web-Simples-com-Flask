from flask import Flask
from db import db
from app.model import Usuario, Produto
from app.controller import controller
from datetime import datetime


app = Flask(__name__, template_folder='templates', static_folder='static')
@app.template_filter('datetimeformat')
def datetimeformat(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").strftime("%d-%m-%Y")
    except:
        return value  # caso já esteja no formato certo ou inválido
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///dados.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # <- sempre bom adicionar isso pra evitar warnings
app.secret_key = 'sua_chave_secreta'

db.init_app(app)
app.register_blueprint(controller)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)