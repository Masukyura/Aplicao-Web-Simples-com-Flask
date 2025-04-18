from flask import Flask
from db import db
from model import Usuario, Produto

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///dados.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # <- sempre bom adicionar isso pra evitar warnings

db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)